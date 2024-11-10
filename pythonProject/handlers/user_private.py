from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f


from filtres.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('начнем',
                         reply_markup=reply.start_kb3.as_markup(
                             resize_keyboard=True,
                         input_field_placeholder="Что вы хотите узнать?"))

@user_private_router.message((F.text.lower().contains('друз')) | (F.lower() == 'список друзей'))
@user_private_router.message(Command('list'))
async def list_cmds(message: types.Message):
    await message.answer('Артём 👽\nАшот 🎮\nВадим 🚬\nДима 🐐\nМатвей 💀\nНикита 🤖\nПаша 🥶\nСтёпа 🚽')

@user_private_router.message(or_f(Command('height'), (F.text.lower() == 'рост'), (F.text.lower().contains('рост'))))
async def menu_cmd(message: types.Message):
    await message.answer("рост...")

@user_private_router.message(F.text.lower() == 'вес')
@user_private_router.message(Command('weight'))
async def weight_cmd(message: types.Message):
    await message.answer("вес....")

@user_private_router.message(or_f(Command('age'), (F.text.lower() == 'кол-во полных лет'), (F.text.lower().contains('лет'))))
async def menu_cmd(message: types.Message):
    await message.answer("ему ..... лет")

@user_private_router.message(or_f(Command('zodiac'), (F.text.lower() == 'знак зодиака'), (F.text.lower().contains('зодиак'))))
async def menu_cmd(message: types.Message):
    await message.answer("его знак зодиака ...")

@user_private_router.message(or_f(Command('data'), (F.text.lower() == 'дата рождения'), (F.text.lower().contains('рожден'))))
async def menu_cmd(message: types.Message):
    await message.answer("дата рождения ...")

@user_private_router.message(or_f(Command('color'), (F.text.lower() == 'любиммый цвет'), (F.text.lower().contains('цвет'))))
async def menu_cmd(message: types.Message):
    await message.answer("его любимый цвет ...")

@user_private_router.message(or_f(Command('anime'), (F.text.lower() == 'любимое аниме'), (F.text.lower().contains('аниме'))))
async def menu_cmd(message: types.Message):
    await message.answer("его любимое аниме...")

@user_private_router.message(or_f(Command('name'), (F.text.lower() == 'полное имя'), (F.text.lower().contains('имя'))))
async def menu_cmd(message: types.Message):
    await message.answer("его полное имя")

@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"Номер получен")
    await message.answer(str(message.contact))

@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"Локация получена")
    await message.answer(str(message.location))




#lower() перводит весь текст в нижний регистр  #contains() убирает лишние слова и оставляет только то, что выделил
#reply_markup=reply.del_kbd удаляет клавиатуру после того как я нажимаю на кнопку "лет"
#@user_private_router.message()
    #async def filter_cmd(message: types.Message):
        #await message.answer(message.text)

# внутри хендллера можно сочетать условия при помомощи &(и),|(или), выглядит примерно так

# F. (...) | (...) тоже самое с и(&)
