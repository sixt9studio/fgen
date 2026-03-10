from ui import clear, matrix_rain, glitch_banner, boot
from menu import show_menu
import time


def main():

    clear()
    matrix_rain()
    time.sleep(0.5)
    glitch_banner("FGEN-V6")
    boot()
    show_menu()


if __name__ == "__main__":
    main()