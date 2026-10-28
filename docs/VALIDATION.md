# Validation matrix

These are dated observations, not a guarantee for all distributions or devices.

| Kernel | Environment | Evidence | Date |
| --- | --- | --- | --- |
| 7.2.2 | ELRepo kernel-ml, x86_64, T2U Plus | Recorded working hardware baseline | 2026-09 |
| 7.2.7 / 7.2.8 | ELRepo kernel-ml, x86_64 | Recorded compile checks | 2026-09-30 |
| 7.2.8 | T2U Plus, managed mode | Recorded boot, 5 GHz DFS channel 52 and traffic test | 2026-09-30 |
| 7.2.13 | ELRepo kernel-ml (el10), x86_64 | Recorded compile check via DKMS: module builds and is signed | 2026-10-28 |
| 7.2.13 | T2U Plus, managed mode | Recorded boot and 5 GHz link up within 1 s. About 20 minutes after boot the interface began losing its DHCP lease about every 10 minutes (NetworkManager: `error -99 dispatching events`, then `no lease`) while the link stayed associated at -52 to -55 dBm. **Not isolated:** it may be the kernel, this driver, the DHCP client or the setup (a second adapter was on the same subnet); no fault is attributed. A fresh control run on 7.2.8 is in progress (started 2026-10-28 17:47) and is not conclusive yet; this row will be updated. Not yet tested: single adapter, another DHCP client, kernels 7.2.9–7.2.12 | 2026-10-28 |

Source: [maintainer changelog](../CHANGELOG.md). These results do not establish
monitor/AP mode, every USB ID, or every kernel/distribution combination.

The Kernel compatibility CI workflow builds against upstream 7.0, 7.1 and
7.2.8 source trees to exercise compatibility boundaries. Consult its actual
run results before treating a matrix entry as passing. It uses prepared
x86_64 configurations without loading modules or replacing a host kernel.

Submit hardware reports through the issue template. Please state failures as
well as successes and distinguish driver faults from router/DHCP problems.
