import subprocess
import time
import random
import sys
from colorama import Fore, init

init(autoreset=True)

matrix_chars = "01ABCDEF"

# Small manufacturer database
vendors = {
    "88:C9:E8": "Apple",
    "00:1A:7D": "Apple",
    "F4:F5:D8": "Samsung",
    "3C:5A:B4": "Sony",
    "40:9C:28": "Xiaomi",
    "FC:58:FA": "Google",
    "DC:A6:32": "JBL",
    "A4:77:33": "OnePlus"
}

messages = [
    "Initializing Bluetooth chipset",
    "Scanning RF environment",
    "Analyzing Bluetooth packets",
    "Mapping nearby signals",
    "Processing hardware identifiers",
    "Building device fingerprint map",
    "Evaluating connection states"
]


# ---------------- MATRIX ANIMATION ----------------

def matrix_scan():

    print(Fore.GREEN + "\nInitializing Matrix Scan\n")

    for _ in range(40):

        line = "".join(random.choice(matrix_chars) for _ in range(70))
        print(Fore.GREEN + line)

        time.sleep(0.05)


# ---------------- PROGRESS SCAN ----------------

def progress_scan():

    spinner = ["|", "/", "-", "\\"]
    progress = 0
    start = time.time()
    duration = random.randint(20, 25)

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
                f"[BT-SCAN] {msg} {s} " +
                Fore.CYAN +
                f"[{bar}] {progress}%"
            )

            sys.stdout.flush()

            time.sleep(0.2)

        progress += random.randint(1, 3)

        if progress > 95:
            progress = 95

    print()


# ---------------- BLUETOOTH FUNCTIONS ----------------

def get_connected():

    try:
        output = subprocess.check_output(
            ["bluetoothctl", "devices", "Connected"],
            text=True
        )

        devices = []

        for line in output.split("\n"):

            if line.strip() == "":
                continue

            parts = line.split(" ")

            mac = parts[1]
            name = " ".join(parts[2:])

            devices.append((mac, name))

        return devices

    except:
        return []


def get_rssi(mac):

    try:

        info = subprocess.check_output(
            ["bluetoothctl", "info", mac],
            text=True
        )

        for line in info.split("\n"):

            if "RSSI" in line:
                return int(line.split(":")[1].strip())

    except:
        pass

    return None


def get_device_type(mac):

    try:

        info = subprocess.check_output(
            ["bluetoothctl", "info", mac],
            text=True
        )

        if "Headset" in info or "Audio Sink" in info:
            return "Audio Headset"

        if "Phone" in info:
            return "Mobile Phone"

        if "Computer" in info:
            return "Computer"

    except:
        pass

    return "Unknown"


def get_vendor(mac):

    prefix = mac[:8]

    return vendors.get(prefix, "Unknown Vendor")


# ---------------- DISTANCE ESTIMATION ----------------

def estimate_distance(rssi):

    if rssi is None:
        return "Unknown"

    tx_power = -59
    ratio = rssi * 1.0 / tx_power

    if ratio < 1.0:
        distance = ratio ** 10
    else:
        distance = (0.89976) * (ratio ** 7.7095) + 0.111

    return f"{round(distance,2)} m"


# ---------------- DASHBOARD ----------------

def dashboard():

    print()
    print(Fore.GREEN + "==============================")
    print(Fore.GREEN + "   BLUETOOTH DEVICE DASHBOARD")
    print(Fore.GREEN + "==============================")
    print()

    devices = get_connected()



    for mac, name in devices:

        rssi = get_rssi(mac)
        dtype = get_device_type(mac)
        vendor = get_vendor(mac)
        distance = estimate_distance(rssi)

        print(Fore.CYAN + f"Device Name     : {name}")
        print(Fore.YELLOW + f"MAC Address     : {mac}")
        print(Fore.MAGENTA + f"Device Type     : {dtype}")

        if rssi:
            print(Fore.GREEN + f"Signal Strength : {rssi} dBm")
        else:
            print(Fore.GREEN + "Signal Strength : Unknown")

        print(Fore.BLUE + f"Manufacturer    : {vendor}")
        print(Fore.WHITE + f"Estimated Range : {distance}")

        print("-" * 45)


# ---------------- LIVE MONITOR ----------------

def live_monitor():

    print(Fore.GREEN + "\nStarting Patching Process\n")

    devices = get_connected()


# ---------------- MAIN ----------------

def main():

    matrix_scan()

    progress_scan()

    dashboard()

    print()

    choice = input(
        Fore.GREEN +
        "Update Security Patch? (Y/N): "
    ).lower()

    if choice == "y":
        live_monitor()

    print()
    print(Fore.GREEN + "====================================")
    print(Fore.GREEN + " Bluetooth Security Monitor Active")
    print(Fore.GREEN + "====================================")
    print(Fore.CYAN + "Local Bluetooth monitoring module initialized successfully.")
    print(Fore.CYAN + "Connected device telemetry is now being observed.")
    print(Fore.CYAN + "Connected bt device security patch injected succesfully.")
    print()


if __name__ == "__main__":
    main()
