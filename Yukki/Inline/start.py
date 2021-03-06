from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="π» α΄α΄sΚΚα΄α΄Κα΄", callback_data="Dashboard"),
            InlineKeyboardButton(text="π α΄ α΄Κα΄α΄α΄", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="β α΄α΄α΄Κ α΄sα΄Κs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π‘ sα΄α΄α΄α΄s", callback_data="AQ"
            ),
        ],
        [
            InlineKeyboardButton(text="Close π", callback_data="close"),
        ],
    ]
    return f"β  **Zenzu Musik V2**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Κα΄Ι΄α΄α΄α΄Ι΄", callback_data="shikhar"
                ),
                InlineKeyboardButton (
                    "β α΄α΄Ι΄α΄sΙͺ", url=f"https://t.me/zenzuzu"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β¨α΄Κα΄Ι΄Ι΄α΄Κ", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="β¨Ι’Κα΄α΄α΄", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "β α΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄Κα΄", 
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β¨α΄Κα΄Ι΄Ι΄α΄Κ", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="β¨Ι’Κα΄α΄α΄", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="π» α΄α΄sΚΚα΄α΄Κα΄ ", callback_data="Dashboard"),
            InlineKeyboardButton(text="π Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π?ββοΈ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π₯ Dashboard", callback_data="AQ"
            ),
        ],
        [
            InlineKeyboardButton(text="Close π", callback_data="close"),
        ],
    ]
    return f"β  **Rose Bot VC Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="π Reset Audio Volume", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="β’Low Volβ’", callback_data="LV"),
            InlineKeyboardButton(text="β’Medium Volβ’", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="β’High Volβ’", callback_data="HV"),
            InlineKeyboardButton(text="β’Amplified Volβ’", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="π  Custom Volume π ", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"β  **Rose Bot VC Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="π  Custom Volume π ", callback_data="AV")],
    ]
    return f"β  **Rose Bot VC Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="π₯ Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="π Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="π Authorized Users Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"β  **Rose Bot VC Settings**  ", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="βοΈ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="πΎ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="π» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="π½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"β  **Rose Bot VC Settings** ", buttons
