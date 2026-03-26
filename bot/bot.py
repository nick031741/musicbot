import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

# ✅ ЛОГИ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    logging.info(f"/start от пользователя {message.from_user.id}")

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="🎧 Перейти в плеер",
                    web_app=types.WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "🎵 Добро пожаловать!\n\n"
        "Жми кнопку ниже и слушай музыку 👇",
        reply_markup=keyboard
    )


# 🔥 лог всех сообщений (очень полезно)
@dp.message()
async def log_all(message: types.Message):
    logging.info(f"Сообщение: {message.text}")


async def main():
    logging.info("Бот запущен 🚀")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())