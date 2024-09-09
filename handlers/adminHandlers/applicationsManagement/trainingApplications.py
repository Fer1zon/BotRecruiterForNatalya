from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesAdmin, dp,bot

from utils.function.JSONProcess import getChannelUrl





async def acceptTestModule1(call : types.CallbackQuery):
    clientId = call.data.split("|")[-1]
    

    
    sendTextToClient = "Здравствуйте. Вы прошли тест модуля 1."
    sendTextToClient1 = f"Прежде чем приступить к 2-му модулю, ознакомьтесь с материалами в <a href = '{getChannelUrl(2)}'>Канале</a> затем приступайте к тесту. При ответах на вопросы можно брать информацию из <a href = '{getChannelUrl(2)}'>Канала</a> с обучением - важно, чтобы вы понимали где в нужный момент найти ответ на свой вопрос по поводу ситуации"


    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Начать тест", callback_data="startModule2"))


    await call.message.delete()

    await bot.send_message(chat_id=clientId, text=sendTextToClient)
    await bot.send_message(chat_id=clientId, text=sendTextToClient1, reply_markup=keyboard)
    
    






async def declineTestModule1(call : types.CallbackQuery):
    clientId = call.data.split("|")[-1]
    
    sendTextToClient = "Здравствуйте. Вы не прошли тест модуля 1. Попробуйте снова."
    

    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Начать тест", callback_data="startModule1"))


    await call.message.delete()


    await bot.send_message(chat_id=clientId, text = sendTextToClient, reply_markup=keyboard)
    

    
