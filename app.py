import asyncio
import logging
from typing import List

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.command import Command, CommandObject, CommandStart
from aiogram.exceptions import TelegramUnauthorizedError
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.utils.token import TokenValidationError

from handlers.add_bot import add_bot
from handlers.echo import echo
from handlers.start import start
from polling_manager import PollingManager

logger = logging.getLogger(__name__)

TOKENS = [
    "2136782573:AAHzjhl3HJhd3t8mPchYYh2-0rhruujSKss",
]
ADMIN_ID = 1970158359


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="add_bot",
            description="add bot, usage '/add_bot 123456789:qwertyuiopasdfgh'",
        ),
        BotCommand(
            command="stop_bot",
            description="stop bot, usage '/stop_bot 123456789'",
        ),
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())


async def on_bot_startup(bot: Bot):
    await set_commands(bot)
    await bot.send_message(chat_id=ADMIN_ID, text="Bot started!")


async def on_bot_shutdown(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text="Bot shutdown!")


async def on_startup(bots: List[Bot]):
    for bot in bots:
        await on_bot_startup(bot)


async def on_shutdown(bots: List[Bot]):
    for bot in bots:
        await on_bot_shutdown(bot)








async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    bots = [Bot(token) for token in TOKENS]
    dp = Dispatcher(isolate_events=True)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.message.register(start, CommandStart())
    dp.message.register(add_bot, Command(commands="add_bot"))
    dp.message.register(stop_bot, Command(commands="stop_bot"))
    dp.message.register(echo)

    polling_manager = PollingManager()

    for bot in bots:
        await bot.get_updates(offset=-1)
    await dp.start_polling(*bots, dp_for_new_bot=dp, polling_manager=polling_manager)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Exit")
