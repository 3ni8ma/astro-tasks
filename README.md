# Astro Tasks 🚀🪐

**Pre-flight checklist for developers.** One command to check GitHub status, today's coding stats, and local repo health before you start coding.

## Quick Start

```bash
pip install -e .
astro check
```

## Commands

| Command | What it does |
|---------|-------------|
| `astro check` | Full pre-flight dashboard — GitHub notifications, open PRs, coding stats, repo health |
| `astro scan` | Scan all local repos for dirty branches, unpushed commits, stale remotes |
| `astro log` | Show last 7 days coding stats from Hackatime |
| `astro --version` | Show version |

## Example

```
🚀 ASTRO TASKS  🪐
  Pre-flight checklist for developers

  ⭐  GitHub Status
    ✅  Unread notifications: 3
    ✅  Open PRs: 1

  ⭐  Coding Stats (Last 7 Days)
    ✅  Total time: 40 hrs 12 mins
    ✅  Daily average: 10 hrs 4 mins
    ✅  Active days: 4

  ⭐  Top Projects
    ✅    react-hooks: 11 hrs 39 mins
    ✅    TheCoderBros-Website: 10 hrs 23 mins

  ⭐  Languages
    ✅    TypeScript: 35 hrs 12 mins
    ✅    Python: 7 hrs 53 mins

  ⭐  Local Repo Scan
    ✅  cli-tool: branch: main
    ✅  3ni8ma: branch: main | 🚀 2 unpushed
```

## Requirements

- Python 3.8+
- `gh` CLI authenticated (`gh auth status`)
- Hackatime/WakaTime config at `~/.wakatime.cfg`

## License

MIT
