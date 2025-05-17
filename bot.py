from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime



EVENTS = [
    {"title": "Gucci Cruise 2026", "date": "15 мая 2025", "location": "Palazzo Settimanni"},
    {"title": "Pitti Uomo 106", "date": "18-21 июня", "location": "Fortezza da Basso"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, я бот афиши Флоренции 🇮🇹\nНапиши /events, чтобы узнать ближайшие события!"
    )

async def events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.date.today()
    message = "🎭 Актуальные события во Флоренции:\n\n"
    for event in EVENTS:
        message += f"📌 {event['title']}\n📅 {event['date']}\n📍 {event['location']}\n\n"
    await update.message.reply_text(message)


if __name__ == "__main__":
    import os
    TOKEN = os.environ["BOT_TOKEN"]

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("events", events))

    app.run_polling()