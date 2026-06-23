import sys
from colorama import init, Fore, Style

init(autoreset=True)

ICON_ROCKET = "\U0001F680"
ICON_EARTH = "\U0001F30D"
ICON_STAR = "\u2B50"
ICON_SATURN = "\U0001FA90"
ICON_ALERT = "\u26A0\uFE0F"
ICON_CHECK = "\u2705"
ICON_CLOCK = "\u23F0"
ICON_FOLDER = "\U0001F4C1"
ICON_CODE = "\U0001F4BB"
ICON_ORBIT = "\U0001F6E1\uFE0F"
ICON_SUN = "\u2600\uFE0F"
ICON_MOON = "\U0001F319"
ICON_GITHUB = "\U0001F5C4\uFE0F"


def banner():
    print()
    print(f"  {ICON_ROCKET} {Fore.CYAN}{Style.BRIGHT}ASTRO TASKS{Style.RESET_ALL}  {ICON_SATURN}")
    print(f"  {Fore.YELLOW}Pre-flight checklist for developers{Style.RESET_ALL}")
    print()


def print_section(title):
    print(f"\n  {Fore.MAGENTA}{ICON_STAR}  {title}{Style.RESET_ALL}")
    print(f"  {Fore.MAGENTA}{'-' * 40}{Style.RESET_ALL}")


def print_ok(label, value):
    print(f"    {Fore.GREEN}{ICON_CHECK}  {label}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_warn(label, value):
    print(f"    {Fore.YELLOW}{ICON_ALERT}  {label}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_info(label, value):
    print(f"    {Fore.CYAN}{ICON_ORBIT}  {label}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_error(label, value):
    print(f"    {Fore.RED}{ICON_ALERT}  {label}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_table(rows):
    for icon, key, val, status in rows:
        if status == "ok":
            print(f"    {Fore.GREEN}{icon}  {key}:{Style.RESET_ALL} {Fore.WHITE}{val}{Style.RESET_ALL}")
        elif status == "warn":
            print(f"    {Fore.YELLOW}{icon}  {key}:{Style.RESET_ALL} {Fore.WHITE}{val}{Style.RESET_ALL}")
        elif status == "error":
            print(f"    {Fore.RED}{icon}  {key}:{Style.RESET_ALL} {Fore.WHITE}{val}{Style.RESET_ALL}")
        else:
            print(f"    {Fore.CYAN}{icon}  {key}:{Style.RESET_ALL} {Fore.WHITE}{val}{Style.RESET_ALL}")
