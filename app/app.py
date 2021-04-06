if __name__ == '__main__':
    from loader import BOT as bot
    from handlers import todo_start, todo_main, callback_query
    from utils.todo import thread_schedule
    thread_schedule()
    bot.polling(none_stop=True)
