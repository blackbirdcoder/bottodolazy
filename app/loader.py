import telebot
from data import config
import pymongo
from utils.db import connect

BOT = telebot.TeleBot(config.TELEGRAM_TOKEN)
MDB_CLIENT = pymongo.MongoClient(config.MDB_STRING_CONNECT)
DB = connect(MDB_CLIENT, config.MDB_NAME, config.MDB_COLLECTION_NAME)
COLLECTION = DB[list(DB.keys())[1]]
