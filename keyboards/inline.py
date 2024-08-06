from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

app_url = "https://t.me/uzchinashopbot/uzchinatrade"


def lang_buttons():
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton('Uzbek', callback_data='uzbek')
    # btn2 = InlineKeyboardButton('Русский', callback_data='russian')
    markup.add(btn1)
    return markup


def menu_buttons():
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("Do'konni ochish🛍", url=app_url)
    btn2 = InlineKeyboardButton('Fikr qoldirish🗒', callback_data='feedback')
    btn3 = InlineKeyboardButton('Sozlamalar⚙️', callback_data='settings')

    markup.add(btn1)
    markup.add(btn2, btn3)
    return markup


def back_button():
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Ortga◀️', callback_data='back')
    markup.add(btn1)
    return markup


def setting_buttons():
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("Tilni o'zgartirish🌐", callback_data='change_lang')
    btn2 = InlineKeyboardButton("No'meringizni o'zgartiring☎️", callback_data='change_num')
    btn3 = InlineKeyboardButton('Doimiy joylashuvingizni tanlang📍', callback_data='location')
    btn4 = InlineKeyboardButton('Ortga◀️', callback_data='back')
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup
