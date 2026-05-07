import time
import webbrowser
import subprocess
import sys
import io
import hashlib
import requests
from PIL import Image
import pyautogui

REQUIRED = ["requests", "Pillow", "pyautogui"]

def install_deps():
    for pkg in REQUIRED:
        try:
            __import__(pkg.lower().replace("-", "_").replace("pillow", "PIL"))
        except ImportError:
            print(f"Installing {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def get_input():
    print("=== Website Auto-Refresher Setup ===\n")

    url = input("URL to monitor: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    while True:
        try:
            interval = float(input("Refresh interval (minutes): "))
            if interval > 0:
                break
            print("Must be a positive number.")
        except ValueError:
            print("Enter a valid number.")

    webhook = input("Discord webhook URL: ").strip()

    return url, interval, webhook


def hash_page(url):
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        return hashlib.md5(r.text.encode()).hexdigest()
    except Exception as e:
        print(f"  Warning: could not fetch page content ({e})")
        return None


def take_screenshot():
    return pyautogui.screenshot()


def send_discord(webhook, message, screenshot=None):
    if not webhook:
        return
    try:
        if screenshot:
            buf = io.BytesIO()
            screenshot.save(buf, format="PNG")
            buf.seek(0)
            requests.post(
                webhook,
                data={"content": message},
                files={"file": ("change.png", buf, "image/png")},
                timeout=10,
            )
        else:
            requests.post(webhook, json={"content": message}, timeout=10)
    except Exception as e:
        print(f"  Discord error: {e}")


def refresh_browser():
    script = (
        'Add-Type -AssemblyName System.Windows.Forms; '
        '[System.Windows.Forms.SendKeys]::SendWait("{F5}")'
    )
    subprocess.run(["powershell", "-Command", script], capture_output=True)


def main():
    install_deps()
    url, interval_minutes, webhook = get_input()
    interval_seconds = interval_minutes * 60

    print(f"\nOpening {url}")
    print(f"Checking for changes every {interval_minutes} minute(s).")
    print("Discord notifications: " + ("enabled" if webhook else "disabled"))
    print("Press Ctrl+C to stop.\n")

    webbrowser.open(url)
    time.sleep(4)

    prev_hash = hash_page(url)
    send_discord(webhook, f"Monitoring started for: {url}")

    try:
        while True:
            print(f"[{time.strftime('%H:%M:%S')}] Waiting {interval_minutes}m before next check...")
            time.sleep(interval_seconds)

            print(f"[{time.strftime('%H:%M:%S')}] Refreshing...")
            refresh_browser()
            time.sleep(3)

            current_hash = hash_page(url)

            if current_hash and prev_hash and current_hash != prev_hash:
                print("  >> Page change detected!")
                screenshot = take_screenshot()
                send_discord(
                    webhook,
                    f"**Page changed!** {url}\n`{time.strftime('%Y-%m-%d %H:%M:%S')}`",
                    screenshot,
                )
                prev_hash = current_hash
            elif current_hash:
                print("  No change detected.")
                if current_hash != prev_hash:
                    prev_hash = current_hash

    except KeyboardInterrupt:
        print("\nStopped.")
        send_discord(webhook, f"Monitoring stopped for: {url}")


if __name__ == "__main__":
    main()
