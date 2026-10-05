# Contributing

Report driver bugs in Issues and usage questions in Discussions. Check existing
reports first. Include the driver commit or release, distribution, exact kernel,
compiler, USB ID, DKMS/build result, and steps to reproduce.

Remove passwords, network names, MAC/IP addresses and other personal data from
logs. Do not publish complete system logs when a small relevant excerpt suffices.

Keep patches focused and preserve GPLv2 attribution. Explain the root cause and
kernel API boundary for compatibility changes. Include a failing-before and
passing-after build or regression check where applicable. Documentation changes
need only relevant spelling, link and consistency checks.

Hardware reports are welcome: adapter USB ID, kernel, driver commit, band,
connection duration and tested features. Label compile-only checks explicitly.
Do not interrupt a production connection just to collect a test report.

See [validation](docs/VALIDATION.md). CI builds modules but never loads them.
