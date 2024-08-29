from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from aiogram.types import Message


class IsNormalBelly(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.isdigit():
            if int(message.text) <= 170 and int(message.text) >= 50:
                return True
        return False


class IsNormalHigh(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.isdigit():
            if int(message.text) <= 220 and int(message.text) >= 100:
                return True
        return False


class IsNormalWeight(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.isdigit():
            if int(message.text) <= 200 and int(message.text) >= 40:
                return True
        return False
