from aiogram import Bot, Dispatcher
from handlers.users.base import router


def create_user_bot(token: str):
    # create bot and dispatcker
    # os.getenv(str) - get values from .env file on a name
    bot = Bot(token)
    dp = Dispatcher(bot=bot)

    # include routers
    dp.include_router(router)


    return bot, dp



