import time
import webbrowser
import subprocess
import sys

def get_input():
    url = input("Enter the URL to refresh: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    while True:
        try:
            interval = float(input("How often to refresh (in minutes): "))
            if interval <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    return url, interval

def refresh_browser(url):
    # Use PowerShell to send F5 to the frontmost window
    script = """
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.SendKeys]::SendWait("{F5}")
    """
    subprocess.run(["powershell", "-Command", script], capture_output=True)

def main():
    print("=== Website Auto-Refresher ===\n")
    url, interval_minutes = get_input()
    interval_seconds = interval_minutes * 60

    print(f"\nOpening {url}")
    print(f"Refreshing every {interval_minutes} minute(s). Press Ctrl+C to stop.\n")

    webbrowser.open(url)
    time.sleep(3)  # Give browser time to open

    try:
        while True:
            print(f"Next refresh in {interval_minutes} minute(s)... (Ctrl+C to stop)")
            time.sleep(interval_seconds)
            print(f"Refreshing {url}...")
            refresh_browser(url)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
