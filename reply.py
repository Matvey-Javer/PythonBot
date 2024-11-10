from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='меню'),
        ],
        {
            KeyboardButton(text='список друзей'),
            KeyboardButton(text='лет')
        }
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вы хотите узнать?'
)

del_kbd = ReplyKeyboardRemove() #данная строка позволяет удалить клавиатуру после нажатия кнопки

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Полное имя'),
    KeyboardButton(text='Рост'),
    KeyboardButton(text='Вес'),
    KeyboardButton(text='Кол-во полных лет'),
    KeyboardButton(text='Знак зодиака'),
    KeyboardButton(text='Дата рождения'),
    KeyboardButton(text='Любимый цвет'),
    KeyboardButton(text='Любимое аниме')
)
start_kb2.adjust(1, 3, 3, 1)

#добавление новой клавиатуры, код ниже

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row( KeyboardButton(text='Список доступных друзей🤯')) #row добавит эту кнопку просто новым рядом

