from aiogram import types


async def start(message: types.Message):
    await message.answer("Hello, I'm a bot.\n")
