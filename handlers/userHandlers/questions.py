from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import sys 
import os 
from datetime import datetime
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import StatesUser, dp,bot, cur,conn

from importantFiles.config import RECIPIENT_APPLICATIONS


from utils.function.createFileApplicationPath import createFilePath
from utils.function.JSONProcess import getOnlineTestLink

from userHandlers import keyboard as kb





async def nameSurname(message : types.Message, state:FSMContext):
    if len(message.text) > 80:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    

    await state.update_data(nameSurname = message.text)

    sendText = "Ваш город проживания"
    await message.answer(sendText)
    await StatesUser.RESIDENCE_CITY.set()


async def residenceCity(message:types.Message, state : FSMContext):
    if len(message.text) > 50:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(residenceCity = message.text)

    sendText = "Ваш номер телефона"

    await message.answer(sendText)
    await StatesUser.PHONE_NUMBER.set()



async def phoneNumber(message:types.Message, state : FSMContext):
    if len(message.text) > 40:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(phoneNumber = message.text)

    sendText = "Ник в телеграмм"

    await message.answer(sendText)
    await StatesUser.TELEGRAM_USERNAME.set()


async def telegramUsername(message:types.Message, state : FSMContext):
    if len(message.text) > 40:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(username = message.text)

    sendText = "Ссылка на социальную сеть(ВК, Инст и т.д.)"

    await message.answer(sendText)
    await StatesUser.SOCIAL_NETWORK.set()



async def socialNetwork(message:types.Message, state : FSMContext):
    if len(message.text) > 300:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(socialNetwork = message.text)

    sendText = "Опыт работы в продажах"

    await message.answer(sendText)
    await StatesUser.SALES_EXPERIENCE.set()


async def salesExperience(message:types.Message, state : FSMContext):
    if len(message.text) > 500:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(salesExperience = message.text)

    sendText = "В каких компаниях вы уже работали?"

    await message.answer(sendText)
    await StatesUser.WORK_EXPERIENCE.set()



async def workExperience(message:types.Message, state:FSMContext):
    if len(message.text) > 500:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(workExperience = message.text)


    sendText = "Причина (ы) увольнения с прошлого (ых) мест работы"

    await message.answer(sendText)
    await StatesUser.DISMISSAL_REASON.set()


async def dismissalReason(message:types.Message, state : FSMContext):
    if len(message.text) > 500:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(dismissalReason = message.text)


    sendText = "Вы прошли обучение но спустя несколько недель у Вас по-прежнему нет результатов, опишите Ваши действия?"

    await message.answer(sendText)
    await StatesUser.NO_RESULT.set()


async def noResult(message :types.Message, state : FSMContext):
    if len(message.text) > 500:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(noResult = message.text)

    sendText ="Рассматриваете данную вакансию как постоянное место работы или временное? Есть ли сейчас какая-то основная работа или учеба? Если есть учеба, то доп вопрос: как планируете совмещать? Нужно ли уходить в ученические? На какие оценки учитесь?"

    await message.answer(sendText)
    await StatesUser.CURRENT_WORK.set()


async def currentWork(message : types.Message, state : FSMContext):
    if len(message.text) > 500:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(currentWork = message.text)


    sendText = "Умеете быстро печатать?"

    await message.answer(sendText, reply_markup=kb.yes_no_keyboard)
    await StatesUser.FAST_PRINT.set()


async def fastPrint(message : types.Message, state:FSMContext):
    if len(message.text) > 100:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(fastPrint = message.text)

    sendText = "Как относитесь к изменениям? Насколько быстро вы их принимаете и адаптируетесь к ним?"

    await message.answer(sendText, reply_markup=types.ReplyKeyboardRemove())
    await StatesUser.ATTITUDE_CHANGE.set()


async def attitudeChange(message : types.Message, state : FSMContext):
    if len(message.text) > 300:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(attitudeChange = message.text)


    sendText = "Есть ли компьютер/ноутбук?"

    await message.answer(sendText, reply_markup=kb.yes_no_keyboard)
    await StatesUser.CURRENT_PC.set()

async def currentPC(message : types.Message, state : FSMContext):
    if len(message.text) > 100:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(currentPC = message.text)

    sendText = "Что для вас важно при сотрудничестве с нашей компанией?"

    await message.answer(sendText, reply_markup=types.ReplyKeyboardRemove())
    await StatesUser.IMPORTANT.set()


async def important(message : types.Message, state : FSMContext):
    if len(message.text) > 400:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(important = message.text)


    sendText = "Насколько быстро вы готовы обучиться и приступить к работе?"

    await message.answer(sendText)
    await StatesUser.SPEED_TRAINING.set()


async def speedTraining(message : types.Message, state : FSMContext):
    if len(message.text) > 300:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(speedTraining = message.text)

    sendText = "У вас московское время?"

    await message.answer(sendText, reply_markup=kb.yes_no_keyboard)
    await StatesUser.TIME_ZONE.set()



async def timeZone(message:types.Message, state:FSMContext):
    if len(message.text) > 100:
        return await message.answer("Текст слишком длинный. Попробуйте сократить количество не нужной информации.")
    
    await state.update_data(timeZone = message.text)


    sendText = f"""Для рассмотрения вашей кандидатуры важно пройти <a href = '{getOnlineTestLink()}'>опрос-собеседование</a> из 17 вопросов. Если вашу кандидатуру одобрят, то с вами свяжутся и вы получите доступ к обучению.
После прохождения теста отправьте в чат результат пройденного теста в формате скриншота."""

    await message.answer(sendText, reply_markup = types.ReplyKeyboardRemove(), disable_web_page_preview=True)
    await StatesUser.ONLINE_TEST_IMG.set()



async def onlineTestImg(message: types.Message, state: FSMContext):
    await state.update_data(onlineTestResult = message.photo[-1].file_id)

    sendText = "Для отправки заявки вам нужно подтвердить то что вы соглашаетесь с политикой обработки персональных данных👇"

    with open(Path("utils","messageContent","ППД.docx"), "rb") as sendFile:
        await message.answer_document(document=sendFile, caption=sendText, reply_markup=kb.sendApplicationsKb)

    await StatesUser.ACCEPT_POLICY_PERSONAL_DATA.set()



    












async def acceptPolicyProcessPersonalData(call : types.CallbackQuery, state :FSMContext):

    await call.message.delete()

    

    sendTextToUser = "Спасибо за ваши ответы! После ознакомления с вашей анкетой, мы свяжемся с вами и расскажем о дальнейших шагах."

    await call.message.answer(sendTextToUser)
    await StatesUser.EXPECTATION.set()


    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
                InlineKeyboardButton("Принять ✅", callback_data=f"accept|{call.from_user.id}"),
                InlineKeyboardButton("Отклонить ❌", callback_data=f"decline|{call.from_user.id}")
                )
    


    async with state.proxy() as stateData:
        nameSurname = stateData["nameSurname"]
        residenceCity = stateData["residenceCity"]
        phoneNumber = stateData["phoneNumber"]
        telegramUsername = stateData["username"]
        socialNetwork = stateData["socialNetwork"]
        salesExperience = stateData["salesExperience"]
        workExperience = stateData["workExperience"]
        dismissalReason = stateData["dismissalReason"]
        noResult = stateData["noResult"]
        currentWork = stateData["currentWork"]
        fastPrint = stateData["fastPrint"]
        attitudeChange = stateData["attitudeChange"]
        currentPC = stateData['currentPC']
        important = stateData["important"]
        speedTraining = stateData["speedTraining"]
        timeZone = stateData["timeZone"]
        onlineTestImg = stateData["onlineTestResult"]
    applicationText = f"""
Дата заполнения: {datetime.now()}
ФИО: {nameSurname}
Город проживания: {residenceCity}
Номер: {phoneNumber}
ТГ никнейм: @{telegramUsername}

Социальная сеть: {socialNetwork}

Опыт продаж: {salesExperience}

В компаниях работал(а): {workExperience}

Причина увольнений: {dismissalReason}

Реакция на отсутствие результата: {noResult}

Трудовой статус: {currentWork}

Умение быстро печатать: {fastPrint}

Отношение к изменениям: {attitudeChange}

Наличие ПК: {currentPC}

Важно при сотрудничестве: {important}

Возможность быстро обучиться: {speedTraining}

Московское время: {timeZone}
"""
    pathToNewFile = createFilePath(Path("utils","applications"))

    with open(pathToNewFile, "w", encoding="utf-8") as newFile:
        newFile.write(applicationText)

    onlineTestImgMessage = await call.message.answer_photo(photo=onlineTestImg)
    with open(pathToNewFile, "rb") as sendFile:
        await bot.send_document(chat_id = RECIPIENT_APPLICATIONS, document = sendFile, reply_markup=keyboard, reply_to_message_id=onlineTestImgMessage.message_id)
    
    

