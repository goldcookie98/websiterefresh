# Website Auto-Refresher

Automatically refreshes a website on a set interval, detects page changes, and sends screenshots to Discord.

## Features

- Refreshes any website on a custom interval
- Detects page changes by comparing page content
- Sends a screenshot and notification to Discord when a change is detected
- Auto-installs required dependencies on first run

## Requirements

- Python 3.7+
- Windows

## Usage

```
python refresh_website.py
```

On first run you will be asked for:

| Prompt | Description |
|---|---|
| URL to monitor | The website URL to refresh and watch |
| Refresh interval | How often to refresh, in minutes (decimals allowed, e.g. `0.5`) |
| Discord webhook URL | Where to send change alerts (leave blank to disable) |

## Discord Setup

1. Open your Discord server settings
2. Go to **Integrations → Webhooks → New Webhook**
3. Copy the webhook URL and paste it when prompted

## How Change Detection Works

Each cycle the script fetches the page HTML and hashes it. If the hash differs from the previous check, a change has been detected. A screenshot of your screen is then taken and sent to Discord along with a timestamped message.

## Dependencies

Installed automatically on first run:

- `requests`
- `Pillow`
- `pyautogui`
