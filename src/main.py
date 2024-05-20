import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F

from core.config import settings
from utils.validate import validate_input_data


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.telegram_bot.token)
dp = Dispatcher()

@dp.message(F.text)
async def cmd_start(message: types.Message):
    # провекрка входящих значений
    validated_data = validate_input_data(input_text=message.text)
    if isinstance(validated_data, str):
        await message.answer(validated_data)
    else:
        await message.answer(f'get text')
async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.info(f'start project: {settings.project.name}')
    asyncio.run(main())