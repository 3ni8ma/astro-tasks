import os
import configparser
import subprocess

from colorama import Fore, Style

from . import display, config


def run():
    display.print_section("Configuration")

    waka = os.path.expanduser(config.WAKATIME_CFG)
    if os.path.exists(waka):
        cfg = configparser.ConfigParser()
        cfg.read(waka)
        key = cfg.get("settings", "api_key", fallback=None)
        url = cfg.get("settings", "api_url", fallback=None)
        display.print_ok("WakaTime config", waka)
        display.print_ok("API endpoint", url or "not set")
        display.print_ok("API key", f"{key[:8]}..." if key else "not set")
    else:
        display.print_warn("WakaTime config", f"not found at {waka}")

    r = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True, timeout=10)
    if r.returncode == 0:
        display.print_ok("GitHub auth", "logged in")
    else:
        display.print_warn("GitHub auth", "not logged in (run `gh auth login`)")

    display.print_ok("Tracked repos", str(len(config.REPOS)))
    for repo in config.REPOS:
        git_dir = os.path.join(repo["dir"], ".git")
        exists = os.path.isdir(git_dir)
        icon = f"{Fore.GREEN}[+]{Style.RESET_ALL}" if exists else f"{Fore.YELLOW}[!]{Style.RESET_ALL}"
        status = "exists" if exists else "not cloned"
        print(f"    {icon} {repo['name']}: {status}")
