# Про цей форк

Це самостійно підтримуваний форк `morrownr/8821au-20210708`, який ми
ведемо для власного парку серверів (адаптер T2U Plus, чіп `rtl8821au`,
kernel-ml 7.x). Upstream-мейнтейнер `@morrownr` офіційно відійшов від
активного супроводу (нотатка нижче) — наші виправлення для ядер 7.x
подаються туди як PR з ввічливості, але **застосовуються в `main` цього
форку одразу**, не чекаючи на злиття. Повна хронологія наших змін —
[`CHANGELOG.md`](../CHANGELOG.md).

- **Ліцензія:** `LICENSE` — GNU GPLv2, авторське право Realtek Corporation,
  успадкована без змін. Наші власні зміни поширюються на тих самих умовах.
- **GitHub Actions:** увімкнено, збірка й перевірки запускаються на кожен
  push у `main` цього форку та на кожен PR.
- **Питання/PR:** [issues цього форку](https://github.com/BenkiNew/8821au-20210708/issues) — для багів і PR.
- **Питання по використанню:** [Discussions → Q&A](https://github.com/BenkiNew/8821au-20210708/discussions/categories/q-a) —
  встановлення, ядра, 5 ГГц/DFS, поради. Якщо відповідь допомогла, позначте її прийнятою.

---

Оригінальна примітка `@morrownr` (upstream):

Notice: An updated standards compliant (mac80211), in-kernel driver for rtl8821/11au chipset based adapters and modules is available and as of kernel 6.14 is of good quality. If your distro uses kernel 6.14 or later, there is no need to install this driver. The in-kernel driver is part of the rtw88 series of drivers. The in-kernel driver is Linux Standards compliant (mac80211) and is a much better driver than this one. This driver will no longer get API related updates beyond kernel 6.14 (unless provided by a user). If you use a kernel prior to 6.14, it is possible to use the new standards compliant driver by going to the following repo:

https://github.com/lwfinger/rtw88

If you decide to use the in-kernel driver, remember to first remove the driver in this repo. You can run the following to remove the driver in this repo:

$ sudo sh remove-driver.sh

It has been my pleasure to maintain this driver for the last several years. Thanks to all of those who helped.

Remember: Ask not what your operating system can do for you, but what you can do for your operating system.

Regards,

@morrownr


