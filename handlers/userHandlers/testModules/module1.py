from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

import sys 
import os 
from datetime import datetime
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesUser, dp,bot 

from importantFiles.config import RECIPIENT_APPLICATIONS


from utils.function.createFileApplicationPath import createFilePathToResultModule

from userHandlers import keyboard as kb





async def startTestModule1(call : types.CallbackQuery):
    sendText = "Какие базовые вопросы надо задать каждому клиенту для выявления потребности?"

    await call.message.delete()

    await call.message.answer(sendText)
    await StatesUser.MODULE1_1.set()


async def module1Question1(message : types.Message, state :FSMContext):
    await state.update_data(question1 = message.text)

    sendText = "Какие  дополнительные требования нужно уточнить для работы связанной с программированием?"

    await message.answer(sendText)
    await StatesUser.MODULE1_2.set()


async def module1Question2(message : types.Message, state : FSMContext):
    await state.update_data(question2 = message.text)

    sendText = "Какие  дополнительные требования нужно уточнить для работы по технической специальности?"

    await message.answer(sendText)
    await StatesUser.MODULE1_3.set()


async def module1Question3(message : types.Message, state : FSMContext):
    await state.update_data(question3 = message.text)

    sendText = "Если клиент пишет, что ему нужна курсовая на 60 страниц - по какому прайсу будем ему считать стоимость"

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(KeyboardButton("Как за курсовую"), KeyboardButton("Как за ВКР бакалавра"))

    await message.answer(sendText, reply_markup=keyboard)
    await StatesUser.MODULE1_4.set()



async def module1Question4(message : types.Message, state : FSMContext):
    await state.update_data(question4 = message.text)

    sendText = "Чем антиплагиат.ру (бесплатная версия) отличается от антиплагиат.вуз (это платная версия антиплагиат.ру)?"

    await message.answer(sendText, reply_markup=types.ReplyKeyboardRemove())
    await StatesUser.MODULE1_5.set()


async def module1Question5(message : types.Message, state : FSMContext):
    await state.update_data(question5 = message.text)

    sendText = "Что такое дожим? (поясните + приведите пример как он может выглядеть - как вы поняли)"

    await message.answer(sendText)
    await StatesUser.MODULE1_6.set()


async def module1Question6(message : types.Message, state : FSMContext):
    await state.update_data(question6 = message.text)

    sendText = "Можно ли писать клиентам с личного аккаунта в мессенджере?"

    await message.answer(sendText, reply_markup=kb.yes_no_keyboard)
    await StatesUser.MODULE1_7.set()


async def module1Question7(message : types.Message, state : FSMContext):
    await state.update_data(question7 = message.text)

    sendText = "Если клиент пишет, что ему нужна оригинальность по антиплагиату 100% - вы примете у него для расчета данное требование?"

    await message.answer(sendText, reply_markup=types.ReplyKeyboardRemove())
    await StatesUser.MODULE1_8.set()


async def module1Question8(message : types.Message, state : FSMContext):
    await state.update_data(question8 = message.text)

    sendText = "Как вы можете показать клиенту экспертность компании? (приведите пример)"

    await message.answer(sendText)
    await StatesUser.MODULE1_9.set()


async def module1Question9(message : types.Message, state : FSMContext):
    await state.update_data(question9 = message.text)

    sendText = "Как нужно открывать и закрывать смену?"

    await message.answer(sendText)
    await StatesUser.MODULE1_10.set()


async def module1Question10(message : types.Message, state : FSMContext):
    await state.update_data(question10 = message.text)

    sendText = "Что нужно скинуть клиенту после внесения первой предоплаты?"

    await message.answer(sendText)
    await StatesUser.MODULE1_11.set()


async def module1Question11(message : types.Message, state : FSMContext):
    await state.update_data(question11 = message.text)

    sendText = "Ваши ответы отправлены администратору. Ожидайте."
    await message.answer(sendText)

    await StatesUser.EXPECTATION.set()




    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
                InlineKeyboardButton("Принять ✅", callback_data=f"acceptModule1|{message.from_user.id}"),
                InlineKeyboardButton("Отклонить ❌", callback_data=f"declineModule1|{message.from_user.id}")
                )
    async with state.proxy() as stateData:
        nameSurname = stateData["nameSurname"]
        phoneNumber = stateData["phoneNumber"]
        telegramUsername = stateData["username"]

        q1 = stateData["question1"]
        q2 = stateData["question2"]
        q3 = stateData["question3"]
        q4 = stateData["question4"]
        q5 = stateData["question5"]
        q6 = stateData["question6"]
        q7 = stateData["question7"]
        q8 = stateData["question8"]
        q9 = stateData["question9"]
        q10 = stateData["question10"]
        q11 = stateData["question11"]

    answers = f"""
МОДУЛЬ 1

ФИО: {nameSurname}
Номер: {phoneNumber}
Телеграмм: @{telegramUsername}

Ответы:

1. {q1}
2. {q2}
3. {q3}
4. {q4}
5. {q5}
6. {q6}
7. {q7}
8. {q8}
9. {q9}
10. {q10}
11. {q11}
"""
    
    pathToFile = createFilePathToResultModule(message.from_user.id, Path("utils", "module1"))

    with open(pathToFile, "w", encoding="utf-8") as writeFile:
        writeFile.write(answers)

    with open(pathToFile, "rb") as sendFile:
        await bot.send_document(chat_id=RECIPIENT_APPLICATIONS, document=sendFile, reply_markup=keyboard, caption="Результаты тестирования. 1 модуль")

    
        







