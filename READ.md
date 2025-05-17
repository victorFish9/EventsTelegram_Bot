# FlorenceEventsBot 🇮🇹

FlorenceEventsBot is a simple Telegram bot that helps users stay up-to-date with cultural and fashion events happening in Florence, Italy. The bot sends notifications and reminders about upcoming shows, exhibitions, and local events.

## 💡 Features

- Get alerts about upcoming events in Florence  
- Receive reminders via Telegram  
- Future support for filtering events by category (e.g., fashion, art, music)

## 🚀 Deployment

The bot is deployed as a **Background Worker** on [Render.com](https://render.com), which keeps the bot running 24/7.

### 🔧 Requirements

- Python 3.11+
- `python-telegram-bot==20.7`

### 📦 Installation (Local)

```bash
git clone https://github.com/victorFish9 FlorenceEventsBot.git
cd FlorenceEventsBot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
