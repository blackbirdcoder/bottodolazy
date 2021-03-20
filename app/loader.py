import telebot
from data import config
import pymongo
from utils.db import connect
import keyboards.keyboard as keyboard
from data.settings_ui import menu_main_items, inline_btn, menu_list_items, menu_back_item


BOT = telebot.TeleBot(config.TELEGRAM_TOKEN)
MDB_CLIENT = pymongo.MongoClient(config.MDB_STRING_CONNECT)
DB = connect(MDB_CLIENT, config.MDB_NAME, config.MDB_COLLECTION_NAME)
COLLECTION = DB[list(DB.keys())[1]]
KEYBOARD_MENU_MAIN = keyboard.create_keyboard(menu_main_items)
BTN_MORE_HELP = keyboard.create_inline_keyboard(inline_btn['help'])
KEYBOARD_MENU_CASE = keyboard.create_keyboard(menu_list_items)
KEYBOARD_MENU_BACK = keyboard.create_keyboard(menu_back_item)
BTN_CNL_BAR_READY = keyboard.create_inline_keyboard(inline_btn['control_panel_btn_ready'])
BTN_CNL_BAR_NOT_READY = keyboard.create_inline_keyboard(inline_btn['control_panel_btn_not_ready'])
