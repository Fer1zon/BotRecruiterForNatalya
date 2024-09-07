from aiogram.dispatcher import Dispatcher



import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser
from importantFiles.helps import StatesUser, dp,bot, cur,conn
from importantFiles.config import adminId


from aiogram import types



def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    
    dp.register_message_handler(startBotHandlerAdmin, lambda call: call.data in adminId, commands="start")
    dp.register_message_handler(startBotHandlerUser, lambda call: call.data not in adminId, commands="start")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    pass


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    pass




def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    pass





def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)