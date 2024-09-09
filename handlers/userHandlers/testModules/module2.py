from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

import sys 
import os 
from datetime import datetime
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesUser, dp,bot, cur,conn

from importantFiles.config import RECIPIENT_APPLICATIONS


from utils.function.createFileApplicationPath import createFilePathToResultModule

from userHandlers import keyboard as kb





async def startModule2(call : types.CallbackQuery):
    sendText = "Вы продали клиенту главу 1 ВКР - распишите своими словами по шагам что вы будете делать с ним дальше?"

    await call.message.delete()

    await call.message.answer(sendText)
    await StatesUser.MODULE2_1.set()


async def module2Question1(message : types.Message, state:FSMContext):
    await state.update_data(question1 = message.text)

    sendText = "Вам автор скинул 2 главу ВКР (при условии, что клиент заказал у нас ВКР в сборе) - что вы с ней будете делать - опишите как вы поняли своими словами?"

    await message.answer(sendText)
    await StatesUser.MODULE2_2.set()


async def module2Question2(message : types.Message, state:FSMContext):
    await state.update_data(question2 = message.text)

    sendText = "Вам автор скинул курсовую работу в сборе - что вы с ней будете делать - опишите как вы поняли своими словами?"

    await message.answer(sendText)
    await StatesUser.MODULE2_3.set()


async def module2Question3(message : types.Message, state:FSMContext):
    await state.update_data(question3 = message.text)

    sendText = "Можно ли обмениваться с авторами работами с личного телефона / мессенджера?"

    await message.answer(sendText)
    await StatesUser.MODULE2_4.set()


async def module2Question4(message : types.Message, state:FSMContext):
    await state.update_data(question4 = message.text)

    sendText = "До какой цели вам нужно довести клиента?"

    await message.answer(sendText)
    await StatesUser.MODULE2_5.set()




async def module2Question5(message : types.Message, state:FSMContext):

    sendText = "Ваши ответы отправлены администратору. Ожидайте."
    await message.answer(sendText)

    await StatesUser.EXPECTATION.set()


    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
                InlineKeyboardButton("Допустить", callback_data=f"acceptModule2|{message.from_user.id}"),
                InlineKeyboardButton("Не допустить", callback_data=f"declineModule2|{message.from_user.id}")
                )
    async with state.proxy() as stateData:
        nameSurname = stateData["nameSurname"]
        phoneNumber = stateData["phoneNumber"]
        telegramUsername = stateData["username"]

        q1 = stateData["question1"]
        q2 = stateData["question2"]
        q3 = stateData["question3"]
        q4 = stateData["question4"]
        q5 = message.text



    answers = f"""
МОДУЛЬ 2

ФИО: {nameSurname}
Номер: {phoneNumber}
Телеграмм: @{telegramUsername}

Ответы:

1. {q1}
2. {q2}
3. {q3}
4. {q4}
5. {q5}
"""


    pathToFileModule1 = createFilePathToResultModule(message.from_user.id, Path("utils", "module1"))
    pathToFileModule2 = createFilePathToResultModule(message.from_user.id, Path("utils", "module2"))


    with open(pathToFileModule2, "w", encoding="utf-8") as writeFile:
        writeFile.write(answers)


    with open(pathToFileModule1, "rb") as module1:
        await bot.send_document(chat_id=RECIPIENT_APPLICATIONS, caption="Модуль 1", document=module1)

    with open(pathToFileModule2, "rb") as module2:
        await bot.send_document(chat_id=RECIPIENT_APPLICATIONS, caption="Модуль 2", document=module2, reply_markup=keyboard)