#import telebot
import telegram
from telegram.ext import Updater, CommandHandler
from bot_commands import *
import weather as wea

TOKEN='my_token'
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
