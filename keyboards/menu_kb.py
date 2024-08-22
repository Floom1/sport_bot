from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON


def create_menu_keyboard() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['training_button'],
            callback_data='training_button'
        ),
        InlineKeyboardButton(
            text=LEXICON['sports_food_button'],
            callback_data='sports_food_button'
        ),
        InlineKeyboardButton(
            text=LEXICON['fat_percentage_button'],
            callback_data='fat_percentage_button'
        ),
        width=2
    )
    return kb_builder.as_markup()
