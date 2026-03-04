from aiogram import Bot, Dispatcher
from handlers.admins.base import router


def create_admin_bot(token: str):
    # create bot and dispatcher
    bot = Bot(token=token)
    dp = Dispatcher(bot=bot)

    # include routers
    dp.include_router(router)
    # ====

    return bot, dp