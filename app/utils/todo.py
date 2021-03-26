import data.settings_ui as ui  # noqa
from loader import BOT as bot, telebot, KEYBOARD_MENU_CASE as MENU_CASE, COLLECTION, KEYBOARD_MENU_BACK as MENU_BACK  # noqa
from loader import BTN_CNL_BAR_READY, BTN_CNL_BAR_NOT_READY  # noqa
from random import getrandbits, sample
from utils.db import user_set_task, user_get_tasks, user_del_task, user_update_task  # noqa


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


def edit_tasks(message, db_collection):
    tasks = user_get_tasks(message, db_collection)
    if tasks['important'] is None and tasks['ordinary'] is None:
        text = ui.dialogue['lists_empty'].format(ui.different_signs['warning'])
        bot.send_message(message.from_user.id, text, reply_markup=MENU_BACK)
    else:
        text = ui.dialogue['lists_ready_change'].format(ui.different_signs['warning'])
        bot.send_message(message.from_user.id, text, reply_markup=MENU_BACK)
    cards = []

    def create_task_cards(asset, pic_status, txt_status, tasks_dict, list_name, item_list):
        blank = {
            'head': asset['card_head'].format(list_item=item_list, separator=asset['separator']),
            'cards_full_info': tasks_dict[list_name],
            'screen_info': []
        }
        if blank['cards_full_info'] is not None:
            for value in blank['cards_full_info']:
                if value.get('task_status'):
                    txt, pic = txt_status['ready'], pic_status['ready']
                else:
                    txt, pic = txt_status['not_ready'], pic_status['not_ready']
                blank['screen_info'].append(asset['card_desc'].format(task=value.get('task'),
                                                                      status=txt, pic_status=pic,
                                                                      task_id=value.get('task_id')))
            cards.append(blank)
        else:
            blank['screen_info'].append(asset['card_empty'])
            cards.append(blank)

    def show_card(cards_tasks):
        show_card_text = cards_tasks['head']
        bot.send_message(message.from_user.id, show_card_text, parse_mode='HTML')
        if cards_tasks['cards_full_info'] is not None:
            for index, current_dict in enumerate(cards_tasks['cards_full_info']):
                if current_dict.get('task_status'):
                    show_card_text = cards_tasks['screen_info'][index]
                    bot.send_message(message.from_user.id, show_card_text,
                                     reply_markup=BTN_CNL_BAR_NOT_READY,
                                     parse_mode='HTML')
                else:
                    show_card_text = cards_tasks['screen_info'][index]
                    bot.send_message(message.from_user.id, show_card_text,
                                     reply_markup=BTN_CNL_BAR_READY,
                                     parse_mode='HTML')
        else:
            show_card_text = cards_tasks['screen_info']
            bot.send_message(message.from_user.id, show_card_text, parse_mode='HTML')

    create_task_cards(ui.card_asset, ui.pic_task_status, ui.txt_task_status,
                      tasks, 'important', ui.menu_list_items['important'], )
    create_task_cards(ui.card_asset, ui.pic_task_status, ui.txt_task_status,
                      tasks, 'ordinary', ui.menu_list_items['ordinary'], )
    show_card(cards[0])
    show_card(cards[1])


def extract_id(text):
    return text.split(':')[-1].strip()


def find_list(call, db_collection, task_id):
    tasks = user_get_tasks(call, db_collection)
    for current_key, current_value in tasks.items():
        if current_value is not None:
            for value in current_value:
                if value.get('task_id') == task_id:
                    return current_key


def find_index_task(call, db_collection, task_id, task_list_name):
    tasks = user_get_tasks(call, db_collection)
    for index, value_dict in enumerate(tasks[task_list_name]):
        if value_dict.get('task_id') == task_id:
            return index


def del_task(call, db_collection, text):
    target_id = extract_id(text)
    target_list = find_list(call, db_collection, target_id)
    if target_list is not None:
        return user_del_task(call, db_collection, target_list, target_id)
    else:
        return False


def edited_task_card(modified_card):
    """
    task card to be redisplayed after modification
    """
    task_ready = False
    txt, pic = ui.pic_task_status['not_ready'], ui.txt_task_status['not_ready']
    for key, value in modified_card.items():
        if key == 'task_status' and value is True:
            task_ready = True
            txt, pic = ui.pic_task_status['ready'], ui.txt_task_status['ready']
    result = [ui.card_asset['card_desc'].format(task=modified_card.get('task'),
                                                status=txt, pic_status=pic,
                                                task_id=modified_card.get('task_id'))]
    result.append(BTN_CNL_BAR_NOT_READY) if task_ready is not False else result.append(BTN_CNL_BAR_READY)
    return result


def edit_text(call, db_collection, text):
    target_id = extract_id(text)
    target_list = find_list(call, db_collection, target_id)
    task_index = find_index_task(call, db_collection, target_id, target_list)
    bot.send_message(chat_id=call.message.chat.id,
                     text=ui.dialogue['new_text'].format(ui.different_signs['warning']),
                     reply_markup=telebot.types.ReplyKeyboardRemove())

    def add_new_text(msg, need_list, need_index):
        new_text = msg.text
        user_task = user_get_tasks(msg, db_collection)[need_list][need_index]
        user_task['task'] = new_text
        update_status = user_update_task(msg, COLLECTION, need_list, need_index, user_task)
        if update_status:
            notify_text = ui.dialogue['text_changed'].format(ui.different_signs['warning'])
            bot.send_message(chat_id=call.message.chat.id,
                             text=notify_text, reply_markup=MENU_BACK)
            new_screen_info = edited_task_card(user_task)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=new_screen_info[0], reply_markup=new_screen_info[1], parse_mode='HTML')
        else:
            notify_text = ui.dialogue['text_not_changed'].format(ui.different_signs['exclamatory'])
            bot.send_message(chat_id=call.message.chat.id, text=notify_text, reply_markup=MENU_BACK)

    bot.register_next_step_handler(call.message, add_new_text, target_list, task_index)


def switch_task_status(call, db_collection, text):
    target_id = extract_id(text)
    target_list = find_list(call, db_collection, target_id)
    task_index = find_index_task(call, db_collection, target_id, target_list)
    user_task = user_get_tasks(call, db_collection)[target_list][task_index]
    if user_task.get('task_status'):
        user_task['task_status'] = False
    else:
        user_task['task_status'] = True
    update_status = user_update_task(call, COLLECTION, target_list, task_index, user_task)
    if update_status:
        new_screen_info = edited_task_card(user_task)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=new_screen_info[0], reply_markup=new_screen_info[1], parse_mode='HTML')
        text = ui.dialogue['task_status_changed'].format(ui.different_signs['warning'])
        bot.send_message(chat_id=call.message.chat.id, text=text)
    else:
        # TODO: Edit branch
        pass

