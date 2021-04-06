import data.settings_ui as ui # noqa
from loader import BOT as bot, telebot, MIN_VALUE, MAX_VALUE, COLLECTION, KEYBOARD_MENU_NOTIFI as MENU_NOTIFI # noqa
from utils.db import user_get_notifications, user_update_notification # noqa
from handlers.todo_start import todo_start  # noqa
from utils.todo import notifi_change_status # noqa


def pre_interval_notifications(message):
    text = ui.dialogue['input_interval']
    bot.send_message(message.from_user.id, text,
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def interval_validity(message):
    try:
        answer = int(message.text)
        if MIN_VALUE <= answer <= MAX_VALUE:
            return answer
        else:
            raise ValueError
    except ValueError:
        text = ui.dialogue['interval_error'].format(ui.different_signs['exclamatory'],
                                                    message.from_user.first_name)
        bot.send_message(message.from_user.id, text, reply_markup=MENU_NOTIFI)


def interval_change(message):
    new_interval = interval_validity(message)
    if new_interval:
        notifi_status = user_get_notifications(message, COLLECTION)['notifications']
        if not notifi_status:
            notifi_change_status(message, COLLECTION, True)
        success_change = user_update_notification(message, COLLECTION,
                                                  'notification_interval',
                                                  new_interval)
        if success_change:
            text = ui.dialogue['new_interval'].format(ui.different_signs['warning'])
            bot.send_message(message.from_user.id, text)
            todo_start(message)
        else:
            text = ui.dialogue['interval_fail'].format(ui.different_signs['exclamatory'])
            bot.send_message(message.from_user.id, text, reply_markup=MENU_NOTIFI)
