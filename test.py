# -*- coding: utf-8 -*-
import time

import telebot
from telebot import types

API_TOKEN = '149991058:AAH5hdk1-oNXlwinJhhomxpGmfdTn10WlZo'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None
        self.key=None

@bot.message_handler(commands=["encrypt"])
def encode(message):
    string=message.text.replace("/encrypt","")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(string.encode(encoding='UTF-8'))
    risposta(message,"Questo è il tuo messaggio criptato: ")
    risposta(message,cipher_text.decode(encoding='UTF-8'))
    risposta(message,"Questa è la tua chiave crittografica")
    risposta(message,key)
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'decrypt'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am Example bot.
What's your message
""")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'what is ur key')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
     plain_text=Fernet(message.text).decrypt(name.encode(encoding='UTF-8'))
     risposta(message,"Il messaggio decriptato è il seguente:")
     risposta(message,plain_text.decode(encoding='UTF-8'))
    except Exception as e:
        bot.reply_to(message, 'oooops')



bot.polling()
