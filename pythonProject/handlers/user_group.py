import string

from aiogram import F, types, Router, Bot
from aiogram.filters import Command

from common.ban_word import bad_word
from filtres.chat_types import ChatTypeFilter

import common.ban_word

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
user_group_router.edited_message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    #просмотреть все данные и свойства полученных объектов
    #print(admins_list)
    # Код ниже это генератор списка, как и этот x = [i for i in range(10)]
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    #print(admins_list)

restricted_word = common.ban_word.bad_word

def clean_text(text: str):
    return text.translate(str.maketrans('', '', string.punctuation))

@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.message):
    if restricted_word.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.first_name}, ❗я слежу за вами, соблюдайте порядок в чате!❗")
        await message.delete()
        #await message.chat.ban(message.from_user.id)