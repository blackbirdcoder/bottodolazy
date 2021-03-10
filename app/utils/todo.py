import data.settings_ui as ui # noqa
from loader import BOT as bot, telebot, KEYBOARD_MENU_CASE as MENU_CASE, COLLECTION # noqa
from random import getrandbits, sample
from utils.db import user_set_task, user_get_tasks # noqa


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


def add_task(message, list_name, db_collection):
    rec_status = None
    if list_name == 'important':
        task = create_task(message.text)
        rec_status = user_set_task(message, db_collection, list_name, task)
    if list_name == 'ordinary':
        task = create_task(message.text)
        rec_status = user_set_task(message, db_collection, list_name, task)
    if not rec_status:
        text = ui.dialogue['not_success']
        bot.send_message(message.from_user.id, text)
    else:
        text = ui.dialogue['add_success']
        bot.send_message(message.from_user.id, text)
    text = ui.dialogue['change_list']
    bot.send_message(message.from_user.id, text, reply_markup=MENU_CASE)


def show_tasks(message, db_collection):
    tasks = user_get_tasks(message, db_collection)
    tables = create_tables(tasks, ui.table_asset,
                           ui.pic_task_status,
                           ui.menu_list_items['important'],
                           ui.menu_list_items['ordinary'])
    bot.send_message(message.from_user.id, tables[0], parse_mode='HTML')
    bot.send_message(message.from_user.id, tables[1], parse_mode='HTML')


def create_tables(tasks: dict, asset: dict, pic_status: dict,
                  item_important: str, item_ordinary: str):
    result = []

    def filler(task_list, item_list):
        blank = [asset['task_start_desc'].format(
            list_item=item_list, separator=asset['separator'])]
        if task_list is not None:
            for value in task_list:
                if value.get('task_status'):
                    pic = pic_status['ready']
                else:
                    pic = pic_status['not_ready']
                blank.append(
                    asset['task_desc'].format(status=pic, task=value.get(
                        'task'), separator=asset['separator']))
            result.append(''.join(blank))
        else:
            blank.append(asset['task_empty'])
            result.append(''.join(blank))

    filler(tasks['important'], item_important)
    filler(tasks['ordinary'], item_ordinary)
    return result








