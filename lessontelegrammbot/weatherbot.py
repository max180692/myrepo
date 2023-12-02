import telebot
from telebot import types
import settings
from registruser import RegisterUser
import collections

collection_user = collections.ChainMap()
list_user = [collection_user,]
bot = telebot.TeleBot(settings.API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in list(collection_user.values()):
        print('non')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Моя первая кнопка')
        button2 = types.KeyboardButton('Моя вторая кнопка')
        markup.add(button1,button2)
        bot.send_message(message.from_user.id,'Выберите какую кнопку нажать! ',reply_markup=markup)
    else:
        reg_user = RegisterUser()
        reg_user.set_user_info(message.from_user.first_name,message.from_user.id)
        list_user[0] = list_user[0].new_child(reg_user.get_info_user())
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('start')
        markup.add(button)
        bot.send_message(message.from_user.id,f'{message.from_user.first_name}  вы зарегистрированы.   Выберите какую кнопку нажать! ',reply_markup=markup2)
        

@bot.message_handler(content_types=['text'])
def answer_on_message(message):
    print(list_user)
    if message.text.lower() == 'моя первая кнопка':
        bot.send_message(message.from_user.id,'Вы нажали на кнопку номер 1')
    elif message.text.lower() == 'моя вторая кнопка':
        bot.send_message(message.from_user.id,'вы нажали на кнопку номер 2')


bot.polling()

