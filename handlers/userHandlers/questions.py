from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import sys 
import os 
from datetime import datetime
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import RECIPIENT_APPLICATIONS


from utils.function.createFileApplicationPath import createFilePath



#TODO write the other questions







async def acceptPolicyProcessPersonalData(call : types.CallbackQuery, state :FSMContext):

    await call.message.delete()

    async with state.proxy() as stateData:
        pass
        #ALL DATA

    sendTextToUser = "Спасибо за ваши ответы! После ознакомления с вашей анкетой, мы свяжемся с вами и расскажем о дальнейших шагах."

    await call.message.answer(sendTextToUser)
    await States.EXPECTATION.set()


    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
                InlineKeyboardButton("Принять", callback_data=f"accept|{call.from_user.id}"),
                InlineKeyboardButton("Отклонить ❌", callback_data=f"decline|{call.from_user.id}")
                )
    
    applicationText = f"""
...
Дата заполнения: {datetime.now()}
ФИО: ...
"""
    pathToNewFile = createFilePath(Path("utils","applications"))

    with open(pathToNewFile, "w", encoding="utf-8") as newFile:
        newFile.write(applicationText)


    with open(pathToNewFile, "rb") as sendFile:
        await bot.send_document(chat_id = RECIPIENT_APPLICATIONS, document = sendFile, reply_markup=keyboard)
    
    

