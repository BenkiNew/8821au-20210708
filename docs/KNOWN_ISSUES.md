# Known issues and upstream status

Last updated: 2026-10-29. Facts only; items marked *planned* have not been released yet.

## Maintenance policy

This fork is kept compatible with the **newest ELRepo `kernel-ml`** on EL10. A scheduled check builds `main` against the latest
`kernel-ml-devel` and records the result. Builds are currently clean on kernel-ml 7.2.2, 7.2.8 and 7.2.13 (two toolchain warnings,
see [VALIDATION.md](VALIDATION.md)).

## Upstream / distribution status

| Item | Status |
|---|---|
| In-kernel `rtw88_8821au` in ELRepo `kernel-ml` | **Planned, not released.** ELRepo maintainers replied on [ELRepo bug 0001612](https://elrepo.org/bugs/view.php?id=1612) (2026-10-28): "We will try to make the requested changes in the next update to kernel-ml/lt" and "Will change to: `CONFIG_RTW88_8821AU=m`, `CONFIG_RTW88_8812AU=m`, `CONFIG_RTW88_8814AU=m`". The newest `kernel-ml` checked (7.2.13) still has `CONFIG_RTW88_8821AU` not set. |
| `kmod-rtw88_usb` (ELRepo) | Available for the **stock EL10 kernel** (not for `kernel-ml`); includes RTW88_8821AU/8821CU/8812AU/8814AU/8822CU. Suggested by the maintainers as an alternative. |
| This fork on `kernel-ml` | Works today as an out-of-tree DKMS module. Once the in-kernel driver is released, it becomes an alternative to compare against; this fork stays as the maintained fallback and for features/devices not covered by `rtw88`. A comparison will be recorded here after testing. |

## Known issues

- **5 GHz DHCP lease loss observed on kernel 7.2.13 (not on 7.2.8)** — see [issue 6](https://github.com/BenkiNew/8821au-20210708/issues/6).
  One boot per kernel version, not isolated to the driver versus the kernel or network stack; no claim of causality. Reports from other setups are welcome.

## How this file is maintained

Updated when ELRepo publishes a kernel-ml that changes the driver availability, or when a new reproducible problem is confirmed.
