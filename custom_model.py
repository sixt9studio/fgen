from encryption import encryption_menu
from colorama import Fore

def custom_model(mode):

    print()
    print(Fore.GREEN + f"Selected video processing mode: {mode}")

    # pass mode to encryption step
    encryption_menu("FGen Custom Video Model", mode)