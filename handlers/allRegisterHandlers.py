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


from handlers.userHandlers.testModules.module1 import module1Question1, module1Question2, module1Question3, module1Question4, module1Question5, module1Question6, module1Question7, module1Question8, module1Question9, module1Question10, module1Question11, startTestModule1



from adminHandlers.applicationsManagement.newApplications import acceptApplication, declineApplication, admissionToTraining
from adminHandlers.applicationsManagement.trainingApplications import declineTestModule1, acceptTestModule1

from adminHandlers.mainAdminHandler import editLink1, editLink2, editOnlineTestLinkH

def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    
    dp.register_message_handler(startBotHandlerAdmin, lambda msg: msg.from_user.id in adminId, commands="start")
    dp.register_message_handler(startBotHandlerUser, lambda msg: msg.from_user.id not in adminId, commands="start")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    pass


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    #Вступительный тест
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

    #Тест 1 модуль
    dp.register_callback_query_handler(startTestModule1, lambda call: call.data == "startModule1", state = StatesUser.EXPECTATION)

    dp.register_message_handler(module1Question1, content_types="text", state = StatesUser.MODULE1_1)
    dp.register_message_handler(module1Question2, content_types="text", state = StatesUser.MODULE1_2)
    dp.register_message_handler(module1Question3, content_types="text", state = StatesUser.MODULE1_3)
    dp.register_message_handler(module1Question4, content_types="text", state = StatesUser.MODULE1_4)
    dp.register_message_handler(module1Question5, content_types="text", state = StatesUser.MODULE1_5)
    dp.register_message_handler(module1Question6, content_types="text", state = StatesUser.MODULE1_6)
    dp.register_message_handler(module1Question7, content_types="text", state = StatesUser.MODULE1_7)
    dp.register_message_handler(module1Question8, content_types="text", state = StatesUser.MODULE1_8)
    dp.register_message_handler(module1Question9, content_types="text", state = StatesUser.MODULE1_9)
    dp.register_message_handler(module1Question10, content_types="text", state = StatesUser.MODULE1_10)
    dp.register_message_handler(module1Question11, content_types="text", state = StatesUser.MODULE1_11)


def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    dp.register_callback_query_handler(acceptApplication, lambda call: call.data.split("|")[0] == "accept", state = StatesAdmin.MAIN_MENU)
    dp.register_callback_query_handler(declineApplication, lambda call: call.data.split("|")[0] == "decline", state = StatesAdmin.MAIN_MENU)
    dp.register_callback_query_handler(admissionToTraining, lambda call: call.data.split("|")[0] == "admissionToTraining", state = StatesAdmin.MAIN_MENU)

    dp.register_callback_query_handler(declineTestModule1, lambda call: call.data.split("|")[0] == "declineModule1", state = StatesAdmin.MAIN_MENU)
    dp.register_callback_query_handler(acceptTestModule1, lambda call: call.data.split("|")[0] == "acceptModule1", state = StatesAdmin.MAIN_MENU)


    dp.register_message_handler(editLink1, commands="edit_channel_url_1", state = StatesAdmin.MAIN_MENU)
    dp.register_message_handler(editLink2, commands="edit_channel_url_2", state = StatesAdmin.MAIN_MENU)
    dp.register_message_handler(editOnlineTestLinkH, commands="edit_online_test_url", state = StatesAdmin.MAIN_MENU)






def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)