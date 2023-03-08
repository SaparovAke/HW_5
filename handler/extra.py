from aiogram import types, Dispatcher
from config import bot

async def python(massage: types.Message):
    if massage.text.lower() == 'python':
        await bot.send_dice(massage.chat.id)


users = {}


async def ban(message: types.Message):
    name = message.from_user.username
    if name:
        name = name
    else:
        name = message.from_user.first_name
    if message.from_user.username is not users:
        users[f'@{name}'] = message.from_user.id
    print(users)

def reg_handler_extra(db: Dispatcher):
    db.register_message_handler(ban)
    db.register_message_handler(python)
