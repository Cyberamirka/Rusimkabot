# modules
import asyncio
import os
import sys

import dotenv
import logging

from bot.user_bot import create_user_bot
from bot.admin_bot import create_admin_bot

# project modules
# ...


# logging
# Настройка базового логирования
logger = logging.getLogger("main.py")
logger.setLevel(logging.INFO)

# StreamHandler — вывод в консоль
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# FileHandler — лог в файл
file_handler = logging.FileHandler("logs/main.log", mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





# main function to starting admin and user bots
async def start_bot():
    logger.info('Loading environment variables...')
    dotenv.load_dotenv()
    logger.info("Starting bot...")

    user_bot, user_dispatcher = create_user_bot(os.getenv("USER_BOT_TOKEN"))
    admin_bot, admin_dispatcher = create_admin_bot(os.getenv("ADMIN_BOT_TOKEN"))

    await user_bot.delete_webhook(drop_pending_updates=True)
    await admin_bot.delete_webhook(drop_pending_updates=True)

    logger.info("Bot started")
    await asyncio.gather(
        user_dispatcher.start_polling(user_bot),
        admin_dispatcher.start_polling(admin_bot)
    )



# if run main file then start program
if __name__ == '__main__':
    asyncio.run(start_bot())