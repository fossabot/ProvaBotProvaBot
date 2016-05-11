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
        self.encrypted_message = None
        self.key=None

@bot.message_handler(commands=["encrypt"])
def encode(message):
    string=message.text.replace("/encrypt","")
    key = Fernet.generate_key()
    print(key)
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(string.encode(encoding='UTF-8'))
    risposta(message,"Questo è il tuo messaggio criptato: ")
    risposta(message,cipher_text.decode(encoding='UTF-8'))
    risposta(message,"Questa è la tua chiave crittografica")
    risposta(message,key)

# Handle '/start' and '/help'
@bot.message_handler(commands=['decrypt'])
def ottieni_messaggio(message):
    chat_id = message.chat.id
    msg = bot.reply_to(message, "Invia il messaggio da decifrare")
    if message.text.replace("/decrypt")!="":
        encrypted_message=message.text.replace("/decrypt")
    else:
        bot.register_next_step_handler(msg, process_name_step)
def ottieni_key(message):
        chat_id = message.chat.id
        encrypted_message = message.text
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'key')
        bot.register_next_step_handler(msg, decifra)
def decifra(message):
        chat_id = message.chat.id
        key = message.text
        user = user_dict[chat_id]
        plain_text=Fernet(user.key.encode(encoding='UTF-8')).decrypt(user.encrypted_message.encode(encoding='UTF-8'))
        risposta(message,"Il messaggio decriptato è il seguente:")
        risposta(message,plain_text.decode(encoding='UTF-8'))
bot.polling()
