import data.settings_ui as ui
from loader import BOT as bot, BTN_MORE_HELP # noqa


@bot.message_handler(content_types=['text'])
def todo_main(message):
    if message.chat.type == 'private':
        if message.text == ui.menu_main_items['help']:
            bot.send_message(message.from_user.id, ui.help_todo['short_info'],
                             parse_mode='HTML')
            text = ui.dialogue['more_info'].format(message.from_user.first_name)
            bot.send_message(message.from_user.id, text, reply_markup=BTN_MORE_HELP)
    print('MAIN SCOPE MSG', message.text)
