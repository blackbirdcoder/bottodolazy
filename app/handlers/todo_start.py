from loader import BOT as bot, COLLECTION # noqa


@bot.message_handler(commands=['start'])
def todo_start(message):
    bot.reply_to(message, 'bot work!')
