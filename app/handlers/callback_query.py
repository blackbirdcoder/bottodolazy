import data.settings_ui as ui
from loader import BOT as bot # noqa


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_keyboard(call):
    if call.message:
        if call.data == list(ui.inline_btn['help'].keys())[0]:
            text = ui.help_todo['full_info']
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=text, parse_mode='HTML', reply_markup=None)