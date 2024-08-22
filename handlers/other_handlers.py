from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON

router = Router()


@router.message()
async def send_echo(message: Message):
    await message.answer(LEXICON['default'])
