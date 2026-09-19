# Astro Tasks

[![PyPI version](https://img.shields.io/pypi/v/astro-tasks)](https://pypi.org/project/astro-tasks/)
[![Python](https://img.shields.io/pypi/pyversions/astro-tasks)](https://pypi.org/project/astro-tasks/)
[![Downloads](https://img.shields.io/pypi/dm/astro-tasks)](https://pypi.org/project/astro-tasks/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/3ni8ma/astro-tasks)](https://github.com/3ni8ma/astro-tasks/stargazers)

> Pre-flight checklist for developers. One command to check GitHub status,
> coding stats, and local repo health before starting work.

![Astro Tasks](https://raw.githubusercontent.com/3ni8ma/astro-tasks/main/docs/Astro-Tasks-thumbnail.png)

## Features

- GitHub notifications + open PRs via `gh` CLI
- Coding stats from WakaTime (last 7 days, top projects, languages)
- Local repo health scan (dirty branches, unpushed commits)

## Quick Start

```bash
pip install astro-tasks
astro check
```

## Commands

| Command | Description |
|---------|-------------|
| `astro check` | Full dashboard: GitHub notifications, open PRs, coding stats, repo health |
| `astro check --json` | Same info as JSON (for piping into other tools) |
| `astro scan` | Scan local repos for dirty branches and unpushed commits |
| `astro log` | Show coding stats from WakaTime (last 7 days) |
| `astro config` | Show current configuration (WakaTime, GitHub auth, tracked repos) |
| `astro --version` | Print version |

## Example

```
>>> ASTRO TASKS <<<
  pre-flight checklist

  [*] GitHub Status
  ------------------------------------------
    [+] Unread notifications: 3
    [+] Open PRs: 1

  [*] Coding Stats (Last 7 Days)
  ------------------------------------------
    [+] Total time: 40 hrs 12 mins
    [+] Daily average: 10 hrs 4 mins
    [+] Active days: 4

  [*] Top Projects
  ------------------------------------------
    [+]   react-hooks: 11 hrs 39 mins
    [+]   TheCoderBros-Website: 10 hrs 23 mins

  [*] Languages
  ------------------------------------------
    [+]   TypeScript: 35 hrs 12 mins
    [+]   Python: 7 hrs 53 mins

  [*] Local Repo Scan
  ------------------------------------------
    [+] cli-tool: branch: main
    [!] 3ni8ma: branch: main | 2 unpushed
```

`astro scan` — repos only, no API calls:

```
  [*] Local Repo Scan
  ------------------------------------------
    [+] 3ni8ma: branch: main | dirty
    [+] cli-tool: branch: main | dirty
    [+] TheCoderBros-Website: branch: main
    [+] aarushkarak-website: branch: main
    [+] react-hooks: branch: main
    [+] tailwind-plugin: branch: main | dirty
    [+] vite-plugin: branch: main | dirty
    [+] astro-tasks: branch: main
```

`astro check --json` — same data, machine-readable (truncated):

```json
{
  "github": {
    "unread_notifications": 3,
    "open_prs_count": 1,
    "open_prs": [
      {"number": 1, "title": "...", "headRefName": "feat", "baseRefName": "main"}
    ],
    "errors": {"notifications": null, "prs": null}
  },
  "coding_stats": {"human_readable_total": "40 hrs 12 mins"},
  "coding_stats_error": null,
  "repos": [
    {"name": "astro-tasks", "branch": "main", "unpushed": 0, "dirty": false, "error": null}
  ]
}
```

## Requirements

- Python 3.8+
- `gh` CLI authenticated (`gh auth status`)
- WakaTime config at `~/.wakatime.cfg`

## License

MIT
