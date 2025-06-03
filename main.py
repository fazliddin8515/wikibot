import asyncio
import wikipedia
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
wikipedia.set_lang("uz")

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()


def bootstrap():
    print("bot has been started....")


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Welcome to the bot.")


@dp.message(Command("wiki"))
async def wiki_handler(message: Message):
    title = message.text[6:]
    summary = wikipedia.summary(title)
    await message.answer(summary)


async def main():
    dp.startup.register(bootstrap)
    await dp.start_polling(bot)


asyncio.run(main())
