import argparse
import sys

from . import display
from . import config
from . import github_check
from . import wakatime_check
from . import repo_check
from . import config_check


def collect_check_data():
    notifs, notifs_err = github_check.get_notifications()
    prs, prs_err = github_check.get_open_prs()
    stats, stats_err = wakatime_check.get_stats()

    repos = []
    for repo in config.REPOS:
        branch, info, err = repo_check.git_status(repo["dir"])
        repos.append({
            "name": repo["name"],
            "dir": repo["dir"],
            "branch": branch,
            "unpushed": info["unpushed"] if info else None,
            "dirty": info["dirty"] if info else None,
            "error": err,
        })

    return {
        "github": {
            "notifications": notifs if notifs_err is None else None,
            "unread_notifications": sum(1 for n in (notifs or []) if n.get("unread")) if notifs_err is None else None,
            "open_prs": prs if prs_err is None else None,
            "open_prs_count": len(prs or []) if prs_err is None else None,
            "errors": {"notifications": notifs_err, "prs": prs_err},
        },
        "coding_stats": stats if stats_err is None else None,
        "coding_stats_error": stats_err,
        "repos": repos,
    }


def cmd_check(args):
    if args.json:
        import json
        print(json.dumps(collect_check_data(), indent=2, default=str))
        return
    display.banner()
    github_check.run()
    wakatime_check.run()
    repo_check.run()
    print()


def cmd_scan(args):
    display.banner()
    repo_check.run()
    print()


def cmd_log(args):
    display.banner()
    wakatime_check.run()
    print()


def cmd_config(args):
    display.banner()
    config_check.run()
    print()


def cmd_version(args):
    from . import __version__
    print(f"astro-tasks v{__version__}")


def main():
    parser = argparse.ArgumentParser(
        prog="astro",
        description="Astro Tasks \u2014 Pre-flight checklist for developers",
    )
    parser.add_argument("--version", action="store_true", help="Show version")

    sub = parser.add_subparsers(dest="command", title="Commands")

    p_check = sub.add_parser("check", help="Full pre-flight check (GitHub + coding + repos)")
    p_check.add_argument("--json", action="store_true", help="Output as JSON")
    p_check.set_defaults(func=cmd_check)

    p_scan = sub.add_parser("scan", help="Scan local repos for issues")
    p_scan.set_defaults(func=cmd_scan)

    p_log = sub.add_parser("log", help="Show today's coding log from WakaTime")
    p_log.set_defaults(func=cmd_log)

    p_config = sub.add_parser("config", help="Show current configuration")
    p_config.set_defaults(func=cmd_config)

    args = parser.parse_args()

    if args.version:
        cmd_version(args)
    elif hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
