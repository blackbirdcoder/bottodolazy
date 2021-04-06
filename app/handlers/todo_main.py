import data.settings_ui as ui
from loader import BOT as bot, BTN_MORE_HELP, KEYBOARD_MENU_CASE as MENU_CASE, KEYBOARD_MENU_MAIN as MENU_MAIN, COLLECTION # noqa
from loader import KEYBOARD_MENU_NOTIFI as MENU_NOTIFI, MIN_VALUE, MAX_VALUE # noqa
from utils.todo import notification_before_task, add_task, show_tasks, edit_tasks, notifi_change_status # noqa
from utils.interval import pre_interval_notifications, interval_change # noqa
from handlers.todo_start import todo_start # noqa


@bot.message_handler(content_types=['text'])
def todo_main(message):
    if message.chat.type == 'private':
        if message.text == ui.menu_main_items['help']:
            bot.send_message(message.from_user.id, ui.help_todo['short_info'],
                             parse_mode='HTML')
            text = ui.dialogue['more_info'].format(message.from_user.first_name)
            bot.send_message(message.from_user.id, text, reply_markup=BTN_MORE_HELP)
        if message.text == ui.menu_main_items['add']:
            text = ui.dialogue['change_list']
            bot.send_message(message.from_user.id, text, reply_markup=MENU_CASE)
        if message.text == ui.menu_list_items['important']:
            list_name = list(ui.menu_list_items.keys())[0]
            text = ui.dialogue['task_desc']
            notification_before_task(message, text)
            bot.register_next_step_handler(message, add_task, list_name, COLLECTION)
        if message.text == ui.menu_list_items['ordinary']:
            list_name = list(ui.menu_list_items.keys())[1]
            text = ui.dialogue['task_desc']
            notification_before_task(message, text)
            bot.register_next_step_handler(message, add_task, list_name, COLLECTION)
        if message.text == ui.menu_list_items['back']:
            sticker = open(ui.sticker_path['main'], 'rb')
            bot.send_sticker(message.from_user.id, sticker)
            text = ui.dialogue['main_menu']
            bot.send_message(message.from_user.id, text, reply_markup=MENU_MAIN)
        if message.text == ui.menu_main_items['view']:
            show_tasks(message, COLLECTION)
        if message.text == ui.menu_main_items['edit']:
            edit_tasks(message, COLLECTION)
        if message.text == ui.menu_main_items['notifi']:
            text = ui.dialogue['notification_settings'].format(ui.different_signs['gear'])
            bot.send_message(message.from_user.id, text, reply_markup=MENU_NOTIFI)
        if message.text == ui.menu_settings_notification['notification_off']:
            notifi_change_status(message, COLLECTION, False)
            todo_start(message)
        if message.text == ui.menu_settings_notification['notification_interval']:
            text = ui.interval_warning['desc_warning'].format(min=MIN_VALUE, max=MAX_VALUE)
            bot.send_message(message.from_user.id, text)
            pre_interval_notifications(message)
            bot.register_next_step_handler(message, interval_change)

