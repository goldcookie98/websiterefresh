# Website Auto-Refresher

Automatically refreshes a website on a set interval, detects page changes, and sends screenshots to Discord.

---

## Installation

1. Make sure you have **Python 3.7 or newer** installed on your PC
2. If you do not have Python, download it from [python.org](https://www.python.org/downloads/)
3. During the Python install, check the box that says **"Add Python to PATH"**
4. Download or clone this repository to your computer
5. Open the folder where `refresh_website.py` is saved
6. You do not need to install any packages manually — the script does it for you on first run

---

## Running the Script

1. Open **Command Prompt** or **PowerShell** on your PC
2. Navigate to the folder where the script is saved — for example:
   ```
   cd C:\Users\YourName\Downloads\websiterefresh
   ```
3. Run the script with:
   ```
   python refresh_website.py
   ```
4. The first time it runs, it will automatically install the required packages (`requests`, `Pillow`, `pyautogui`)
5. Wait for the packages to finish installing — this only happens once
6. The setup prompts will appear — follow the steps below

---

## Setup Prompts

1. **URL to monitor** — type the full website address you want to watch, for example:
   ```
   https://www.example.com
   ```
2. If you forget `https://` the script will add it for you automatically
3. Press **Enter** after typing the URL
4. **Refresh interval** — type how often you want the page to refresh, in minutes
5. You can use decimals — for example, type `0.5` for every 30 seconds or `2.5` for every 2.5 minutes
6. Press **Enter** after typing the interval
7. **Discord webhook URL** — paste your Discord webhook URL here (see Discord Setup below)
8. If you do not want Discord notifications, just press **Enter** to skip
9. The script will open the website in your default browser automatically
10. The script will begin monitoring — you will see status updates in the terminal

---

## Discord Setup

1. Open **Discord** on your PC or in your browser
2. Go to the server where you want to receive notifications
3. Click the **server name** at the top left to open the server menu
4. Click **Server Settings**
5. In the left sidebar, click **Integrations**
6. Click **Webhooks**
7. Click **New Webhook**
8. Give the webhook a name, for example `Page Watcher`
9. Choose which channel you want the alerts to appear in
10. Click **Copy Webhook URL**
11. Go back to the script setup prompt and paste the URL in when asked

---

## How It Works

1. The script opens your chosen URL in your default browser
2. Every time the interval ends, the script sends an F5 keypress to refresh the browser
3. The script also fetches the page content in the background and creates a fingerprint (hash) of it
4. It compares the new fingerprint to the previous one
5. If the fingerprints are different, the page content has changed
6. When a change is detected, the script takes a screenshot of your screen
7. The screenshot and a timestamped message are sent to your Discord channel
8. The script then continues monitoring from that point forward
9. If no change is detected, the script simply waits for the next interval and tries again
10. When you are done, press **Ctrl+C** in the terminal to stop the script
11. A final message will be sent to Discord letting you know monitoring has stopped

---

## Tips

1. Keep the browser window visible on screen for the best screenshots
2. Use a small interval (like `0.5` minutes) if you need near-real-time alerts
3. Use a larger interval (like `10` or `30` minutes) to avoid hammering slower websites
4. The script works best on websites that serve regular HTML — heavily JavaScript-rendered pages may not trigger change detection reliably
5. You can run multiple instances of the script at the same time to monitor more than one URL
6. To monitor a second URL, open a new terminal window and run `python refresh_website.py` again
