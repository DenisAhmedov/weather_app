from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import TOKEN
from bot.handlers import router

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

