import telebot


def create_keyboard(btn_names: dict):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = [telebot.types.KeyboardButton(current_value)
           for current_value in btn_names.values()]
    keyboard.add(*btn)
    return keyboard


def create_inline_keyboard(data: dict):
    inline_keyboard = telebot.types.InlineKeyboardMarkup()
    inline_btn = [telebot.types.InlineKeyboardButton(text=current_value,
                                                     callback_data=current_key)
                  for current_key, current_value in data.items()]
    inline_keyboard.add(*inline_btn)
    return inline_keyboard
