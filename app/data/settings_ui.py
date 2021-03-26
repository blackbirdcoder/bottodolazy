bot_name = 'Ленни Бот'

sticker_path = {
    'hello': 'static/images/lazyhello.webp',
    'returned': 'static/images/lazyreturned.webp',
    'main': 'static/images/lazymainmenu.webp'
}

dialogue = {
    'welcome_text': 'Привет! Дорогой друг {}.\n'
                    'Я {}. Твой помощник по делам на ближайшее время.',
    'user_returned': 'С возвращением, {}.\n '
                     '{} задач: <b>{}</b>\n '
                     '{} задач: <b>{}</b>\n',
    'more_info': '{}, хотите узнать подробней?',
    'change_list': 'Выберете список:',
    'task_desc': 'Опишите задачу:',
    'add_success': 'Задача добавлена в список',
    'not_success': 'Что-то пошло не так. Ошибка!',
    'main_menu': 'Главное меню',
    'lists_ready_change': '{} Списки готовы к изменениям',
    'lists_empty': '{} Списки пустые, нечего изменять',
    'delete_task_success': '{} Задача удалена',
    'delete_failed': '{} Не могу удалить задачу',
    'new_text': '{} Введите новый текст задачи:',
    'text_changed': '{} Текст задачи изменен',
    'text_not_changed': '{} Не удалось изменить текст задачи',
    'task_status_changed': '{} Статус задачи изменен'
}

menu_main_items = {
    'add': '\U0000270D Добавить',
    'view': '\U0001F4D6 Просмотр',
    'edit': '\U0001F4DD Редактировать',
    'notifi': '\U0001F4E3 Уведомления',
    'help': '\U00002753 Помощь',
}

button_blanks = {
    'more_help_info': 'Хочу...',
    'del': 'Удалить',
    'edit': 'Редактировать',
    'ready': 'Готово',
    'not_ready': 'Отмена'
}

inline_btn = {
    'help': {
        'more_help_info': button_blanks['more_help_info'],
    },
    'control_panel_btn_ready': {
        'del': button_blanks['del'],
        'edit': button_blanks['edit'],
        'ready': button_blanks['ready']
    },
    'control_panel_btn_not_ready': {
        'del': button_blanks['del'],
        'edit': button_blanks['edit'],
        'not_ready': button_blanks['not_ready']
    }
}

different_signs = {
    'warning': '\U000026A0',
    'exclamatory': '\U00002757',
}

menu_list_items = {
    'important': '\U0001F4D5 Важный',
    'ordinary': '\U0001F4D7 Обычный',
    'back': '\U00002B05 Назад',
}

menu_back_item = {
    'back': menu_list_items['back']
}

pic_task_status = {
    'ready': '\U00002705',
    'not_ready': '\U000025FB'
}

txt_task_status = {
    'ready': 'Готово',
    'not_ready': 'Не готово'
}

help_todo = {
    'short_info': f'<b>{menu_main_items["add"]}</b> - <i>Добавить задачи</i>\n'
                  f'<b>{menu_main_items["view"]}</b> - <i>Просмотр задач</i>\n'
                  f'<b>{menu_main_items["edit"]}</b> - <i>Править задачи</i>\n'
                  f'<b>{menu_main_items["notifi"]}</b> - <i>Задать интервал</i>\n'
                  f'<b>{menu_main_items["help"]}</b> - <i>Посмотреть помощь</i>\n',
    'full_info': 'Этот бот поможет вам вести список дел.\n'
                 f'Чтобы начать работать со списком, нажмите кнопку \"<b>{menu_main_items["add"]}</b>\". '
                 'Выберите нужный список и напишите в него задачу.\n'
                 '\n'
                 'Для задач есть два разных списка:\n'
                 f'\"<b>{menu_list_items["ordinary"]}</b>\" - для второстепенных задач.\n'
                 f'\"<b>{menu_list_items["important"]}</b>\" - для самых важных задач, его основное отличие от '
                 'обычного списка - это уведомления. Как это работает? '
                 f'Через время вам от {bot_name + "а"} придёт напоминание'
                 ' о какой-либо невыполненной задаче из важного списка.\n'
                 '\n'
                 f'Кнопка \"<b>{menu_main_items["notifi"]}</b>\" позволяет настроить временной интервал напоминания'
                 ' или отключить его. По умолчанию напоминания работают через каждый час.\n'
                 '\n'
                 f'Кнопка \"<b>{menu_main_items["view"]}</b>\" покажет все ваши записи в списках.\n'
                 '\n'
                 f'Кнопка \"<b>{menu_main_items["edit"]}</b>\" даст доступ к возможностям изменять текст задач, '
                 'отметить их как "готовые" или удалять задачи.\n'
}

table_asset = {
    'separator': '<pre>-----------------------------</pre>',
    'task_start_desc': '<b>{list_item}:</b>\n{separator}\n',
    'task_desc': '{status} <b>{task}</b>\n{separator}\n',
    'task_empty': '<em>Список задач пуст</em>'
}

card_asset = {
    'separator': table_asset['separator'],
    'card_head': table_asset['task_start_desc'],
    'card_desc': '<i>Задача:</i> <b>{task}</b>\n'
                 '<i>Статус:</i> {status} {pic_status}\n'
                 '<i>ID задачи:</i> {task_id}\n',
    'card_empty': table_asset['task_empty']
}

