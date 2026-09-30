# Журнал змін цього форку

Формат: [Keep a Changelog](https://keepachangelog.com/uk-UA/1.0.0/). Кожен
запис — наша власна зміна поверх `morrownr/8821au-20210708`, з посиланням
на upstream PR (якщо подавався) і датою.

## [Unreleased] — на `main` цього форку

### Виправлено — 2026-09-27
- Межа версії ядра для нового API `remain_on_channel` виправлена з
  `KERNEL_VERSION(7, 0, 0)` на `KERNEL_VERSION(7, 2, 0)` — точну межу, коли
  cfg80211 отримав цей параметр. Ядра `7.0.x`–`7.1.x` помилково вважались
  сумісними й не компілювались.
  upstream: [morrownr#217](https://github.com/morrownr/8821au-20210708/pull/217) (відкритий, без реакції мейнтейнера)

### Додано — 2026-09-12
- `cfg80211_ops.set_cqm_rssi_config` — офіційний callback моніторингу якості
  з'єднання (RSSI-поріг), якого драйвер не реалізовував.
  upstream: [morrownr#212](https://github.com/morrownr/8821au-20210708/pull/212) (відкритий)

### Виправлено — 2026-09-12
- CI: прибрано мертву job `ubuntu-20.04` (образ знято з GitHub-раннерів) і
  `gcc-10` з матриці `ubuntu-22.04`.
  upstream: [morrownr#214](https://github.com/morrownr/8821au-20210708/pull/214) (відкритий)
- Дрібні друкарські помилки в `README.md`/`FAQ.md`, знайдені codespell.
  upstream: [morrownr#213](https://github.com/morrownr/8821au-20210708/pull/213) (відкритий)

### Виправлено — 2026-09-03 / 2026-09-11
- Збірка на ядрі Linux 7.1/7.2 (нові cfg80211-параметри).
  upstream: [morrownr#210](https://github.com/morrownr/8821au-20210708/pull/210) — **влито**
- Регресія збірки на ядрах < 7.1, внесена попереднім фіксом.
  upstream: [morrownr#211](https://github.com/morrownr/8821au-20210708/pull/211) — **влито**
