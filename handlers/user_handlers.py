from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

import os

from database.db import FSMFillForm, user_dict
from lexicon.lexicon_ru import LEXICON
from services.percent import fat_percentage, join
from keyboards.menu_kb import create_menu_keyboard
from keyboards.gender_kb import create_gender_keyboard
from keyboards.training_kb import (create_base_training_kb,
                                   create_workout_select_kb,
                                   create_back_to_workout_select_kb,
                                   create_beginner_training_kb)
from keyboards.sport_food_kb import (create_sport_food_select_kb,
                                     create_weight_gain_kb,
                                     create_weight_loss_kb,
                                     create_back_to_sport_food_select_kb)
from filters.filters import IsNormalBelly, IsNormalWeight

router = Router()
all_media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')


# --------------------------------
# Раздел команд
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_menu_keyboard()
    )


@router.message(Command(commands='cancel'),
                StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text=LEXICON['cancel_default'])


@router.message(Command(commands='cancel'),
                ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['cancel'])
    await state.clear()


@router.message(Command(commands='showpercent'))
async def process_showpercent_comman(message: Message):
    if message.from_user.id in user_dict:
        fat = fat_percentage(user_dict[message.from_user.id]['gender'],
                             user_dict[message.from_user.id]['belly_girth'],
                            #  user_dict[message.from_user.id]['high'],
                             user_dict[message.from_user.id]['weight'])
        photo = FSInputFile(path=os.path.join('media', 'results.jpg'))
        await message.answer_photo(photo=photo)
        await message.answer(
            text=("".join([LEXICON['result'], fat + "%"]))
        )
    else:
        await message.answer(
            text=LEXICON['no_data']
        )


# ----------------------------
# Раздел %ЖМТ
# РАЗДЕЛИТЬ НА 2 ФУНКЦИИ и КЛАВИАТУРЫ!!!!!!!!!!!
@router.callback_query(F.data == 'fat_percentage_button')
async def process_fat_percentage_test_command(callback: CallbackQuery,
                                              state: FSMContext):
    await callback.message.edit_text(text=LEXICON['start_fat_test'],
                         reply_markup=create_gender_keyboard())
    await state.set_state(FSMFillForm.fill_gender)


@router.callback_query(StateFilter(FSMFillForm.fill_gender),
                       F.data.in_(['female', 'male']))
async def process_gender_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['fill_belly_girth']
    )
    await state.set_state(FSMFillForm.fill_belly_girth)


@router.message(StateFilter(FSMFillForm.fill_belly_girth),
                       IsNormalBelly())
async def process_belly_enter(message: Message, state: FSMContext):
    await state.update_data(belly_girth=int(message.text))
    await message.answer(
        text=LEXICON['fill_weight']
    )
    await state.set_state(FSMFillForm.fill_weight)

    # await state.set_state(FSMFillForm.fill_high)


@router.message(StateFilter(FSMFillForm.fill_belly_girth))
async def process_wrong_belly_enter(message: Message):
    await message.answer(
        text=LEXICON['wrong_belly_girth']
    )


# Данные хэндлеры использовались ранее для другой формулы вычисления %ЖМТ!
# @router.message(StateFilter(FSMFillForm.fill_high),
#                        IsNormalHigh())
# async def process_high_enter(message: Message, state: FSMContext):
#     await state.update_data(high=int(message.text))
#     await message.answer(
#         text=LEXICON['fill_weight']
#     )
#     await state.set_state(FSMFillForm.fill_weight)


# @router.message(StateFilter(FSMFillForm.fill_high),
#                        ~IsNormalHigh())
# async def process_wrong_high_enter(message: Message):
#     await message.answer(
#         text=LEXICON['wrong_high']
#     )


@router.message(StateFilter(FSMFillForm.fill_weight),
                       IsNormalWeight())
async def process_weight_enter(message: Message,
                                state: FSMContext):
    await state.update_data(weight=int(message.text))
    user_dict[message.from_user.id] = await state.get_data()
    fat = fat_percentage(user_dict[message.from_user.id]['gender'],
                         user_dict[message.from_user.id]['belly_girth'],
                        #  user_dict[message.from_user.id]['high'],
                         user_dict[message.from_user.id]['weight'])
    photo = FSInputFile(path=os.path.join('media', 'results.jpg'))
    await message.answer_photo(photo=photo)
    await message.answer(
        text=(join(LEXICON['result'], fat, "%")),
        reply_markup=create_menu_keyboard()
    )
    await state.clear()


@router.message(StateFilter(FSMFillForm.fill_weight),
                ~IsNormalWeight())
async def process_wrong_weight_enter(message: Message):
    await message.answer(
        text=LEXICON['wrong_weight']
    )


@router.message(~StateFilter(default_state))
async def process_wrong_message(message: Message):
    await message.answer(
        text=LEXICON['wrong_message']
    )


#  --------------------------------
# Раздел тренировок
@router.callback_query(F.data.in_(['training_button', 'back_to_workout_select']))
async def process_create_training_keyboard(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['workout_select_keyboard'],
                         reply_markup=create_workout_select_kb())


@router.callback_query(F.data.in_(['male', 'female']))
async def process_create_base_workout_kb(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON[join(str(callback.data), '_base_workout_keyboard')],
                         reply_markup=create_base_training_kb(callback))


@router.callback_query(F.data.in_(['male_day_1_base_training', 'male_day_2_base_training', 'male__day_3_base_training',
                                   'female_day_1_base_training', 'female_day_2_base_training', 'female_day_3_base_training']))
async def process_send_base_workout(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON[callback.data],
                                     reply_markup=create_back_to_workout_select_kb())


@router.callback_query(F.data == 'beginner_training')
async def process_create_beginner_workout_kb(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['beginner_training_keyboard'],
                         reply_markup=create_beginner_training_kb())


@router.callback_query(F.data.in_(['day_1_beginner_training', 'day_2_beginner_training']))
async def process_send_beginner_workou(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON[callback.data],
                                     reply_markup=create_back_to_workout_select_kb())


@router.callback_query(F.data == 'back_to_menu')
async def process_back_to_menu_kb(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['start_fat_test'],
                         reply_markup=create_menu_keyboard())


# ---------------------------------------
# Раздел спортивного питания
@router.callback_query(F.data.in_(['sports_food_button', 'back_to_sport_food_select']))
async def process_create_sport_food_keyboard(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['sport_food_select_keyboard'],
                         reply_markup=create_sport_food_select_kb())


@router.callback_query(F.data == 'weight_gain')
async def process_create_weight_gain_kb(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['weight_gain_keyboard'],
                         reply_markup=create_weight_gain_kb(callback))


@router.callback_query(F.data == 'weight_loss')
async def process_create_weight_loss_kb(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['weight_loss_keyboard'],
                         reply_markup=create_weight_loss_kb(callback))


@router.callback_query(F.data.in_(['weight_gain_day_1_sport_pit', 'weight_gain_day_2_sport_pit', 'weight_gain_day_3_sport_pit',
                                   'weight_loss_day_1_sport_pit', 'weight_loss_day_2_sport_pit', 'weight_loss_day_3_sport_pit']))
async def process_send_base_workout(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON[callback.data],
                                     reply_markup=create_back_to_sport_food_select_kb())
