import telebot


def create_keyboard(btn_names: dict):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = [telebot.types.KeyboardButton(current_value)
           for current_value in btn_names.values()]
    keyboard.add(*btn)
    return keyboard
