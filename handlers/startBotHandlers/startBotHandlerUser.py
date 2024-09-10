from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesUser, dp,bot, cur,conn







async def startBotHandlerUser(message : types.Message):
    sendText0 = "Здравствуйте. Для рассмотрения вашей кандидатуры важно пройти опрос-собеседование из 16 вопросов. Если вашу кандидатуру одобрят, то с вами свяжутся и вы получите доступ к обучению."
    sendText = "Напишите ваше ФИО"

    await message.answer(sendText0)
    await message.answer(sendText)
    await StatesUser.NAME_SURNAME.set()
    