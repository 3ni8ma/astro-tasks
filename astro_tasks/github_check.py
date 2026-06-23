import subprocess
import json

from . import config, display


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
    result = subprocess.run(
        ["gh", "pr", "list", "--author", config.GITHUB_USER, "--state", "open",
         "--json", "number,title,headRefName,baseRefName"],
        capture_output=True, text=True, timeout=15
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
        unread = sum(1 for n in notifs if not n.get("unread", False) is False)
        display.print_ok("Unread notifications", str(unread))

    prs, err = get_open_prs()
    if err:
        display.print_warn("Open PRs", f"Could not fetch: {err}")
    else:
        display.print_ok("Open PRs", str(len(prs)))
        for pr in prs[:5]:
            display.print_info(f"  #{pr['number']}", f"{pr['title']} ({pr['headRefName']} \u2192 {pr['baseRefName']})")
        if len(prs) > 5:
            display.print_info("  ...", f"and {len(prs) - 5} more")
