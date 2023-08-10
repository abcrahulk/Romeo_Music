from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔥ᴏᴡɴᴇʀ🔥", url=f"https://t.me/itz_Lucky_Raja"),
            InlineKeyboardButton(
                text="🥰ᴄᴏ ᴏᴡɴᴇʀ🥰", url=f"https://t.me/Shivans_Raj_BrockenHart"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ᴄʜᴜᴛɪʏᴀ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔥ᴏᴡɴᴇʀ🔥", url=f"https://t.me/itz_Lucky_Raja"),
            InlineKeyboardButton(
                text="🥰ᴄᴏ ᴏᴡɴᴇʀ🥰", url=f"https://t.me/Shivans_Raj_BrockenHart"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥵 ᴍᴏʀᴇ 🥵", url=f"https://t.me/ZiddiXBot"
                ),
        ],
        [
            InlineKeyboardButton(
                    text="🥰sᴛᴜᴅʏ ɢʀᴏᴜᴘ🥰"
url=f"https://t.me/+LHcxarl1geQyYWM1"
                ),
           
        ],
     ]
    return buttons
