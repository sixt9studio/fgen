import os
import random
import time
from pyfiglet import Figlet
from colorama import Fore, init

init(autoreset=True)

matrix_chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def matrix_rain(lines=20, width=60):
    for _ in range(lines):
        line = "".join(random.choice(matrix_chars) for _ in range(width))
        print(Fore.GREEN + line)
        time.sleep(0.03)


def glitch_banner(text):
    fig = Figlet(font="slant")
    banner = fig.renderText(text).split("\n")

    glitch_chars = "!@#$%^&*()"

    for _ in range(12):
        clear()
        for line in banner:
            new_line = ""
            for c in line:
                if c != " " and random.random() < 0.15:
                    new_line += random.choice(glitch_chars)
                else:
                    new_line += c
            print(Fore.GREEN + new_line)
        time.sleep(0.08)

    clear()
    print(Fore.CYAN + fig.renderText(text))


def boot():
    messages = [
        "[•] Initializing FGEN-V6",
        "[•] Loading Matrix Engine",
        "[•] Injecting Fgen protocol",
        "[•] Starting terminal interface",
        "[✓] System Ready"
    ]

    for m in messages:
        print(Fore.GREEN + m)
        time.sleep(0.6)