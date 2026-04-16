from aiogram import F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.dispatcher import dp

CHANNEL_LINK = "https://t.me/fxkiller01"
ADMIN_LINK = "https://t.me/Abdumanov_001"
@dp.message(F.text == "Biz bilan boglanish 📱️️️️️️")
async def help_command(message: Message):
    text = (
        "<b>👋 Yordam bo‘limi</b>\n\n"
        "<b>Botdan foydalanish:</b>\n"
        "👤 Nima muammo bor \n"
        "<i>Muammo bo‘lsa admin yoki kanalga yozing👇</i>"
    )
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="👨‍💻 Adminga yozish",
            url=ADMIN_LINK
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="📢 Kanalimiz",
            url=CHANNEL_LINK
        )
    )
    await message.answer(text, reply_markup=builder.as_markup(), parse_mode="HTML")