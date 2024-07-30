from bot.models import TgUser


def create_user(full_name, first_name, last_name, telegram_id, phone_number):
    user = TgUser.objects.create(full_name, first_name, last_name, telegram_id, phone_number)
    return user

