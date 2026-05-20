from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("бот работает ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_reply))

print("BOT STARTED")
app.run_polling()
