from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.fsm import CityState
from bot.keyboards import keyboard
from bot.utils import get_weather_data

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Введите наименование города', reply_markup=keyboard)


@router.message(F.text == 'Узнать погоду')
async def get_weather(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(f'Не указан город!', reply_markup=keyboard)
        return
    state_data = await state.get_data()
    city_name = state_data['city']
    weather_data = await get_weather_data(city_name)
    if weather_data.get('error'):
        answer_text = weather_data['error']
    else:
        answer_text = (
            f'Погода в г. <b>{city_name}</b>\n'
            '=========================\n'
            f'<b>Температура:</b> {weather_data["temperature"]} °C\n'
            f'<b>Скорость ветра:</b> {weather_data["wind_speed"]} м.с\n'
            f'<b>Атмосферное давление:</b> {weather_data["pressure"]} мм рт.ст.'
        )
    await message.answer(answer_text, reply_markup=keyboard)


@router.message()
async def get_city(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await state.set_state(CityState.set_city)
        await state.set_data(data={'city': message.text})
    else:
        await state.update_data(city=message.text)
    await message.answer(f'Текущим городом установлен - <b>г. {message.text}</b>', reply_markup=keyboard)
