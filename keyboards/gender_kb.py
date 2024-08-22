from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON


def create_gender_keyboard() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['male_button'],
            callback_data='male_button'
        ),
        InlineKeyboardButton(
            text=LEXICON['female_button'],
            callback_data='female_button'
        ),
        width=1,
    )
    return kb_builder.as_markup()
