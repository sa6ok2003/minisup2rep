import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '1879854327:AAFSaMU1r5QMNCX5vn5PRpU1sR59FXCMpKE'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)