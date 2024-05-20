import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F

from core.config import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.telegram_bot.token)
dp = Dispatcher()

@dp.message(F.text)
async def cmd_start(message: types.Message):
    await message.answer(f'get text: {message.text}')
async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.info(f'start project: {settings.project.name}')
    asyncio.run(main())