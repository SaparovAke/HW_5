from aiogram import Dispatcher, types
from config import bot
from .extra import users


async def ban(message: types.Message):
    if message.chat.type != 'private':
        massage = message.text.split()
        username = massage[1]
        await bot.kick_chat_member(message.chat.id, user_id=users[f'{username}'])
        await message.answer('Он вышел сам!')


def reg_ban(db: Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix=['!'])
