import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message



async def ForceSub(bot: Client, event: Message):
    try:
        await bot.get_chat_member(chat_id=(int(-1001585364777) if -1001585364777.startswith("-100") else -1001585364777), user_id=event.from_user.id)
    except UserNotParticipant:
        try:
           gh = await bot.send_message(chat_id=event.chat.id,text=f"""
<b>Hey </b>{event.from_user.mention} !,
<b>You are Free user so join my creators channel before useing me !Click join now button and join sz channel.</b>
<i>Don't forget to give</i><code>/start</code><i>command again.</i>""",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Now ↗️", url="https://t.me/Buduh")]]),disable_web_page_preview=True)
           await asyncio.sleep(10)
           await gh.delete()
           return 400
        except FloodWait as e:
           await asyncio.sleep(e.x)
           fix_ = await ForceSub(bot, event)
           return fix_
    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}\n\nContact Support Group: https://t.me/NiskalaSupport")
        return 200
