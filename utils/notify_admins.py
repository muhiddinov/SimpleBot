import logging
import requests
from aiogram import Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config.settings import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)
