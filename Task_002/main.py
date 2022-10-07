#import telebot
import telegram
from telegram.ext import Updater, CommandHandler
from bot_commands import *
import weather as wea

TOKEN='5766062444:AAFio0sBZ20a8Z-7ATc67j_xG_BNi39OMH8'
bot = telegram.Bot(token=TOKEN)

#print(bot.get_me())
updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('weather', get_weather))
updater.dispatcher.add_handler(CommandHandler('help', help))
#updater.dispatcher.add_handler(CommandHandler('video', get_video))


print('server start')
updater.start_polling()
updater.idle()