from loader import dp
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config.variables import viloyatlar
import requests

@dp.message_handler(text=["Namoz vaqtlari"], state=None)
async def chooseRegion(message: Message):
    keyboardMarkup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    for x in viloyatlar:
        keyboardMarkup.insert(KeyboardButton(x))
    await message.answer("✅ Viloyatingizni tanlang: ", reply_markup=keyboardMarkup)

@dp.message_handler(text=[x for x in viloyatlar], state=None)
async def prayerTime (message: Message):
    #if message.text in viloyatlar:
    resp = requests.get(url='https://api.pray.zone/v2/times/today.json?city=' + viloyatlar[message.text]).json()
    prayer_time = resp['results']['datetime'][0]['times']
    prayer_location = resp['results']['location']
    await message.answer(f"<i><b>{prayer_location['city']}</b></i>" + '\n' + '\n'.join(x + ' - ' + prayer_time[x] for x in prayer_time))