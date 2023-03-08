from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboard.client_kb import start_markup

async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}',
                           reply_markup=start_markup)
    await message.reply('пока что всё')

async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Кто ты воин?'
    answer = [
        'Бетмэн - Темный рыцарь',
        'Спанч Боб - Квадратные штаны',
        'Томас Шелби - глава Острых козырьков',
        'Ахилес - сын Пелея',
        'Диктор канала "Мастерская настроения"',
        'Оптимус Прайм - Последний Прайм',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation='Ты Ахилес - Сын Пелея',
        open_period=10,
        reply_markup=markup
    )

async def info_hand(message: types.Message):
    await message.answer('новая функция')


def reg_client(db: Dispatcher):
    db.register_message_handler(start_handler, commands=['start', 'salam'])
    db.register_message_handler(quiz1, commands=['quiz'])
    db.register_message_handler(info_hand, commands=['info'])