from aiogram.dispatcher import Dispatcher



import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser
from importantFiles.helps import StatesUser, StatesAdmin, dp,bot, cur,conn
from importantFiles.config import adminId


from aiogram import types





from handlers.userHandlers.questions import nameSurname, residenceCity, phoneNumber, telegramUsername, socialNetwork, salesExperience, workExperience, dismissalReason, noResult, currentWork, fastPrint, attitudeChange, currentPC, important, speedTraining, timeZone, onlineTestImg, acceptPolicyProcessPersonalData



from adminHandlers.applicationsManagement.newApplications import acceptApplication, declineApplication, admissionToTraining

def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    
    dp.register_message_handler(startBotHandlerAdmin, lambda msg: msg.from_user.id in adminId, commands="start")
    dp.register_message_handler(startBotHandlerUser, lambda msg: msg.from_user.id not in adminId, commands="start")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    pass


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    dp.register_message_handler(nameSurname, content_types="text", state = StatesUser.NAME_SURNAME)
    dp.register_message_handler(residenceCity, content_types="text", state = StatesUser.RESIDENCE_CITY)
    dp.register_message_handler(phoneNumber, content_types="text", state = StatesUser.PHONE_NUMBER)
    dp.register_message_handler(telegramUsername, content_types="text", state = StatesUser.TELEGRAM_USERNAME)
    dp.register_message_handler(socialNetwork, content_types="text", state = StatesUser.SOCIAL_NETWORK)
    dp.register_message_handler(salesExperience, content_types="text", state = StatesUser.SALES_EXPERIENCE)
    dp.register_message_handler(workExperience, content_types="text", state = StatesUser.WORK_EXPERIENCE)
    dp.register_message_handler(dismissalReason, content_types="text", state = StatesUser.DISMISSAL_REASON)
    dp.register_message_handler(noResult, content_types="text", state = StatesUser.NO_RESULT)
    dp.register_message_handler(currentWork, content_types="text", state = StatesUser.CURRENT_WORK)
    dp.register_message_handler(fastPrint, content_types="text", state = StatesUser.FAST_PRINT)
    dp.register_message_handler(attitudeChange, content_types="text", state = StatesUser.ATTITUDE_CHANGE)
    dp.register_message_handler(currentPC, content_types="text", state = StatesUser.CURRENT_PC)
    dp.register_message_handler(important, content_types="text", state = StatesUser.IMPORTANT)
    dp.register_message_handler(speedTraining, content_types="text", state = StatesUser.SPEED_TRAINING)
    dp.register_message_handler(timeZone, content_types="text", state = StatesUser.TIME_ZONE)
    dp.register_message_handler(onlineTestImg, content_types="photo", state = StatesUser.ONLINE_TEST_IMG)
    dp.register_callback_query_handler(acceptPolicyProcessPersonalData, lambda call: call.data == "acceptPolicy", state = StatesUser.ACCEPT_POLICY_PERSONAL_DATA)



def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    dp.register_callback_query_handler(acceptApplication, lambda call: call.data.split("|")[0] == "accept", state = StatesAdmin.MAIN_MENU)
    dp.register_callback_query_handler(declineApplication, lambda call: call.data.split("|")[0] == "decline", state = StatesAdmin.MAIN_MENU)
    dp.register_callback_query_handler(admissionToTraining, lambda call: call.data.split("|")[0] == "admissionToTraining", state = StatesAdmin.MAIN_MENU)





def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)