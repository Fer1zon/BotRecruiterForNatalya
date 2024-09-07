
from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesAdmin, dp,bot, cur,conn

from utils.function.getMessageText import getCommandsList






async def startBotHandlerAdmin(message : types.Message):
    sendText = getCommandsList()

    await message.answer(sendText)
    await StatesAdmin.MAIN_MENU.set()
    
    