import argparse
import sys

from . import display
from . import config
from . import github_check
from . import hackatime_check
from . import repo_check


def cmd_check(args):
    display.banner()
    github_check.run()
    hackatime_check.run()
    repo_check.run()
    print()


def cmd_scan(args):
    display.banner()
    repo_check.run()
    print()


def cmd_log(args):
    display.banner()
    hackatime_check.run()
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
    p_check.set_defaults(func=cmd_check)

    p_scan = sub.add_parser("scan", help="Scan local repos for issues")
    p_scan.set_defaults(func=cmd_scan)

    p_log = sub.add_parser("log", help="Show today's coding log from Hackatime")
    p_log.set_defaults(func=cmd_log)

    args = parser.parse_args()

    if args.version:
        cmd_version(args)
    elif hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
