import pymongo


def connect(client, db_name, db_collection_name):
    try:
        print('Connect: MongoDB version is %s' % client.server_info()['version'])
        db = client[db_name]
        db_collection = db[db_collection_name]
        return {
            'db': db,
            'collection': db_collection
        }
    except pymongo.errors.OperationFailure as error:  # noqa
        print(error)
        quit(1)


# ============ create
def add_user(message, db_collection):
    if db_collection.find_one({'user_telegram_id': message.from_user.id}) is None:
        user = {
            'user_telegram_id': message.from_user.id,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'important': [],
            'ordinary': [],
            'notifications': False,
            'notification_interval': 60,
            'working_process': True
        }
        db_collection.insert_one(user)
        return True


# ============ get
def user_get_tasks(message, db_collection):
    result = {}
    tasks = db_collection.find_one({'user_telegram_id': message.from_user.id},
                                   {'important', 'ordinary'})
    if tasks.get('_id'):
        del tasks['_id']
    for key, value in tasks.items():
        if value:
            result[key] = value
        else:
            result[key] = None
    return result
