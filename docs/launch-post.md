# Launch draft — review before publishing (do not auto-post)

## dev.to (title)
A one-command pre-flight checklist for developers: astro-tasks

## dev.to (body)
Before starting work I used to open three tabs: GitHub notifications,
WakaTime dashboard, and `git status` across repos. astro-tasks puts that
in one terminal command.

`pip install astro-tasks`, then `astro check`. That's GitHub status,
coding stats (last 7 days, top projects, languages), and a local repo
scan. `--json` gives you machine-readable output; `scan`, `log`, and
`config` cover the subsets.

Caveats: it shells out to `gh`, so you need `gh auth login`, and coding
stats need a WakaTime config at `~/.wakatime.cfg`. Python 3.8+, MIT.

https://github.com/3ni8ma/astro-tasks

## Checklist before posting
- [x] Publish 0.2.0 to PyPI so `pip install` matches GitHub (live 2026-09-19)
- [x] Upload `docs/Astro-Tasks-thumbnail.png` at GitHub repo → Settings → Social preview (done 2026-09-19)
- [x] Pin the repo on your GitHub profile (done 2026-09-19, astro-tasks first of 6)
