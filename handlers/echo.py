from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

@dp.message_handler(state=None)
async def bot_start(message: types.Message):
    await message.answer(f"<b><i>{message.text}</i></b>!")

@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Kiritilgan xabar <code>{state}</code>.\n"
                             f"\nXabar matni:\n"
                             f"<code>{message}</code>")