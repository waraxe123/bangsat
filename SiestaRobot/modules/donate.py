import os
import re
from platform import python_version as kontol
from telethon import events, Button
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/c97b7e4f0af6394db940b.jpg"

@register(pattern=("/donate"))
async def awake(event):
  TEXT = f"**Donate For Hito Robot 🥰**"
  BUTTON = [[Button.url("✨ Here ✨", "https://t.me/+eOyeaWYq4BUyZjhl")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
