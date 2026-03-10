import os
from colorama import Fore
import time
from modelprocess import upload_dataset

server_url = "https://api.moosaksecurity.space/moosak/upload_dataset.php"


# ---------------- FILE EXTENSIONS ----------------

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".heic", ".heif")
VIDEO_EXT = (".mp4", ".mov", ".avi", ".mkv")


# ---------------- FILE PATH INPUT ----------------

def pick_file(file_type):

    while True:

        print()

        if file_type == "image":
            path = input(Fore.GREEN + "Enter image file path: ").strip()

        elif file_type == "video":
            path = input(Fore.GREEN + "Enter video file path: ").strip()

        else:
            path = input(Fore.GREEN + "Enter file path: ").strip()

        if not os.path.exists(path):
            print(Fore.RED + "File not found. Please enter a valid path.")
            continue

        # Validate extension
        if file_type == "image" and not path.lower().endswith(IMAGE_EXT):
            print(Fore.RED + "Invalid file type. Only image files allowed.")
            continue

        if file_type == "video" and not path.lower().endswith(VIDEO_EXT):
            print(Fore.RED + "Invalid file type. Only video files allowed.")
            continue

        return path


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

            file = pick_file("image")

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

            file = pick_file("image")

            selected_files.append((label, file))


    # ---------------- VIDEO MODEL ----------------
    else:

        print()
        print(Fore.YELLOW + "Now select VIDEO file")

        file = pick_file("video")

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
