from aiogram.fsm.state import StatesGroup, State


class CityState(StatesGroup):
    set_city = State()
