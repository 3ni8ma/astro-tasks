import sys
from colorama import init, Fore, Style

init(autoreset=True)


def banner():
    print()
    print(f"  {Fore.CYAN}{Style.BRIGHT}>>> ASTRO TASKS <<<{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}pre-flight checklist{Style.RESET_ALL}")
    print()


def print_section(title):
    print(f"\n  {Fore.MAGENTA}[*] {title}{Style.RESET_ALL}")
    print(f"  {Fore.MAGENTA}{'-' * 42}{Style.RESET_ALL}")


def print_ok(label, value):
    print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} {label}: {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_warn(label, value):
    print(f"    {Fore.YELLOW}[!]{Style.RESET_ALL} {label}: {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_info(label, value):
    print(f"    {Fore.CYAN}[*]{Style.RESET_ALL} {label}: {Fore.WHITE}{value}{Style.RESET_ALL}")


def print_error(label, value):
    print(f"    {Fore.RED}[x]{Style.RESET_ALL} {label}: {Fore.WHITE}{value}{Style.RESET_ALL}")
