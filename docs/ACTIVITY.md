# Measuring repository adoption

[Repository activity monitor](https://github.com/BenkiNew/8821au-20210708/actions/workflows/activity-monitor.yml)
runs daily at 07:20 UTC and can be started manually. Each successful run stores
an aggregate snapshot and a readable report for 90 days. Its summary compares
stars, forks, external issues/PRs and release asset downloads with the preceding
successful run. No contributor identities are stored in the artifact.

The first run establishes a baseline. Compare results after 7 and 30 days.
Review snapshots on those dates together with the substance of incoming reports:
a useful hardware report matters more than a cosmetic count increase.

This monitor does not measure page views, clones, source archive downloads or
Discussion participation. Repository traffic needs separate API permissions.
Daily GitHub schedules may run late. Growth does not by itself prove which
change caused it. The workflow does not post promotional messages or issues.

For an owner-authenticated local collector, `--traffic` also stores daily view
and clone buckets from the rolling 14-day traffic API. Archive these snapshots
regularly; do not sum overlapping 14-day totals. Credentials stay in the local
GitHub CLI store and are never committed or uploaded by this workflow.
