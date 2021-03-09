import data.settings_ui as ui # noqa
from loader import BOT as bot, telebot, KEYBOARD_MENU_CASE as MENU_CASE, COLLECTION # noqa
from random import getrandbits, sample
from utils.db import user_set_task # noqa


def quantity_tasks(dicts):
    result = {}
    for key, value in dicts.items():
        if value is not None:
            result[key] = len(value)
        else:
            result[key] = '0'
    return result


def notification_before_task(message, text):
    bot.send_message(message.from_user.id, text,
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def create_task(txt: str):
    def generate_id():
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = getrandbits(4)
        chars = sample(alphabet, 2)
        while True:
            yield str(num) + ''.join(chars)
    return {'task_id': next(generate_id()), 'task_status': False, 'task': txt}


def add_task(message, list_name):
    rec_status = None
    if list_name == 'important':
        task = create_task(message.text)
        rec_status = user_set_task(message, COLLECTION, list_name, task)
    if list_name == 'ordinary':
        task = create_task(message.text)
        rec_status = user_set_task(message, COLLECTION, list_name, task)
    if not rec_status:
        text = ui.dialogue['not_success']
        bot.send_message(message.from_user.id, text)
    else:
        text = ui.dialogue['add_success']
        bot.send_message(message.from_user.id, text)
    text = ui.dialogue['change_list']
    bot.send_message(message.from_user.id, text, reply_markup=MENU_CASE)
