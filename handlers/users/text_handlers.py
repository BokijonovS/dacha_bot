from bot.models import TgUser
from data.loader import bot
from telebot.types import Message, ReplyKeyboardRemove

from functions.user_checker import name_checker
from keyboards.default import phone_button
from keyboards.inline import menu_buttons



USER_DATA = {}


@bot.message_handler(func=lambda message: message.text == "Ro'yxatdan o'tish")
def register(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    USER_DATA[from_user_id] = {}
    msg = bot.send_message(chat_id, "Ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_name)


def get_name(message: Message):
    chat_id = message.chat.id
    name1 = message.text
    if name_checker(name1):
        name = message.text
    else:
        msg = bot.send_message(chat_id, "Ismingizni bosh harfini katta bilan lotin harflarida kiriting")
        bot.register_next_step_handler(msg, get_name)

    from_user_id = message.from_user.id
    USER_DATA[from_user_id]["name"] = name
    msg = bot.send_message(chat_id, "Telefon raqamni yuborish tugmasini bosing!", reply_markup=phone_button())
    bot.register_next_step_handler(msg, save_user)


def save_user(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    name = USER_DATA[from_user_id]['name']

    if message.contact:
        phone_number = message.contact.phone_number
    elif message.text.startswith('+998') and len(message.text) == 13 and message.text[1:].isdigit():
        phone_number = message.text
    else:
        msg = bot.send_message(chat_id, "Telefon raqamni yuborish tugmasini bosing!", reply_markup=phone_button())
        bot.register_next_step_handler(msg, save_user)

    user = TgUser.objects.get(telegram_id=from_user_id)
    user.name = name
    user.phone_number = phone_number
    user.save()
    del USER_DATA[from_user_id]
    bot.send_message(chat_id, "Ro'yxatdan o'tdingiz", reply_markup=ReplyKeyboardRemove())
    bot.send_photo(chat_id, photo="sources/img.png", caption="Botga xush kelibsiz, tilni tanlang", reply_markup=menu_buttons())


@bot.message_handler(func=lambda message: message.text == "Bosh menyu")
def menu(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bosh menyuga qaytdingiz", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, "China botga hush kelibsiz", reply_markup=menu_buttons())
