from aiogram import types


async def help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/add_bot - Добавить бота",
            "/stop_bot -  Остановить бота")

    await message.answer("\n".join(text))