import os
import random
import sys
import time
from colorama import Fore, init

init(autoreset=True)

r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = r"""
 _   _ ____  _        ____ _
| | | |  _ \| |      / ___| | ___  __ _ _ __   ___ _ __
| | | | |_) | |     | |   | |/ _ \/ _` | '_ \ / _ \ '__|
| |_| |  _ <| |___  | |___| |  __/ (_| | | | |  __/ |
 \___/|_| \_\_____|  \____|_|\___|\__,_|_| |_|\___|_|
               ./By, Sheikh Nightshader
"""
    for line in x.split("\n"):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        sys.stdout.flush()
        time.sleep(0.02)

def clean_urls(file_path):
    cleaned_urls = []
    with open(file_path, 'r') as file:
        for url in file.readlines():
            url = url.strip()
            if url.startswith(("http://", "https://")):
                protocol = url.split("://")[0] + "://"
                domain = url.split("://")[1].split("/")[0]
                cleaned_urls.append(protocol + domain)
    output_file = "cleaned.txt"
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(set(cleaned_urls)))
    print(f"{g}Cleaned URLs saved to {output_file}")

def main():
    cls()
    print_logo()
    file_path = input(f"{y}Path to your urls.txt file: ").strip()
    if os.path.isfile(file_path):
        clean_urls(file_path)
    else:
        print(f"{r}Invalid file path :(")

if __name__ == "__main__":
    main()
