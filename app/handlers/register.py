from app.dispatcher import dp
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Assalom")


