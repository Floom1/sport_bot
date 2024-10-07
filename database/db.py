from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis

redis = Redis(host='localhost')

storage = RedisStorage(redis=redis)

user_dict: dict[int, dict[str, int, int, int]] = {}

class FSMFillForm(StatesGroup):
    fill_gender = State()
    fill_belly_girth = State()
    # fill_high = State()
    fill_weight = State()