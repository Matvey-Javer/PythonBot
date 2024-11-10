from aiogram import F, types, Router
from aiogram.filters import Command


from filtres.chat_types import ChatTypeFilter, IsAdmin
from kbds.reply import start_kb3


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

ADMIN_KB = start_kb3(
    "Добавить функционал",
    "Изменить функционал",
    "Удалить функционал",
    "Я так, просто посмотреть зашел",
    placeholder="Выберите действие",
    sizes=(2, 1, 1),
)

@admin_router.message(Command('admin'))
async def add_product(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=ADMIN_KB)

@admin_router.message(F.text == 'Я так, просто посмотреть зешёл')
async def starring_at_product(message: types.Message):
    await message.answer("OK, вот список функций")

@admin_router.message(F.text == 'Изменить товар')
async def change_product(message: types.Message):
    await message.answer("OK, вот список функций")

@admin_router.message(F.text == 'Удалить товар')
async def delete_product(message: types.Message):
    await message.answer("Выберите функцию(и) для удаления")



