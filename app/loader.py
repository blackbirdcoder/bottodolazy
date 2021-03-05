import telebot
from data import config
import pymongo
from utils.db import connect
import keyboards.keyboard as keyboard
from data.settings_ui import menu_main_items


BOT = telebot.TeleBot(config.TELEGRAM_TOKEN)
MDB_CLIENT = pymongo.MongoClient(config.MDB_STRING_CONNECT)
DB = connect(MDB_CLIENT, config.MDB_NAME, config.MDB_COLLECTION_NAME)
COLLECTION = DB[list(DB.keys())[1]]
KEYBOARD_MENU_MAIN = keyboard.create_keyboard(menu_main_items)