import asyncio
import logging

from core.config import settings

logging.basicConfig(level=logging.INFO)

if __name__=='__main__':
    print(f'start project: {settings.project.name}')