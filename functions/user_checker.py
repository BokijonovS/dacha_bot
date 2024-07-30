from bot.models import TgUser


def check_user(user_id):
    status = TgUser.objects.get(telegram_id=user_id)
    if status.name and status.phone_number:
        return True
    else:
        return False


letters = "abcdefghijklmnopqrstuvwxyz '"


def name_checker(name):
    name1 = str(name)
    for i in name1:
        if i.lower() not in letters:
            return False
    if name1.istitle():
        return True
    else:
        return False
