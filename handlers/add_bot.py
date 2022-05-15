from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import CommandObject
from aiogram.exceptions import TelegramUnauthorizedError
from aiogram.utils.token import TokenValidationError

from app import on_bot_startup, on_bot_shutdown
from polling_manager import PollingManager
from aiogram.utils.markdown import html_decoration as fmt


async def add_bot(
    message: types.Message,
    command: CommandObject,
    dp_for_new_bot: Dispatcher,
    polling_manager: PollingManager,
):
    if command.args:
        try:
            bot = Bot(command.args)

            if bot.id in polling_manager.polling_tasks:
                await message.answer("Bot with this id already running")
                return

            # also propagate dp and polling manager to new bot to allow new bot add bots
            polling_manager.start_bot_polling(
                dp=dp_for_new_bot,
                bot=bot,
                on_bot_startup=on_bot_startup(bot),
                on_bot_shutdown=on_bot_shutdown(bot),
                polling_manager=polling_manager,
                dp_for_new_bot=dp_for_new_bot,
            )
            bot_user = await bot.get_me()
            await message.answer(f"New bot started: @{bot_user.username}")
        except (TokenValidationError, TelegramUnauthorizedError) as err:
            await message.answer(fmt.quote(f"{type(err).__name__}: {str(err)}"))
    else:
        await message.answer("Please provide token")