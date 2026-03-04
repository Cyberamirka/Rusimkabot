from aiogram import Router, types
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer("Hello World bro, i am just created, this is user bot!")