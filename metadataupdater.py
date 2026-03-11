import os
import time
import random
import sys
from colorama import Fore, init

init(autoreset=True)

# ---------------- UI ----------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():

    print(Fore.CYAN + """
███╗   ███╗███████╗████████╗ █████╗ 
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
██╔████╔██║█████╗     ██║   ███████║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝

        METADATA UPDATER
""")


# ---------------- FILE VALIDATION ----------------

def get_meta_file():

    while True:

        path = input(Fore.GREEN + "Enter metadata file path (.meta): ").strip()

        if not os.path.exists(path):
            print(Fore.RED + "File does not exist.")
            continue

        if not path.lower().endswith(".meta"):
            print(Fore.RED + "Invalid file. Provide a valid metadata file to update.")
            continue

        return path


# ---------------- PROCESSING ANIMATION ----------------

def processing():

    messages = [
        "Reading metadata structure",
        "Validating metadata blocks",
        "Updating metadata index",
        "Rebuilding metadata mapping",
        "Applying metadata changes",
        "Synchronizing metadata tables",
        "Finalizing metadata update"
    ]

    spinner = ["|", "/", "-", "\\"]
    progress = 0
    start = time.time()

    duration = 15

    print()

    while time.time() - start < duration:

        msg = random.choice(messages)

        for s in spinner:

            bar_len = 30
            filled = int(bar_len * progress / 100)
            bar = "█" * filled + "-" * (bar_len - filled)

            sys.stdout.write(
                "\r" +
                Fore.YELLOW +
                f"[META] {msg} {s} " +
                Fore.CYAN +
                f"[{bar}] {progress}%"
            )

            sys.stdout.flush()

            time.sleep(0.2)

        progress += random.randint(2, 5)

        if progress > 95:
            progress = 95

    print()


# ---------------- MAIN ----------------

def main():

    clear()

    banner()

    print(Fore.YELLOW + "Provide a valid metadata file to update.\n")

    meta_file = get_meta_file()

    print()
    print(Fore.CYAN + f"Selected File : {meta_file}")

    input(Fore.GREEN + "\nPress ENTER to begin metadata update...")

    processing()

    print()
    print(Fore.GREEN + "====================================")
    print(Fore.GREEN + " Metadata Update Completed")
    print(Fore.GREEN + "====================================")
    print(Fore.CYAN + "Metadata updated successfully.")


if __name__ == "__main__":
    main()