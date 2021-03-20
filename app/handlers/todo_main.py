import data.settings_ui as ui
from loader import BOT as bot, BTN_MORE_HELP, KEYBOARD_MENU_CASE as MENU_CASE, KEYBOARD_MENU_MAIN as MENU_MAIN, COLLECTION # noqa
from utils.todo import notification_before_task, add_task, show_tasks, edit_tasks # noqa


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
    print('MAIN SCOPE MSG', message.text)
