from aiogram import types
from aiogram.dispatcher.filters import CommandObject

from polling_manager import PollingManager
from aiogram.utils.markdown import html_decoration as fmt


async def stop_bot(
        message: types.Message, command: CommandObject, polling_manager: PollingManager
):
    if command.args:
        try:
            polling_manager.stop_bot_polling(int(command.args))
            await message.answer("Bot stopped")
        except (ValueError, KeyError) as err:
            await message.answer(fmt.quote(f"{type(err).__name__}: {str(err)}"))
    else:
        await message.answer("Please provide bot id")
