from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery


from lexicon.lexicon_ru import LEXICON
from services.percent import join


def create_workout_select_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['base_male_training_button'],
            callback_data='male'
        ),
        InlineKeyboardButton(
            text=LEXICON['base_female_training_button'],
            callback_data='female'
        )
    )
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['beginner_training_button'],
            callback_data='beginner_training'
        )
    )
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['back_to_menu_button'],
            callback_data='back_to_menu'
        )
    )
    return kb_builder.as_markup()


def create_base_training_kb(callback: CallbackQuery) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_1_base_training_button')],
            callback_data=join(str(callback.data), '_day_1_base_training')
        ),
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_2_base_training_button')],
            callback_data=join(str(callback.data), '_day_2_base_training')
        ),
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_3_base_training_button')],
            callback_data=join(str(callback.data), '_day_3_base_training')
        ),
        width=1,
    )
    return kb_builder.as_markup()


def create_beginner_training_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['day_1_beginner_training_button'],
            callback_data='day_1_beginner_training'
        ),
        InlineKeyboardButton(
            text=LEXICON['day_2_beginner_training_button'],
            callback_data='day_2_beginner_training'
        ),
        width=2
    )
    return kb_builder.as_markup()


def create_back_to_workout_select_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['back_to_workout_select_button'],
            callback_data='back_to_workout_select'
        ),
    )
    return kb_builder.as_markup()
