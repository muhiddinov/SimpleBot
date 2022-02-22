from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboardMurkup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Namoz vaqtlari'))
    await message.answer(f"Assalomu alaykum, <b><i>{message.from_user.full_name}</i></b>!", reply_markup=keyboardMurkup)