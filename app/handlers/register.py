from aiogram import F
from aiogram.fsm.context import FSMContext
from app.buttons.reply import main_menu, reply_button, get_salat_keyboard, get_fast_food_keyboard, \
    get_issiqtaom_keyboard
from app.dispatcher import dp
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from app.states import RegisterState, SalatState, FastfoodState, IssiqtaomState
from db import get_user, save_user
load_dotenv()
@dp.message(CommandStart())
async def command_start_handler(message: Message , state: FSMContext) -> None:
    await message.answer("Assalomu alekum hus kelibsiz 👋🥰 !")
    tg_id = message.from_user.id
    markup = main_menu()
    data = get_user(tg_id)
    if data:
        await message.answer("Siz oldin royhatdan otgansiz❗️ " , reply_markup= markup)
        await message.answer(" Asosiy menudasiz " , reply_markup=main_menu())
    else:
        await message.answer("Ismingizni kiriting ?")
        await state.set_state(RegisterState.name)

@dp.message(RegisterState.name)
async def register_handler(message: Message , state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(" yoshingizni  kiriting ? ")
    await state.set_state(RegisterState.age)

@dp.message(RegisterState.age)
async def register_handler(message: Message , state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    tg_id = message.from_user.id
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    markup = main_menu()
    save_user(tg_id=tg_id ,name=name , age=age)
    await message.answer(" Sizning malumotlaringiz muoffiqiyatli saqland ✅ " , reply_markup= markup)
    await  state.clear()

@dp.message(F.text == "Restoran menusi 🍽")
async def restore_menusi(message: Message):
    markub = reply_button()
    await message.answer("Qiuydagi taomlardan  birini tanglang 👇" , reply_markup=markub)

@dp.message(F.text == "Salatlar 🥗")
async def order(message: Message, state: FSMContext):
    await message.answer("Slatlardan birini  tangalang 👇:", reply_markup=get_salat_keyboard())
    await state.set_state(SalatState.salat_name)
    await state.clear()

@dp.message(F.text == "Orqaga qaytish 🔙")
async def order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("📋Bosh  Menudasiz ", reply_markup=main_menu())

@dp.message(F.text == "Fast food 🌭")
async def order(message: Message, state: FSMContext):
    await message.answer("Fast Food  birini tanglanag 👇 " , reply_markup=get_fast_food_keyboard())
    fast_food = message.text
    await state.update_data(fast_food=fast_food)
    await state.set_state(FastfoodState.fast_food_name)
    await state.clear()

@dp.message(F.text == "️️Issiq taomllar 🍲")
async def order(message: Message, state: FSMContext):
    await message.answer("Quyadagi issiq taomlardan birni tanglanag👇 " , reply_markup=get_issiqtaom_keyboard())
    issiq = message.text
    await state.update_data(issiq=issiq)
    await state.set_state(IssiqtaomState.issiqtaom_name)
    await state.clear()

@dp.message(F.text == "Orqaga qaytish 🔙")
async def back(message: Message , state: FSMContext):
    await state.clear()
    await message.answer("📋Bosh  Menudasiz ", reply_markup=main_menu())
