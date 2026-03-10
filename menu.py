from colorama import Fore
import time
from face_model import face_model
from body_model import body_model
from custom_model import custom_model


def show_menu():

    print()
    print(Fore.YELLOW + "==============================")
    print(Fore.YELLOW + "         FGEN-V6 MENU")
    print(Fore.YELLOW + "==============================")

    print(Fore.CYAN + "1. FGen Face Model (Image Model)")
    print(Fore.CYAN + "2. FGen Body Model (Image Model)")
    print(Fore.CYAN + "3. FGen Custom Model (Video Model)")
    print()

    choice = input(Fore.GREEN + "Select option (1-3): ")

    if choice == "1":
        face_model()

    elif choice == "2":
        body_model()

    elif choice == "3":
        custom_video_menu()

    else:
        print(Fore.RED + "Invalid option")
        time.sleep(1)
        show_menu()


def custom_video_menu():

    print()
    print(Fore.YELLOW + "==============================")
    print(Fore.YELLOW + "     VIDEO MODEL SETTINGS")
    print(Fore.YELLOW + "==============================")

    print(Fore.CYAN + "1. 60 Second Video (Low)")
    print(Fore.CYAN + "2. 120 Second Video (Medium)")
    print(Fore.CYAN + "3. 300 Second Video (Strong)")
    print()

    choice = input(Fore.GREEN + "Select video processing mode (1-3): ")

    if choice == "1":
        custom_model("60s")

    elif choice == "2":
        custom_model("120s")

    elif choice == "3":
        custom_model("300s")

    else:
        print(Fore.RED + "Invalid option")
        time.sleep(1)
        custom_video_menu()