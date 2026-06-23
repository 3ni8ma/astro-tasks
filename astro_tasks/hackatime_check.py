import configparser
import json
import urllib.request
import urllib.error

from . import config, display


def get_stats():
    cfg = configparser.ConfigParser()
    cfg.read(config.WAKATIME_CFG)
    api_key = cfg.get("settings", "api_key", fallback=None)
    api_url = cfg.get("settings", "api_url", fallback=None)

    if not api_key or not api_url:
        return None, "No API config found in ~/.wakatime.cfg"

    url = f"{api_url}/users/current/stats/last_7_days"

    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("X-Machine-Name", "Aarushs-MacBook-Pro")
    req.add_header("Accept", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", {}), None
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, OSError) as e:
        return None, str(e)


def run():
    display.print_section("Coding Stats (Last 7 Days)")

    stats, err = get_stats()
    if err:
        display.print_warn("Hackatime", f"Could not fetch: {err}")
        return

    if not stats:
        display.print_info("Hackatime", "No data yet")
        return

    total = stats.get("human_readable_total", "N/A")
    daily_avg = stats.get("human_readable_daily_average", "N/A")
    days = stats.get("days_including_holidays", 0)

    display.print_ok("Total time", total)
    display.print_ok("Daily average", daily_avg)
    display.print_ok("Active days", str(days))

    projects = stats.get("projects", [])
    if projects:
        display.print_section("Top Projects")
        for p in sorted(projects, key=lambda x: x.get("total_seconds", 0), reverse=True)[:5]:
            name = p.get("name", "?")
            text = p.get("text", "0")
            display.print_ok(f"  {name}", text)

    languages = stats.get("languages", [])
    if languages:
        display.print_section("Languages")
        for lang in sorted(languages, key=lambda x: x.get("total_seconds", 0), reverse=True):
            name = lang.get("name", "?")
            text = lang.get("text", "0")
            display.print_ok(f"  {name}", text)

    categories = stats.get("categories", [])
    if categories:
        display.print_section("Categories")
        for c in categories:
            display.print_ok(f"  {c.get('name', '?')}", c.get("text", "0"))
