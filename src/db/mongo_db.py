from typing import AsyncGenerator

from motor import motor_asyncio as mt


class MongoDb:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = None
        self.batch_size = 1000000

    def get_format_data_group(self, val: str) -> str:
        sample_date = {
            "month": "%Y-%m-00T00:00:00",
            "day": "%Y-%m-%dT00:00:00",
            "hour": "%Y-%m-%dT%H:00:00",
        }
        return sample_date.get(val)

    def connection_db(self):
        self.client = mt.AsyncIOMotorClient(self.host, self.port)

    async def get_aggreate_data(self, input_data: dict) -> AsyncGenerator:
        my_collection = self.client["sampleDB"]["sample_collection"]
        query = [
            {
                "$match": {
                    "dt": {
                        "$gte": input_data.get('dt_from'),
                        "$lt": input_data.get('dt_upto')
                    }
                }
            },
            {
                "$group": {
                    "_id": {
                        "$dateToString": {
                            "date": "$dt", "format": self.get_format_data_group(input_data.get("group_type"))
                        }
                    },
                    "dataset": {"$sum": "$value"}
                }
            }
        ]
        result_data = []
        async for data in my_collection.aggregate(pipeline=query):
            # сделано для того, чтобы при необходимости отправлять данные частями
            if len(result_data) == self.batch_size:
                yield result_data
                result_data = []
            result_data.append(data)
        yield result_data