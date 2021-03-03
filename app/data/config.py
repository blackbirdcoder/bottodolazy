import os
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
MDB_PASSWORD = os.getenv('MDB_PASSWORD')
MDB_NAME = os.getenv('MDB_NAME')
MDB_COLLECTION_NAME = os.getenv('MDB_COLLECTION_NAME')
MDB_STRING_CONNECT = os.getenv('MDB_STRING_CONNECT').format(MDB_PASSWORD, MDB_NAME)
