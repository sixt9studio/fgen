from colorama import Fore
import time
from generator import start_generation


def encryption_menu(model_name, mode=None):

    print()
    print(Fore.YELLOW + "==============================")
    print(Fore.YELLOW + "     SELECT ENCRYPTION")
    print(Fore.YELLOW + "==============================")

    print(Fore.CYAN + "1. Hash48Bit")
    print(Fore.CYAN + "2. Hash128Bit")
    print(Fore.CYAN + "3. Hash256Bit")

    choice = input(Fore.GREEN + "Select encryption type: ")

    if choice == "1":
        encryption = "Hash48Bit"
    elif choice == "2":
        encryption = "Hash128Bit"
    else:
        encryption = "Hash256Bit"

    validity_menu(model_name, encryption, mode)


def validity_menu(model, encryption, mode=None):

    print()
    print(Fore.YELLOW + "1. One Time")
    print(Fore.YELLOW + "2. 7 Days")
    print(Fore.YELLOW + "3. 30 Days")
    print(Fore.YELLOW + "4. 90 Days")

    choice = input(Fore.GREEN + "Select validity: ")

    validity = ["One Time", "7 Days", "30 Days", "90 Days"][int(choice) - 1]

    confirm_settings(model, encryption, validity, mode)


def confirm_settings(model, encryption, validity, mode=None):

    print()
    print(Fore.CYAN + f"Model Type      : {model}")

    if mode:
        print(Fore.CYAN + f"Video Mode      : {mode}")

    print(Fore.CYAN + f"Encryption Type : {encryption}")
    print(Fore.CYAN + f"Hash Validity   : {validity}")

    confirm = input(
        Fore.GREEN +
        "Proceed with model generation? (Y/N): "
    ).lower()

    if confirm == "y":
        start_generation(model, encryption, validity)