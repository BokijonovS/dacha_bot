from data.loader import bot
from telebot.types import Message
from bot.models import TgUser
from functions.user_checker import check_user
from keyboards.default import register_button


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        TgUser.objects.create(telegram_id=user_id)
    except:
        pass
    registered = check_user(user_id)
    if registered:
        bot.send_message(chat_id, "Assalomu alekum hush kelibsiz")
    else:
        bot.send_message(chat_id, "Royxatdan oting", reply_markup=register_button())
