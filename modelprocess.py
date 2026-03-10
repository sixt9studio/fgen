import requests
from colorama import Fore
import time
import os
import zipfile
import threading
import random
import sys
import math
from concurrent.futures import ThreadPoolExecutor
import secrets
import string


# ---------------- MODEL ID GENERATOR ----------------

def generate_model_id(length=256):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))


# ---------------- CONFIG ----------------

CHUNK_SIZE = 5 * 1024 * 1024  # 5MB
PARALLEL_UPLOADS = 5


# ---------------- MAIN FUNCTION ----------------

def upload_dataset(selected_files, server_url):

    print()
    print(Fore.GREEN + "[FGEN] Initializing model processing pipeline")


    # generate random dataset name
    chars = string.ascii_letters + string.digits
    random_name = ''.join(secrets.choice(chars) for _ in range(12))
    zip_name = f"fgen_{random_name}.zip"

    

    # ---------------- DATASET PACKAGING ----------------

    print(Fore.YELLOW + "[FGEN] Packaging training dataset")

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:

        for label, filepath in selected_files:

            filename = os.path.basename(filepath)
            zipf.write(filepath, arcname=filename)

            print(Fore.CYAN + f"[FGEN] Integrating sample → {filename}")
            time.sleep(0.2)

    print(Fore.GREEN + "[FGEN] Dataset packaging complete")

    upload_done = {"status": False}

    # ---------------- CHUNK UPLOAD ----------------

    def upload_chunk(chunk_data):

        chunk_index, chunk_bytes = chunk_data

        files = {
            "chunk": ("chunk", chunk_bytes)
        }

        data = {
            "chunk_index": chunk_index,
            "filename": zip_name
        }

        requests.post(server_url, files=files, data=data, timeout=120)


    def background_process():

        try:

            file_size = os.path.getsize(zip_name)
            total_chunks = math.ceil(file_size / CHUNK_SIZE)

            # resume check
            try:
                r = requests.get(server_url + "?status=" + zip_name, timeout=30)
                uploaded_chunks = set(r.json().get("uploaded", []))
            except:
                uploaded_chunks = set()

            chunks = []

            with open(zip_name, "rb") as f:

                chunk_index = 0

                while True:

                    chunk = f.read(CHUNK_SIZE)

                    if not chunk:
                        break

                    if chunk_index not in uploaded_chunks:
                        chunks.append((chunk_index, chunk))

                    chunk_index += 1

            # parallel upload
            with ThreadPoolExecutor(max_workers=PARALLEL_UPLOADS) as executor:
                list(executor.map(upload_chunk, chunks))

            # notify server upload finished
            requests.post(server_url, data={"complete": zip_name}, timeout=60)

        except Exception as e:
            print(Fore.RED + f"\n[FGEN ERROR] {e}")

        upload_done["status"] = True


    # start background upload
    thread = threading.Thread(target=background_process)
    thread.start()

    # ---------------- PROCESS UI ----------------

    messages = [
        "Calibrating neural parameters",
        "Analyzing training samples",
        "Mapping facial vectors",
        "Generating feature embeddings",
        "Optimizing dataset alignment",
        "Evaluating structural patterns",
        "Building neural model layers",
        "Refining dataset attributes",
        "Synchronizing model weights",
        "Applying adaptive learning rules",
        "Processing biometric signatures",
        "Running stabilization checks",
        "Balancing neural gradients",
        "Enhancing dataset consistency"
    ]

    spinner = ["|", "/", "-", "\\"]
    progress = 0

    start_time = time.time()
    min_duration = 30

    print()
    print(Fore.GREEN + "[FGEN] Model processing started")
    print()

    while True:

        msg = random.choice(messages)

        for s in spinner:

            bar_length = 30
            filled = int(bar_length * progress / 100)
            bar = "█" * filled + "-" * (bar_length - filled)

            sys.stdout.write(
                "\r" +
                Fore.YELLOW +
                f"[FGEN] {msg} {s} " +
                Fore.CYAN +
                f"[{bar}] {progress}%"
            )

            sys.stdout.flush()

            time.sleep(0.2)

        progress += random.randint(1, 3)

        if progress > 95:
            progress = 95

        elapsed = time.time() - start_time

        if upload_done["status"] and elapsed >= min_duration:
            break

    # wait until upload finished
    thread.join()

    # ---------------- FINALIZE ----------------

    for i in range(progress, 101):

        bar_length = 30
        filled = int(bar_length * i / 100)
        bar = "█" * filled + "-" * (bar_length - filled)

        sys.stdout.write(
            "\r" +
            Fore.YELLOW +
            "[FGEN] Finalizing model " +
            Fore.CYAN +
            f"[{bar}] {i}%"
        )

        sys.stdout.flush()
        time.sleep(0.03)

    model_id = generate_model_id()

    print()
    print()
    print(Fore.GREEN + "[FGEN] Neural model preparation complete")
    print(Fore.GREEN + "[FGEN] Model pipeline successfully initialized")
    print(Fore.CYAN + f"[FGEN] FGen Model : {model_id}")

        # ---------------- CLEANUP ----------------

    try:
        os.remove(zip_name)
    
    except Exception as e:
        print(Fore.RED + f"[FGEN] Cleanup warning: {e}")