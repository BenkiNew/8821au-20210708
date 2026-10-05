#!/usr/bin/env python3
"""Collect aggregate public engagement without storing contributor identities."""
import argparse
import datetime
import json
import os
import pathlib
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--traffic', action='store_true')
parser.add_argument('--output', type=pathlib.Path, required=True)
args = parser.parse_args()
repo = 'BenkiNew/8821au-20210708'
owner = repo.split('/')[0]


def api(path):
    return json.loads(subprocess.check_output(['gh', 'api', path], text=True))


def items(path):
    result = []
    page = 1
    while True:
        rows = api(f'{path}&per_page=100&page={page}')
        result.extend(rows)
        if len(rows) < 100:
            return result
        page += 1


metadata = api(f'repos/{repo}')
issues = items(f'repos/{repo}/issues?state=all')
external = [x for x in issues if x['user']['login'].lower() != owner.lower()
            and x['user']['type'] != 'Bot']
releases = items(f'repos/{repo}/releases?')
metrics = {
    'stars': metadata['stargazers_count'],
    'forks': metadata['forks_count'],
    'external_issues_total': sum('pull_request' not in x for x in external),
    'external_prs_total': sum('pull_request' in x for x in external),
    'release_downloads_total': sum(a['download_count'] for r in releases for a in r['assets']),
}
snapshot = {'captured_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'repository': repo, 'metrics': metrics}
if args.traffic:
    snapshot['traffic_14_days'] = {kind: api(f'repos/{repo}/traffic/{kind}')
                                  for kind in ['views', 'clones']}
args.output.mkdir(parents=True, exist_ok=True)
previous_path = args.output / 'snapshot.json'
previous = json.loads(previous_path.read_text()) if previous_path.exists() else None
snapshot['delta'] = {k: v - previous['metrics'][k] for k, v in metrics.items()} if previous else None
snapshot['previous_capture'] = previous['captured_at'] if previous else None
with (args.output / 'history.jsonl').open('a') as handle:
    handle.write(json.dumps(snapshot) + '\n')
previous_path.write_text(json.dumps(snapshot, indent=2) + '\n')
lines = ['# Repository engagement', '', f"Captured: {snapshot['captured_at']}", '',
         '| Metric | Total | Change since previous snapshot |', '| --- | ---: | ---: |']
for key, value in metrics.items():
    delta = snapshot['delta'][key] if previous else 'baseline'
    lines.append(f'| {key} | {value} | {delta} |')
lines += ['', 'External means non-owner, non-bot issue/PR authors. Downloads count release',
          'assets only, not source archives. These signals do not prove causation.',
          'Compare weekly and monthly results; a zero baseline is a valid observation.',
          'GitHub Actions omits traffic; the local --traffic collector includes it.']
if args.traffic:
    lines += ['', '## Traffic (rolling 14-day windows; do not sum successive totals)', '']
    for kind, data in snapshot['traffic_14_days'].items():
        lines.append(f"- {kind}: {data['count']}, unique: {data['uniques']}")
report = '\n'.join(lines) + '\n'
(args.output / 'report.md').write_text(report)
if os.environ.get('GITHUB_STEP_SUMMARY'):
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as handle:
        handle.write(report)
print(report)
