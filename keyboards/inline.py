from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def menu_buttons(uuid):
    markup = InlineKeyboardMarkup(row_width=2)
    app_url = f"https://t.me/uzchinashopbot/uzchinatrade?uuid={uuid}"
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
    markup = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton("Ismingizni o'zgartiring!", callback_data='change_name')
    btn2 = InlineKeyboardButton("Telefon raqamingizni o'zgartiring ☎️", callback_data='change_num')
    btn3 = InlineKeyboardButton('Doimiy joylashuvingizni tanlang 📍', callback_data='location')
    btn4 = InlineKeyboardButton('Ortga◀️', callback_data='back')
    markup.add(btn2)
    markup.add(btn1, btn3)
    markup.add(btn4)
    return markup
