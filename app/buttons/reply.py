from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder



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