import telebot
import config
import random
import time
import urllib.request

from telebot import types
win = random.randint(1, 11)
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Посмотреть активность сайта')
    item2 = types.KeyboardButton('Выключить бота')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Бот включён", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def sm(message):
    if message.chat.type == 'private':
        if message.text == 'Посмотреть активность сервера':
            bot.send_message(message.chat.id, urllib.request.urlopen("http://www.www.youtube.com").getcode())

        elif message.text == 'Выключить бота':
            bot.send_message(message.chat.id, 'Бот выключен')
            time.sleep(1)
            bot.stop_bot()
        else:
            bot.send_message(message.chat.id, 'Я не понимаю вас, проверте текст на наличие ошибок')

bot.polling(none_stop=True)