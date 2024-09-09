from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesAdmin, dp,bot



#Нужно проверить, сохраняется ли путь к файлу в самом сообщении
async def acceptApplication(call: types.CallbackQuery):
    clientId = call.data.split("|")[-1]

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Допустить к обучению 📖", callback_data=f"admissionToTraining|{clientId}"))

    sendTextToClient = "Здравствуйте. Ваша заявка на вакансию одобрена. Свяжемся с Вами в ближайшее время."
    sendTextToAdmin = "Заявитель уведомлен"

    await call.message.edit_reply_markup(reply_markup=keyboard)
    await call.answer(sendTextToAdmin)


    await bot.send_message(chat_id=clientId, text=sendTextToClient)



async def admissionToTraining(call : types.CallbackQuery):
    clientId = call.data.split("|")[-1]

    sendTextToClient = "Вы допущены до обучения"
    sendTextToAdmin = "Пользователь допущен"


    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Начать тест", callback_data="startModule1"))



    await call.message.delete()
    await call.answer(sendTextToAdmin)




    await bot.send_message(chat_id=clientId, text=sendTextToClient, reply_markup=keyboard)





async def declineApplication(call: types.CallbackQuery):
    clientId = call.data.split("|")[-1]

    sendTextToClient = "Здравствуйте. Ваша заявка на вакансию отклонена."
    sendTextToAdmin = "Заявитель уведомлен"


    await call.message.delete()
    await call.answer(sendTextToAdmin)

    await bot.send_message(chat_id=clientId, text=sendTextToClient)




