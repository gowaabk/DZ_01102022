from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from spy import *
import weather as wea

# import youtube as ytb


def start(update: Update, context: CallbackContext):
    log(update, context)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Что требуется холопу? (/help)"
    )


def get_weather(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    city = msg.split()[1]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wea.find_weather(city)
    )


def help(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        "/start - Начало работы\n/weather - запрос погоды (/weather Москва)\n/help - справка"
    )


# def get_video(update: Update, context: CallbackContext):
#     log(update, context)
#     msg = update.message.text
#     adress_video = msg.split()[1]
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text=ytb.find_weather(adress_video))
