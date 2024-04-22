from colorama import Fore, Style

print_colors = {
    "dir": Fore.BLUE,
    "file": Fore.GREEN,
    "": Fore.WHITE,
}

def print_out(type: str, line: str):
    print(print_colors.get(type) + line)
    print(Style.RESET_ALL, end="")
