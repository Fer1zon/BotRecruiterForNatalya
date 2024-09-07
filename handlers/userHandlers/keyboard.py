from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


yes = KeyboardButton("Да")
no = KeyboardButton("Нет")

yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(yes, no)


sendApplications = InlineKeyboardButton("Я согласен(а). Подать заявку", callback_data="acceptPolicy")
sendApplicationsKb = InlineKeyboardMarkup().add(sendApplications)