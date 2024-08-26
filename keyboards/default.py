from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def register_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Ro'yxatdan o'tish")
    markup.add(btn1)
    return markup


def phone_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Telefon raqamni yuborish", request_contact=True)
    markup.add(btn1)
    return markup


def location_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("Lokatsiya yuborish", request_location=True)
    btn2 = KeyboardButton("Ortga")
    markup.add(btn1)
    markup.add(btn2)
    return markup


def back_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Ortga")
    markup.add(btn)
    return markup
