from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboard.client_kb import start_markup


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    region = State()
    gender = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Как вас зовут?', reply_markup=start_markup)
    else:
        await message.answer('???')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as date:  # для хранение данных
        date['id'] = message.from_user.id
        date['username'] = message.from_user.username
        date['name'] = message.text
        print(date)
    await FSMAdmin.region.set()  # переключатель состояние (.state)
    await message.answer('Откуда вы?')


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['region'] = message.text
        print(date)
    await FSMAdmin.next()
    await message.answer('Ваш пол?')


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['gender'] = message.text
        print(date)
    await FSMAdmin.next()


def reg_hand_anceta(db: Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_region, state=FSMAdmin.region)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
