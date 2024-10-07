from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery


from lexicon.lexicon_ru import LEXICON
from services.percent import join


def create_sport_food_select_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['weight_gane_button'],
            callback_data='weight_gain'
        ),
        InlineKeyboardButton(
            text=LEXICON['weight_loss_button'],
            callback_data='weight_loss'
        )
    )
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['back_to_menu_button'],
            callback_data='back_to_menu'
        )
    )
    return kb_builder.as_markup()


def create_weight_gain_kb(callback: CallbackQuery) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_1_button')],
            callback_data=join(str(callback.data), '_day_1_sport_pit')
        ),
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_2_button')],
            callback_data=join(str(callback.data), '_day_2_sport_pit')
        ),
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_3_button')],
            callback_data=join(str(callback.data), '_day_3_sport_pit')
        ),
        width=1,
    )
    return kb_builder.as_markup()


def create_weight_loss_kb(callback: CallbackQuery) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_1_button')],
            callback_data=join(str(callback.data), '_day_1_sport_pit')
        ),
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_2_button')],
            callback_data=join(str(callback.data), '_day_2_sport_pit')
        ),
        InlineKeyboardButton(
            text=LEXICON[join(str(callback.data), '_day_3_button')],
            callback_data=join(str(callback.data), '_day_3_sport_pit')
        ),
        width=1,
    )
    return kb_builder.as_markup()


def create_back_to_sport_food_select_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['back_to_sport_food_select_button'],
            callback_data='back_to_sport_food_select'
        ),
    )
    return kb_builder.as_markup()