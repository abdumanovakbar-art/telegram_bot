from aiogram import F
from aiogram.types import KeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.dispatcher import dp


def main_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Restoran menusi 🍽"),
        KeyboardButton(text="Biz bilan boglanish 📱️️️️️️"),
    )
    rkb.adjust(1 , repeat=True)
    return rkb.as_markup(resize_keyboard=True)

def reply_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Salatlar 🥗"),
        KeyboardButton(text="Fast food 🌭"),
        KeyboardButton(text="Issiq taomllar 🍲"),
        KeyboardButton(text="Orqaga qaytish 🔙"),
    )
    rkb.adjust(2 , repeat=True)
    return rkb.as_markup(resize_keyboard=True)

#
# def get_salat_keyboard():
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(
#         KeyboardButton(text="Oliviya🥗"),
#         KeyboardButton(text="Sezer🥗"),
#         KeyboardButton(text="Orqaga qaytish 🔙")
#     )
#     rkb.adjust(1)
#     return rkb.as_markup(resize_keyboard=True)


@dp.message(F.text == "Oliviya🥗")
async def oliviya_handler(message: Message):
    text = (
        "🥗 Oliviya salati\n\n"
        "Tarkibi: kartoshka, sabzi, tuxum, mayonez\n"
        "Narxi: 25 000 so'm"
    )
    await message.answer_photo(
        "https://link-to-image.jpg",
        caption=text
    )


@dp.message(F.text == "Sezer🥗")
async def sezer_handler(message: Message):
    text = (
        "🥗 Sezer salati\n\n"
        "Tarkibi: salat bargi, tovuq, pishloq, sous\n"
        "Narxi: 30 000 so'm"
    )
    await message.answer_photo(
        "https://www.bakenroll.az/en/image/caesar-chicken-7-wolt-1x1.jpg",
        caption=text
    )


def get_salat_keyboard():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Oliviya🥗"),
        KeyboardButton(text="Sezer🥗"),
        KeyboardButton(text="Orqaga qaytish 🔙")
    )
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)

def get_fast_food_keyboard():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Burger🍔"),
        KeyboardButton(text="Hot-dog🌭️️"),
        KeyboardButton(text="Orqaga qaytish 🔙")
    )
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)


def get_issiqtaom_keyboard():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Osh🍛"),
        KeyboardButton(text="sho'rva🍲️️️️️️"),
        KeyboardButton(text="Orqaga qaytish 🔙")
    )
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)