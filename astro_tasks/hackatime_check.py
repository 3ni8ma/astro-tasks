import configparser
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

from . import config, display


def get_today_heartbeats():
    cfg = configparser.ConfigParser()
    cfg.read(config.WAKATIME_CFG)
    api_key = cfg.get("settings", "api_key", fallback=None)
    api_url = cfg.get("settings", "api_url", fallback=None)

    if not api_key or not api_url:
        return None, "No API config found in ~/.wakatime.cfg"

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    url = f"{api_url}/users/current/heartbeats?date={today}"

    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("X-Machine-Name", "Aarushs-MacBook-Pro")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", []), None
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, OSError) as e:
        return None, str(e)


def run():
    display.print_section("Today's Coding Log")

    beats, err = get_today_heartbeats()
    if err:
        display.print_warn("Hackatime", f"Could not fetch: {err}")
        return

    if not beats:
        display.print_info("Heartbeats", "No heartbeats recorded today yet")
        return

    total_secs = 0
    projects = {}
    languages = {}
    for b in beats:
        proj = b.get("project", "unknown")
        lang = b.get("language", "unknown")
        projects[proj] = projects.get(proj, 0) + 1
        languages[lang] = languages.get(lang, 0) + 1
        if b.get("time"):
            total_secs += 1

    hours = total_secs // 3600
    minutes = (total_secs % 3600) // 60

    display.print_ok("Total heartbeats", str(len(beats)))
    display.print_ok("Est. time", f"{hours}h {minutes}m")

    display.print_info("Projects today", ", ".join(sorted(projects.keys())))
    display.print_info("Languages today", ", ".join(sorted(languages.keys())))

    display.print_section("Recent Heartbeats")
    for b in beats[-5:]:
        t = b.get("time", 0)
        if isinstance(t, (int, float)):
            ts = datetime.fromtimestamp(t, tz=timezone.utc).strftime("%H:%M:%S")
        else:
            ts = str(t)
        proj = b.get("project", "?")
        entity = b.get("entity", "?").split("/")[-1]
        display.print_info(f"  {ts}", f"{proj} / {entity}")
