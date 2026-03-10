import os
import time
import random
import requests
import sys
from colorama import Fore, init

init(autoreset=True)

SERVER_URL = "https://api.moosaksecurity.space/moosak/dmca_upload_terminal.php"

matrix_chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ---------------- UI ----------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def matrix_rain(lines=20, width=60):
    for _ in range(lines):
        line = "".join(random.choice(matrix_chars) for _ in range(width))
        print(Fore.GREEN + line)
        time.sleep(0.02)

def banner():
    print(Fore.CYAN + """
██████╗ ███╗   ███╗ ██████╗ █████╗ 
██╔══██╗████╗ ████║██╔════╝██╔══██╗
██║  ██║██╔████╔██║██║     ███████║
██║  ██║██║╚██╔╝██║██║     ██╔══██║
██████╔╝██║ ╚═╝ ██║╚██████╗██║  ██║
╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝
        FGEN DMCA PANEL
""")

# ---------------- OPTIONS ----------------

height = ["135","140","145","150","155","160","165","170","175","180","185","190","195","200","205","210"]
weight = ["30","35","40","45","50","55","60","65","70","75","80","90","100","120","150","180","200"]
shoulder = ["28","30","32","34","36","38","40","42","45","48","50","55","60"]
chest_male = ["65","70","75","80","85","90","95","100","105","110","115","120","130","140","150"]
waist = ["50","55","60","65","70","75","80","85","90","100","110","120","140","160"]
hip = ["60","65","70","75","80","85","90","95","100","110","120","140","160","170"]
thigh = ["30","35","40","45","50","55","60","65","70","80","90","100"]
bust = ["65","70","75","80","85","90","95","100","105","110","120","130","140"]
underbust = ["60","65","70","75","80","85","90","95","100","105","110"]
cup = ["AA","A","B","C","D","DD","E","F","G"]

# ---------------- MENU ----------------

def select_option(title, options):

    print()
    print(Fore.YELLOW + f"Select {title}")

    for i,opt in enumerate(options):
        print(Fore.CYAN + f"{i+1}. {opt}")

    choice = int(input(Fore.GREEN + "Select option: "))
    return options[choice-1]

# ---------------- SEND DMCA ----------------

def send_dmca_to_server(reporter, gender, model, data):

    print()
    print(Fore.YELLOW + "[FGEN] Preparing DMCA documentation")

    lines = []
    lines.append("DMCA TAKEDOWN REQUEST")
    lines.append("--------------------")
    lines.append(f"Reporter: {reporter}")
    lines.append(f"Gender: {gender}")
    lines.append(f"Model ID: {model}")
    lines.append("")

    for k,v in data.items():
        lines.append(f"{k}: {v}")

    content = "\n".join(lines)

    filename = f"dmca_{model[:10]}.txt"

    files = {
        "dmca_file": (filename, content)
    }

    try:
        requests.post(SERVER_URL, files=files, timeout=60)
    except:
        pass

    # processing animation

    spinner = ["|","/","-","\\"]
    messages = [
        "Verifying ownership claim",
        "Analyzing biometric references",
        "Preparing legal documentation",
        "Submitting takedown request",
        "Registering DMCA record",
        "Securing removal authorization"
    ]

    progress = 0

    print()
    print(Fore.GREEN + "[FGEN] Processing DMCA request")

    while progress < 100:

        msg = random.choice(messages)

        for s in spinner:

            bar_len = 30
            filled = int(bar_len * progress / 100)
            bar = "█"*filled + "-"*(bar_len-filled)

            sys.stdout.write(
                "\r" +
                Fore.YELLOW +
                f"[FGEN] {msg} {s} " +
                Fore.CYAN +
                f"[{bar}] {progress}%"
            )

            sys.stdout.flush()
            time.sleep(0.15)

        progress += random.randint(3,8)

        if progress > 100:
            progress = 100

    print()
    print()

    print(Fore.GREEN + "DMCA takedown request generated successfully.")
    print(
        Fore.GREEN +
        "The reported biometric dataset and associated model references have been permanently flagged for removal."
    )

# ---------------- MAIN ----------------

def start_dmca():

    clear()
    matrix_rain()
    clear()
    banner()

    print(Fore.YELLOW + "Policy Notice:")
    print("You must provide accurate information.")
    print("False claims may lead to legal consequences.\n")

    accept = input(Fore.GREEN + "Do you accept the policy? (Y/N): ").lower()

    if accept != "y":
        print(Fore.RED + "Policy not accepted.")
        return

    print()
    print(Fore.YELLOW + "1. Myself")
    print(Fore.YELLOW + "2. On behalf of another person")

    who = input(Fore.GREEN + "Select option: ")

    reporter = "Myself" if who=="1" else "On behalf of another person"

    print()
    print(Fore.YELLOW + "Select Body Measurement")
    print("Note: Enter correct body measurements.")
    input(Fore.GREEN + "Press ENTER to continue")

    print()
    print(Fore.YELLOW + "1. Male")
    print(Fore.YELLOW + "2. Female")

    g = input(Fore.GREEN + "Select Gender: ")

    gender = "Male" if g=="1" else "Female"

    data = {}

    data["Height"] = select_option("Height", height)
    data["Weight"] = select_option("Weight", weight)
    data["Shoulder"] = select_option("Shoulder", shoulder)

    if gender == "Male":
        data["Chest"] = select_option("Chest", chest_male)

    data["Waist"] = select_option("Waist", waist)
    data["Hip"] = select_option("Hip", hip)
    data["Thigh"] = select_option("Thigh", thigh)

    if gender == "Female":
        data["Bust"] = select_option("Bust", bust)
        data["Under Bust"] = select_option("Under Bust", underbust)
        data["Cup"] = select_option("Cup Size", cup)

    print()
    confirm = input(Fore.GREEN + "Confirm details? (Y/N): ").lower()

    if confirm != "y":
        print(Fore.RED + "Cancelled.")
        return

    model = input(Fore.GREEN + "Enter FGen Model: ")

    send_dmca_to_server(reporter, gender, model, data)

if __name__ == "__main__":
    start_dmca()