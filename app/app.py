from app.bot import Bot
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.strings import s
from app.secrets import TOKEN, ADMIN_ID
from functools import wraps
import aiohttp


bot = Bot(TOKEN)


@bot.command
async def start(u: Update, c: ContextTypes.DEFAULT_TYPE):
    u.effective_message.reply_text(s["hello"])


@bot.admin_command
async def get_meeting_info(u: Update, c: ContextTypes.DEFAULT_TYPE):
    async with aiohttp.ClientSession() as s:
        async with s.get("https://meet.pcworms.ir/data.json") as res:
            data = await res.json()
            caption = s["announcement"]
            caption: str
            await c.bot.send_photo(
                chat_id=u.effective_chat.id,
                photo="https://meet.pcworms.ir/preview.png",
                caption=caption.format_map(data),
            )
