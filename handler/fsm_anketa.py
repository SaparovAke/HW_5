from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboard.client_kb import *



class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(massage: types.Message):
    if massage.chat.type == 'private':
        await FSMAdmin.name.set()
        await massage.answer('как вас зовут?',reply_markup=start_markup)
    else:
        await massage.answer('напишите в личку')


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('сколько вам лет?')


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer("только числа")
    elif not 16 <= int(massage.text) <= 99:
        await massage.answer('вам вход запрещен')
    else:
        async with state.proxy() as date:
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('ваш пол?',reply_markup=gender_murkup)


async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('вы откуда?')


async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('нужно ваша фото',reply_markup=cancel_markup)


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)
    async with state.proxy() as date:
        date['photo'] = massage.photo[0].file_id

        await massage.answer_photo(date["photo"],
                                   caption=f'{date["name"]} {date["age"]}'
                                           f'{date["gender"]} @{date["username"]}')
    await FSMAdmin.next()
    await massage.answer('всё верно?',reply_markup=submit_markup)


async def submit(massage: types.Message, state: FSMContext):
    if massage.text.lower() == 'да':
        await massage.answer('данные сохранены под кэшом',reply_markup=start_markup)
        await state.finish()
    elif massage.text == 'начать заново':
        await massage.answer('как вас зовут?')
        await FSMAdmin.name.set()
    else:
        await massage.answer('не верно')


async def cancel_reg(massage: types.Message, state: FSMContext):
    currents_state = await state.get_state()
    if currents_state is not None:
        await state.finish()
        await massage.answer('всё сброшено')


def reg_hand_anceta(db: Dispatcher):

    db.register_message_handler(cancel_reg,Text(equals='cancel',ignore_case=True),state='*')

    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_age, state=FSMAdmin.age)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
    db.register_message_handler(load_region, state=FSMAdmin.region)
    db.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    db.register_message_handler(submit, state=FSMAdmin.submit)