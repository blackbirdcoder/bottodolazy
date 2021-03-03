import pymongo


def connect(client, db_name, db_collection_name):
    try:
        print("Connect: MongoDB version is %s" % client.server_info()['version'])
        db = client[db_name]
        db_collection = db[db_collection_name]
        return {
            'db': db,
            'collection': db_collection
        }
    except pymongo.errors.OperationFailure as error: # noqa
        print(error)
        quit(1)
