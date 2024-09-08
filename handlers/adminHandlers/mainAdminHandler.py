from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesUser, dp,bot, cur,conn

from utils.function.JSONProcess import editChannelUrl, editOnlineTestLink

from validators import url






async def editLink1(message:types.Message):
    if not url(message.get_args()):
        return await message.answer("Введенный вами URL не валиден!")
    
    editChannelUrl(1, message.get_args())

    await message.answer("Ссылка на канал 1 успешно изменена!")



async def editLink2(message : types.Message):
    if not url(message.get_args()):
        return await message.answer("Введенный вами URL не валиден!")
    
    editChannelUrl(2, message.get_args())

    await message.answer("Ссылка на канал 2 успешно изменена!")
    

async def editOnlineTestLinkH(message : types.Message):
    if not url(message.get_args()):
        return await message.answer("Введенный вами URL не валиден!")
    
    editOnlineTestLink(message.get_args())

    await message.answer("Ссылка на онлайн тест успешно изменена!")















