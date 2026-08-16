# Astro Tasks

[![PyPI version](https://img.shields.io/pypi/v/astro-tasks)](https://pypi.org/project/astro-tasks/)
[![Python](https://img.shields.io/pypi/pyversions/astro-tasks)](https://pypi.org/project/astro-tasks/)
[![Downloads](https://img.shields.io/pypi/dm/astro-tasks)](https://pypi.org/project/astro-tasks/)

> Pre-flight checklist for developers. One command to check GitHub status,
> coding stats, and local repo health before starting work.

Pre-flight checklist for developers. One command to check GitHub status,
coding stats, and local repo health before starting work.

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

## Requirements

- Python 3.8+
- `gh` CLI authenticated (`gh auth status`)
- WakaTime config at `~/.wakatime.cfg`

## License

MIT
