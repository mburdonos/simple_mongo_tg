import asyncio
import logging
from json import dumps

from aiogram import Bot, Dispatcher, types, F

from core.config import settings
from utils.validate import validate_input_data
from utils.format_data import create_structure
from db.mongo_db import MongoDb


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.telegram_bot.token)
dp = Dispatcher()
mongo_db = MongoDb(host=settings.mongo.host, port=int(settings.mongo.port))
mongo_db.connection_db()

@dp.message(F.text)
async def cmd_start(message: types.Message):
    # провекрка входящих значений
    validated_data = validate_input_data(input_text=message.text)
    if isinstance(validated_data, str):
        await message.answer(validated_data)
    else:
        # если данные корректны, то выполняем запрос к хранилищу
        async for data in mongo_db.get_aggreate_data(input_data=validated_data):
            data_for_send = create_structure(data)
            await message.answer(dumps(data_for_send))
async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.info(f'start project: {settings.project.name}')
    asyncio.run(main())