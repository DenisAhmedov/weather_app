from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Узнать погоду')]],
    resize_keyboard=True,
    input_field_placeholder='Укажите город'
)