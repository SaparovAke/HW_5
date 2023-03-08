from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    spider = InlineKeyboardButton('next', callback_data='spider')
    markup.add(spider)
    ques = 'Откуда мем?'
    answer = [
        'Бетмэн',
        'Спанч Боб Квадратные штаны',
        'Человек-паук',
        'Халк',
        'Бесстыжие',
        'Неуязвимый',
    ]
    photo = open('media/bat.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='This is Batman, because I am Batman',
        open_period=10,
        reply_markup=markup
    )

async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    monster = InlineKeyboardButton('next', callback_data='monster')
    markup.add(monster)
    ques = 'Откуда мем?'
    answer = [
        'Корпорация монстров',
        'Спанч Боб Квадратные штаны',
        'Человек-паук',
        'Халк',
        'Бесстыжие',
        'Неуязвимый',
    ]
    photo = open('media/spidermem.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation='Это человек паук',
        open_period=10,
        reply_markup=markup
    )

async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    ques = 'Откуда мем?'
    answer = [
        'Спанч Боб Квадратные штаны',
        'Человек-паук',
        'Халк',
        'Корпорация монстров',
        'Бесстыжие',
        'Неуязвимый',
    ]
    photo = open('media/monster.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation='Это Корпорация Монстров',
        open_period=10,
    )

def reg_hand_callback(db: Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')
    db.register_callback_query_handler(quiz3, text='spider')
    db.register_callback_query_handler(quiz4, text='monster')