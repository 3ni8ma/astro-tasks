import subprocess
import os

from . import config, display


def git_status(repo_dir):
    if not os.path.isdir(os.path.join(repo_dir, ".git")):
        return None, None, "not a git repo"

    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_dir, stderr=subprocess.DEVNULL, timeout=10
        ).decode().strip()
    except subprocess.CalledProcessError:
        return None, None, "could not determine branch"

    unpushed = 0
    try:
        result = subprocess.check_output(
            ["git", "log", "--oneline", f"origin/{branch}..HEAD"],
            cwd=repo_dir, stderr=subprocess.DEVNULL, timeout=10
        ).decode().strip()
        unpushed = len([l for l in result.split("\n") if l.strip()]) if result else 0
    except subprocess.CalledProcessError:
        unpushed = -1

    dirty = False
    try:
        result = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=repo_dir, stderr=subprocess.DEVNULL, timeout=10
        ).decode().strip()
        dirty = bool(result)
    except subprocess.CalledProcessError:
        dirty = False

    return branch, {"unpushed": unpushed, "dirty": dirty}, None


def run():
    display.print_section("Local Repo Scan")

    for repo in config.REPOS:
        name = repo["name"]
        d = repo["dir"]
        branch, info, err = git_status(d)

        if err:
            display.print_warn(name, f"Error: {err}")
            continue

        parts = [f"branch: {branch}"]
        if info["dirty"]:
            parts.append(f"{display.ICON_ALERT} dirty")
        if info["unpushed"] > 0:
            parts.append(f"{display.ICON_ROCKET} {info['unpushed']} unpushed")
        elif info["unpushed"] == -1:
            parts.append("no remote tracking")

        display.print_ok(name, " | ".join(parts))
