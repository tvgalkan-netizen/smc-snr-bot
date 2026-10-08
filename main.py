import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN tapylmady. .env faýlyna token goý.")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salam! 👋\n\n"
        "Men SMC + Support/Resistance signal boty.\n\n"
        "Signal almak üçin /signal ýaz."
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 ANALIZ\n\n"
        "Asset: EUR/USD OTC\n"
        "Timeframe: 1M\n\n"
        "SMC: Häzirlikçe data ýok\n"
        "S/R: Häzirlikçe data ýok\n\n"
        "⏳ Real-time grafik maglumat çeşmesi birikdirilmegine garaşylýar."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Boty başlat\n"
        "/signal - Signal soramak\n"
        "/help - Kömek"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot işledi...")
    app.run_polling()


if __name__ == "__main__":
    main()
