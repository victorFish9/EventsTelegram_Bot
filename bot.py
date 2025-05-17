from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.firenzetoday.it/eventi/"

def parse_events():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    events = []

    cards = soup.select("div.teaser__text")[:5]  # Первые 5 событий
    for card in cards:
        title = card.select_one("h3 a")
        date = card.select_one("p.teaser__date")
        location = card.select_one("p.teaser__place")

        events.append({
            "title": title.get_text(strip=True) if title else "Без названия",
            "date": date.get_text(strip=True) if date else "Дата не указана",
            "location": location.get_text(strip=True) if location else "Локация не указана"
        })
    return events

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, я бот афиши Флоренции 🇮🇹\nНапиши /events, чтобы узнать ближайшие события!"
    )

async def events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    parsed_events = parse_events()
    message = "🎭 Актуальные события во Флоренции:\n\n"
    for event in parsed_events:
        message += f"📌 {event['title']}\n📅 {event['date']}\n📍 {event['location']}\n\n"
    await update.message.reply_text(message)

if __name__ == "__main__":
    TOKEN = os.environ["BOT_TOKEN"]

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("events", events))

    app.run_polling()
