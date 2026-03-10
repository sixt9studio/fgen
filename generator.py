import os
import subprocess
from colorama import Fore
import time
from modelprocess import upload_dataset

# Try tkinter (for Windows/Linux)
try:
    from tkinter import Tk, filedialog
    tkinter_available = True
except:
    tkinter_available = False

server_url = "https://api.moosaksecurity.space/moosak/upload_dataset.php"


# ---------------- FILE PICKER ----------------

def pick_file(file_type):

    # If running in Termux
    if "com.termux" in os.environ.get("PREFIX", ""):

        while True:

            try:
                path = subprocess.check_output(
                    ["termux-file-picker", "-m", file_type],
                    text=True
                ).strip()

                if path and os.path.exists(path):
                    return path

                print(Fore.RED + "No file selected. Please try again.")

            except:
                print(Fore.RED + "File picker closed. Try again.")

    # Desktop (tkinter)
    elif tkinter_available:

        root = Tk()
        root.withdraw()

        if file_type == "image/*":
            path = filedialog.askopenfilename(
                filetypes=[
                    ("Image Files", "*.png *.jpg *.jpeg *.heic *.heif")
                ]
            )
            return path

        elif file_type == "video/*":
            path = filedialog.askopenfilename(
                filetypes=[
                    ("Video Files", "*.mp4 *.mov *.avi *.mkv")
                ]
            )
            return path

    return None


# ---------------- MAIN FUNCTION ----------------

def start_generation(model, encryption, validity):

    print()
    print(Fore.GREEN + "[FGEN] Preparing generation pipeline")

    selected_files = []

    # ---------------- FACE MODEL ----------------
    if "Face" in model:

        prompts = [
            ("Left View", "Now select LEFT VIEW face image"),
            ("Front View", "Now select FRONT VIEW face image"),
            ("Right View", "Now select RIGHT VIEW face image")
        ]

        for label, message in prompts:

            print()
            print(Fore.YELLOW + message)
            input(Fore.GREEN + "Press ENTER to open image picker...")

            file = pick_file("image/*")

            if not file:
                print(Fore.RED + "Selection cancelled.")
                return

            selected_files.append((label, file))


    # ---------------- BODY MODEL ----------------
    elif "Body" in model:

        prompts = [
            ("Upper Body", "Now select UPPER BODY image"),
            ("Full Body", "Now select FULL BODY image"),
            ("Lower Body", "Now select LOWER BODY image")
        ]

        for label, message in prompts:

            print()
            print(Fore.YELLOW + message)
            input(Fore.GREEN + "Press ENTER to open image picker...")

            file = pick_file("image/*")

            if not file:
                print(Fore.RED + "Selection cancelled.")
                return

            selected_files.append((label, file))


    # ---------------- VIDEO MODEL ----------------
    else:

        print()
        print(Fore.YELLOW + "Now select VIDEO file")
        input(Fore.GREEN + "Press ENTER to open video picker...")

        file = pick_file("video/*")

        if not file:
            print(Fore.RED + "No video selected.")
            return

        selected_files.append(("Video", file))


    # ---------------- SHOW SELECTED FILES ----------------

    print()
    print(Fore.GREEN + "==============================")
    print(Fore.GREEN + "      SELECTED FILES")
    print(Fore.GREEN + "==============================")

    for label, file in selected_files:
        print(Fore.CYAN + f"{label}: {file}")


    # ---------------- FINAL CONFIRMATION ----------------

    print()
    confirm = input(
        Fore.GREEN +
        "Continue model generation with selected files? (Y/N): "
    ).strip().lower()

    if confirm == "y":

        print()
        print(Fore.GREEN + "[FGEN] Model generation started...")
        time.sleep(1)

        upload_dataset(selected_files, server_url)

    else:
        print(Fore.RED + "Model generation cancelled.")
