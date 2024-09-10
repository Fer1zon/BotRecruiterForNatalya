
from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesAdmin, dp,bot 

from utils.function.getMessageText import getCommandsList






async def startBotHandlerAdmin(message : types.Message):
    sendText = getCommandsList()

    await message.answer(sendText, disable_web_page_preview=True)
    await StatesAdmin.MAIN_MENU.set()
    
    