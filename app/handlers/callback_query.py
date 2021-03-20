import data.settings_ui as ui
from loader import BOT as bot, COLLECTION  # noqa
from utils.todo import del_task  # noqa


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_keyboard(call):
    if call.message:
        if call.data == list(ui.button_blanks.keys())[0]:
            # Show expanded help
            text = ui.help_todo['full_info']
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=text, parse_mode='HTML', reply_markup=None)
        if call.data == list(ui.button_blanks.keys())[1]:
            # Delete task
            del_status = del_task(call, COLLECTION, call.message.text)
            if del_status:
                text = ui.dialogue['delete_task_success'].format(ui.different_signs['warning'])
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=text)
            else:
                text = ui.dialogue['delete_failed'].format(ui.different_signs['exclamatory'])
                bot.send_message(chat_id=call.message.chat.id, text=text)
