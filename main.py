import os
import re
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

CA = "49AAh2Vh8YdD9EpimegnnXt1ACyHySotRs5Yr5GZ8Xmc"

async def reply_ca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and re.fullmatch(r"\s*ca\s*", update.message.text or "", re.I):
        await update.message.reply_text(CA)

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_ca))
app.run_polling()