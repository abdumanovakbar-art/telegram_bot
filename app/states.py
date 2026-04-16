from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    name = State()
    age = State()


class SalatState(StatesGroup):
    salat_name = State()

class FastfoodState(StatesGroup):
    fast_food_name = State()


class IssiqtaomState(StatesGroup):
    issiqtaom_name = State()

