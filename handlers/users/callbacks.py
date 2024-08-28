from data.loader import bot
from telebot.types import Message, CallbackQuery, ReplyKeyboardRemove
from bot.models import Feedback, TgUser

from keyboards.inline import menu_buttons, setting_buttons
from keyboards.default import location_button, back_button


@bot.callback_query_handler(func=lambda call: call.data == 'uzbek')
def reaction_to_language(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    photo_path = "sources/img.png"
    caption = "Chinashop bot eng zor tanlov!"
    bot.send_photo(chat_id, photo=open(photo_path, 'rb'), caption=caption, reply_markup=menu_buttons())


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def reaction_to_language(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    photo_path = "sources/img.png"
    caption = "Chinashop bot eng zor tanlov!"
    bot.send_photo(chat_id, photo=open(photo_path, 'rb'), caption=caption, reply_markup=menu_buttons())


@bot.callback_query_handler(func=lambda call: call.data == 'feedback')
def feedback(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    msg = bot.send_message(chat_id, 'Feedback qoldiring!', reply_markup=back_button())
    bot.register_next_step_handler(msg, save_feedback)


def save_feedback(message: Message):
    chat_id = message.chat.id
    if message.text == "Ortga":
        bot.send_message(chat_id, "Bosh menyuga qaytildi", reply_markup=ReplyKeyboardRemove())
        photo_path = "sources/img.png"
        caption = "Chinashop bot eng zor tanlov!"
        bot.send_photo(chat_id, photo=open(photo_path, 'rb'), caption=caption, reply_markup=menu_buttons())
    else:
        user_id = message.from_user.id
        tguser = TgUser.objects.get(telegram_id=user_id)
        Feedback.objects.create(user=tguser, text=message.text)
        bot.send_message(chat_id, "Fikringiz uchun raxmat💥", reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, "China shop", reply_markup=menu_buttons())


@bot.callback_query_handler(func=lambda call: call.data == 'settings')
def back(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, "Sozlamalar", reply_markup=setting_buttons())


@bot.callback_query_handler(func=lambda call: call.data == 'change_num')
def change_number(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    msg = bot.send_message(chat_id, "Yangi raqamni kiriting", reply_markup=back_button())
    bot.register_next_step_handler(msg, number_changer)


def number_changer(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.text == "Ortga":
        bot.send_message(chat_id, "Ortga qaytildi", reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, "China  shop", reply_markup=setting_buttons())
        return
    elif message.text.startswith('+998') and len(message.text) == 13 and message.text[1:].isdigit():
        phone_number = message.text
    else:
        msg = bot.send_message(chat_id, "Telefon raqamni qaytadan kiriting!")
        bot.register_next_step_handler(msg, number_changer)
        return  # Stop further execution if the number is invalid

    try:
        tguser = TgUser.objects.get(telegram_id=user_id)
        tguser.phone_number = phone_number
        tguser.save()
        bot.send_message(chat_id, "Telefon raqam o'zgartirildi", reply_markup=setting_buttons())
    except TgUser.DoesNotExist:
        bot.send_message(chat_id, "Foydalanuvchi topilmadi.")
    except Exception as e:
        bot.send_message(chat_id, f"Xatolik yuz berdi: {str(e)}")


@bot.callback_query_handler(func=lambda call: call.data == 'location')
def insert_location(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    msg = bot.send_message(chat_id, "lokatsiyani yuborish tugmasini bosing", reply_markup=location_button())
    bot.register_next_step_handler(msg, location_save)


def location_save(message: Message):
    chat_id = message.chat.id
    if message.location:
        user_id = message.from_user.id
        user = TgUser.objects.get(telegram_id=user_id)
        user.location_lat = message.location.latitude
        user.location_long = message.location.longitude
        user.save()
        bot.send_message(chat_id, "Lokatsiya saqlandi", reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, "Sozlamalar", reply_markup=setting_buttons())
    elif message.text:
        if message.text == "Ortga":
            bot.send_message(chat_id, "Ortga qaytildi", reply_markup=ReplyKeyboardRemove())
            bot.send_message(chat_id, "Sozlamalar", reply_markup=setting_buttons())
            return
        else:
            msg = bot.send_message(chat_id, "lokatsiyangizni qaytadan jonating!")
            bot.register_next_step_handler(msg, location_save)
            return
    else:
        msg = bot.send_message(chat_id, "lokatsiyangizni qaytadan jonating!")
        bot.register_next_step_handler(msg, location_save)
        return
