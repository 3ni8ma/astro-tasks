import os
import subprocess
import json

from . import config, display


def count_unread(notifs):
    """Count notifications with unread=True. Missing key counts as read."""
    return sum(1 for n in (notifs or []) if n.get("unread", False))


def get_notifications():
    result = subprocess.run(
        ["gh", "api", "notifications"],
        capture_output=True, text=True, timeout=15
    )
    if result.returncode != 0:
        return None, result.stderr.strip()
    try:
        data = json.loads(result.stdout)
        return data, None
    except json.JSONDecodeError as e:
        return None, str(e)


def get_open_prs():
    # Run from any tracked repo so gh can find its git context
    cwd = None
    for repo in config.get_repos():
        if os.path.isdir(os.path.join(repo["dir"], ".git")):
            cwd = repo["dir"]
            break
    result = subprocess.run(
        ["gh", "pr", "list", "--author", config.get_github_user(), "--state", "open",
         "--json", "number,title,headRefName,baseRefName"],
        capture_output=True, text=True, timeout=15, cwd=cwd
    )
    if result.returncode != 0:
        return None, result.stderr.strip()
    try:
        data = json.loads(result.stdout)
        return data, None
    except json.JSONDecodeError as e:
        return None, str(e)


def run():
    display.print_section("GitHub Status")

    notifs, err = get_notifications()
    if err:
        display.print_warn("Notifications", f"Could not fetch: {err}")
    else:
        display.print_ok("Unread notifications", str(count_unread(notifs)))

    prs, err = get_open_prs()
    if err:
        display.print_warn("Open PRs", f"Could not fetch: {err}")
    else:
        display.print_ok("Open PRs", str(len(prs)))
        for pr in prs[:5]:
            display.print_info(f"  #{pr['number']}", f"{pr['title']} ({pr['headRefName']} \u2192 {pr['baseRefName']})")
        if len(prs) > 5:
            display.print_info("  ...", f"and {len(prs) - 5} more")
