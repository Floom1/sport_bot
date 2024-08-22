from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext

import os

from database.db import FSMFillForm
from lexicon.lexicon_ru import LEXICON
from services.percent import fat_percentage
from keyboards.menu_kb import create_menu_keyboard
from keyboards.gender_kb import create_gender_keyboard

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    # photo = FSInputFile(path=os.path.join('media', 'goyda.jpg'))
    # await message.answer_photo(photo=photo)
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

#РАЗДЕЛИТЬ НА 2 ФУНКЦИИ и КЛАВИАТУРЫ!!!!!!!!!!!
@router.callback_query(F.data == 'fat_percentage_button')
async def process_fat_percentage_test_command(callback: CallbackQuery,
                                              state: FSMContext):
    await callback.message.edit_text(text=LEXICON['start_fat_test'],
                         reply_markup=create_gender_keyboard())
    await state.set_state(FSMFillForm.fill_gender)


@router.callback_query(StateFilter(FSMFillForm.fill_gender),
                       F.data.in_(['female_button', 'male_button']))
async def process_gender_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['fill_belly_girth']
    )
    await state.set_state(FSMFillForm.fill_belly_girth)
