from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ParseMode

import platform

TOKEN = "PUT_YOUR_TOKEN_HERE"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}!\n\n"
                         f"Info about machine that bot stay\n"
                         f"machine: <i><b>{platform.machine()}</b></i>\n"
                         f"version: <i><b>{platform.version()}</b></i>\n"
                         f"platform: <i><b>{platform.platform()}</b></i>\n"
                         f"uname: <i><b>{platform.uname()}</b></i>\n"
                         f"system: <i><b>{platform.system()}</b></i>\n"
                         f"processor: <i><b>{platform.processor()}</b></i>")


def done():
    print("Bot was started!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=done())
