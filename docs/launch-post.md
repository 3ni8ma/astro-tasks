# Launch drafts — review before posting (do not auto-post)

## r/Python (title)
Show: astro-tasks — one command pre-flight check (GitHub, WakaTime, repo health)

## r/Python (body)
I built a small Python CLI for my morning routine: one command that shows
GitHub notifications + open PRs (via `gh`), WakaTime stats for the last
7 days, and local repo health (dirty branches, unpushed commits).

```bash
pip install astro-tasks
astro check
```

`astro check --json` emits the same data as JSON for piping into other tools.
`astro scan` checks local repos only, `astro log` shows coding stats,
`astro config` shows current configuration.

Requires Python 3.8+, `gh` CLI auth, and a WakaTime config. MIT licensed.
Repo: https://github.com/3ni8ma/astro-tasks — feedback welcome, especially
on the JSON schema and multi-machine WakaTime setups.

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
- [ ] Publish 0.2.0 to PyPI so `pip install` matches GitHub
- [ ] Upload `docs/Astro-Tasks-thumbnail.png` at GitHub repo → Settings → Social preview
- [ ] Pin the repo on your GitHub profile
