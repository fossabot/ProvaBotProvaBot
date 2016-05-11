# -*- coding: utf-8 -*-
import time

import telebot
from telebot import types
from cryptography.fernet import Fernet
def risposta(sender, messaggio):
    bot.send_chat_action(sender.chat.id, action="typing")
    bot.reply_to(sender, messaggio)


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
@bot.message_handler(commands=['help', 'start','decrypt'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am Example bot.
What's your message
""")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'key')
        bot.register_next_step_handler(msg, process_age_step)


def process_age_step(message):
        chat_id = message.chat.id
        age = message.text
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)

def process_sex_step(message):
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            raise Exception()
        plain_text=Fernet(user.name).decrypt(user.age.encode(encoding='UTF-8'))
        risposta(message,"Il messaggio decriptato è il seguente:")
        risposta(message,plain_text.decode(encoding='UTF-8'))
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
