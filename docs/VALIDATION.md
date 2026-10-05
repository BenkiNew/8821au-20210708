# Validation matrix

These are dated observations, not a guarantee for all distributions or devices.

| Kernel | Environment | Evidence | Date |
| --- | --- | --- | --- |
| 7.2.2 | ELRepo kernel-ml, x86_64, T2U Plus | Recorded working hardware baseline | 2026-09 |
| 7.2.7 / 7.2.8 | ELRepo kernel-ml, x86_64 | Recorded compile checks | 2026-09-30 |
| 7.2.8 | T2U Plus, managed mode | Recorded boot, 5 GHz DFS channel 52 and traffic test | 2026-09-30 |

Source: [maintainer changelog](../CHANGELOG.md). These results do not establish
monitor/AP mode, every USB ID, or every kernel/distribution combination.

The Kernel compatibility CI workflow builds against upstream 7.0, 7.1 and
7.2.8 source trees to exercise compatibility boundaries. Consult its actual
run results before treating a matrix entry as passing. It uses prepared
x86_64 configurations without loading modules or replacing a host kernel.

Submit hardware reports through the issue template. Please state failures as
well as successes and distinguish driver faults from router/DHCP problems.
