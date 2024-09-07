from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import sys
import os

if __package__:
    from . import config
else:
    sys.path.append(os.path.dirname(__file__) + '/..')
    import config


import sqlite3 

conn = sqlite3.connect(config.dataBasePath)
cur = conn.cursor()







bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot,storage=MemoryStorage())

class StatesUser(StatesGroup):  # Создаём состояния юзера
    NAME_SURNAME = State()
    RESIDENCE_CITY = State()
    PHONE_NUMBER = State()
    TELEGRAM_USERNAME = State()
    SOCIAL_NETWORK = State()
    SALES_EXPERIENCE = State()
    WORK_EXPERIENCE = State()
    DISMISSAL_REASON = State()
    NO_RESULT = State()
    CURRENT_WORK = State()
    FAST_PRINT = State()
    ATTITUDE_CHANGE = State()
    CURRENT_PC = State()
    IMPORTANT = State()
    SPEED_TRAINING = State()
    TIME_ZONE = State()
    
    ONLINE_TEST_IMG = State()

    ACCEPT_POLICY_PERSONAL_DATA = State()
    
    EXPECTATION = State()


class StatesAdmin(StatesGroup):  # Создаём состояния Админа
    MAIN_MENU = State()
