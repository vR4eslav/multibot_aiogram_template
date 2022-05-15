from aiogram import Router, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

form_router = Router()
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bots_list = []