import json
import os

REPOS = [
    {"name": "3ni8ma", "dir": os.path.expanduser("~/Coding Projects/3ni8ma")},
    {"name": "cli-tool", "dir": os.path.expanduser("~/Coding Projects/cli-tool")},
    {"name": "TheCoderBros-Website", "dir": os.path.expanduser("~/Coding Projects/TheCoderBros-Website")},
    {"name": "aarushkarak-website", "dir": os.path.expanduser("~/Coding Projects/aarushkarak-website")},
    {"name": "react-hooks", "dir": os.path.expanduser("~/Coding Projects/react-hooks")},
    {"name": "tailwind-plugin", "dir": os.path.expanduser("~/Coding Projects/tailwind-plugin")},
    {"name": "vite-plugin", "dir": os.path.expanduser("~/Coding Projects/vite-plugin")},
    {"name": "astro-tasks", "dir": os.path.expanduser("~/Coding Projects/astro-tasks")},
]

WAKATIME_CFG = os.path.expanduser("~/.wakatime.cfg")
GITHUB_USER = "3ni8ma"
MACHINE_NAME = "Aarushs-MacBook-Pro"

# Per-user overrides live here so a pip install works for anyone.
# Example ~/.config/astro-tasks/config.json:
#   {"github_user": "octocat", "machine_name": "My-Mac",
#    "repos": [{"name": "demo", "dir": "~/code/demo"}]}
CONFIG_PATH = os.path.expanduser("~/.config/astro-tasks/config.json")


def load_user_config():
    """Return user config dict; empty dict when the file is missing/invalid."""
    try:
        with open(CONFIG_PATH) as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def get_github_user():
    return (
        os.environ.get("ASTRO_GITHUB_USER")
        or load_user_config().get("github_user")
        or GITHUB_USER
    )


def get_machine_name():
    return (
        os.environ.get("ASTRO_MACHINE_NAME")
        or load_user_config().get("machine_name")
        or MACHINE_NAME
    )


def get_repos():
    repos = load_user_config().get("repos")
    if isinstance(repos, list):
        return repos
    return REPOS
