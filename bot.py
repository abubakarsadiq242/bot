from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm NexusAI Bot from Sadiq Digital Nexus Ltd. How can I assist you today?")

app = ApplicationBuilder().token("7260901093:AAE4o9im-P6vW9lr1NbZsHrdPAEMvDdOXoA").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()