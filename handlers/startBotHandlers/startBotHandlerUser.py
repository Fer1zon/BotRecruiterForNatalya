from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesUser, dp,bot, cur,conn







async def startBotHandlerUser(message : types.Message):
    sendText = "Напишите ваше ФИО"

    await message.answer(sendText)
    await StatesUser.NAME_SURNAME.set()
    