import os
from database.database import Database
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv(find_dotenv(r'config\.env'))

bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database(r'database\database.db')