if __name__ == '__main__':
    from loader import BOT as bot
    from handlers import todo_start
    bot.polling(none_stop=True)
