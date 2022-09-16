import os
import re
from platform import python_version as kontol
from telethon import events, Button
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/c880f57deef159e1e9b6c.jpg"

@register(pattern=("/donate"))
async def awake(event):
  TEXT = f"ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴛᴏ ɴɪsᴋᴀʟᴀ ʀᴏʙᴏᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ʜᴇʟᴘ sᴜᴘᴘᴏʀᴛ ᴜs sᴏ ᴛʜᴀᴛ ʙᴏᴛs sᴛᴀʏ ᴀᴄᴛɪᴠᴇ ᴀɴᴅ ʜᴇʟᴘ ʏᴏᴜʀ ᴀᴄᴛɪᴠɪᴛɪᴇs ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ 😉"
  BUTTON = [[Button.url("💢 ᴅᴏɴᴀᴛᴇ 💢", "https://t.me/+eOyeaWYq4BUyZjhl")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
