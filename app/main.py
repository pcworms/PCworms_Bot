from app.bot import Bot
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.strings import s
from app.secrets import TOKEN


bot = Bot(TOKEN)


@bot.command
async def start(u: Update, c: ContextTypes.DEFAULT_TYPE):
    u.effective_message.reply_text(s["hello"])
