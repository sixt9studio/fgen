from tkinter import Tk, filedialog
from colorama import Fore
import time
from modelprocess import upload_dataset

server_url = "https://api.moosaksecurity.space/moosak/upload_dataset.php"

def start_generation(model, encryption, validity):

    print()
    print(Fore.GREEN + "[FGEN] Preparing generation pipeline")

    root = Tk()
    root.withdraw()

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

            file = filedialog.askopenfilename(
                title=f"Select {label} Image",
                filetypes=[
                    ("Image Files", "*.png *.jpg *.jpeg *.heic *.heif"),
                    ("PNG Files", "*.png"),
                    ("JPEG Files", "*.jpg *.jpeg"),
                    ("HEIC Files", "*.heic *.heif")
                ]
            )

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

            file = filedialog.askopenfilename(
                title=f"Select {label} Image",
                filetypes=[
                    ("Image Files", "*.png *.jpg *.jpeg *.heic *.heif"),
                    ("PNG Files", "*.png"),
                    ("JPEG Files", "*.jpg *.jpeg"),
                    ("HEIC Files", "*.heic *.heif")
                ]
            )

            if not file:
                print(Fore.RED + "Selection cancelled.")
                return

            selected_files.append((label, file))


    # ---------------- VIDEO MODEL ----------------
    else:

        print()
        print(Fore.YELLOW + "Now select VIDEO file")
        input(Fore.GREEN + "Press ENTER to open video picker...")

        file = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[
                ("Video Files", "*.mp4 *.mov *.avi *.mkv"),
                ("MP4 Files", "*.mp4"),
                ("MOV Files", "*.mov"),
                ("AVI Files", "*.avi"),
                ("MKV Files", "*.mkv")
            ]
        )

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