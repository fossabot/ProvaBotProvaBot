# -*- coding: utf-8 -*-
import telebot
import random
import requests
import base64
import os
import logging
import time
import urllib.request
import mmap
import os.path
import shutil
import sys
import json
from apiclient.discovery import build
from cryptography.fernet import Fernet
from telebot import types
from telebot import util
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
try:
    API=sys.argv[1]
except Exception as e:
    print("You must provide a telegram api key as argument")
user_dict={}
search_path =os.getcwd()
def risposta(sender, messaggio):
    bot.send_chat_action(sender.chat.id, action="typing")
    bot.send_message(sender.chat.id, messaggio)
lista_cartelle=["/videoporno","/fotoporno","/playmates","/strisce","/cibo","/xkcd"]
#check if folders exist
print("inizializzation, this may take a while...\n")
for x in lista_cartelle:
    if os.path.exists(search_path+x)==False:
     print("Manca la cartella "+x.replace("/","")+", la creo inserendoci un file .jpg vuoto")
     os.makedirs(search_path+x)
     if os.path.isfile(search_path+"/nope.jpg") ==False:
      urllib.request.urlretrieve("http://www.neacuho.org/resource/resmgr/EBoard_Photos/2015-2016/No_Image.jpg", "nope.jpg")
     shutil.copy2(search_path+"/nope.jpg",search_path+x)
lista_video_porno_mp4=[f for f in listdir(search_path+"/videoporno") if isfile(join(search_path+"/videoporno", f))]
lista_foto_porno=[f for f in listdir(search_path+"/fotoporno") if isfile(join(search_path+"/fotoporno", f))]
lista_playmate=[f for f in listdir(search_path+"/playmates") if isfile(join(search_path+"/playmates", f))]
lista_cibo=[f for f in listdir(search_path+"/cibo") if isfile(join(search_path+"/cibo", f))]
lista_strisce = [f for f in listdir(search_path+"/strisce") if isfile(join(search_path+"/strisce", f))]
lista_xkcd= [f for f in listdir(search_path+"/xkcd") if isfile(join(search_path+"/xkcd", f))]
if os.path.isfile(search_path+"/nope.jpg") ==True:
    os.remove(search_path+"/nope.jpg")
print("Done! The bot is ready and operative :)")
class User:
    def __init__(self):
        self.encmessage = None
        self.key=None
        self.message=None
@bot.message_handler(commands=["aiuto","start"])
def invia_comandi(message):
    print("aiuto")
    risposta(message,"""i comandi sono:
/insulta
/striscia
/playmate
/pornimg
/pornvid
/pornsrc
/cibo
/xkcd
/coinflip
/encrypt
/decrypt""")
@bot.callback_query_handler(func=lambda call: True)
def coinflip_callback(call):
 try:
    user=user_dict[call.message.chat.id]
    user.message=str(call.data)
    coinflip=["Testa","Croce"]
    if user.key==0:
        bot.edit_message_text(text="Volevi aver vinto qualcosa eh? Invece no",message_id=call.message.message.id,chat_id=call.message.chat.id)
    elif random.choice(coinflip)==user.message:
        user.key=user.key*2
        if str(user.key).endswith(".0"):
            user.key=int(user.key)
        try:
         bot.edit_message_text(text=call.from_user.first_name+" ha vinto "+str(user.key)+" euro", message_id=call.message.message_id,chat_id=call.message.chat.id)
        except Exception as e:
         if "400" in str(e):
             splitted_text=str(user.key)
             for text in splitted_text:
                 bot.send_message(call.message.chat.id,text)
         else:
                print(str(e)+" in funzione coinflip durante l'invio del messaggio all'utente ")
    else:
        user.key=0
        bot.edit_message_text(text=call.from_user.first_name+" ha perso tutto", message_id=call.message.message_id,chat_id=call.message.chat.id)
 except Exception as e:
     if e == ValueError:
      bot.edit_message_text(text=call.from_user.first_name+" ha inserito qualcosa che non doveva", message_id=call.message.message_id,chat_id=call.message.chat.id)
     else:
      print(str(e)+" in coinflip")
@bot.message_handler(commands=["encrypt"])
def informa(message):
    msg=bot.send_message(message.chat.id,"Inserisci un messaggio da criptare")
    bot.register_next_step_handler(msg,encode)
def encode(message):
    string=message.text
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(string.encode(encoding='UTF-8'))
    bot.send_message(message.chat.id,"Questo è il tuo messaggio criptato: ")
    try:
     bot.send_message(message.chat.id,cipher_text.decode(encoding='UTF-8'))
    except Exception as e:
     if "400" in str(e):
      splitted_text=util.split_string(cipher_text.decode(encoding='UTF-8'),3000)
      for text in splitted_text:
          bot.send_message(message.chat.id,text)
     else:
         print(str(e)+" in funzione encode")
    bot.send_message(message.chat.id,"Questa è la tua chiave crittografica")
    bot.send_message(message.chat.id,key)
@bot.message_handler(commands=['decrypt'])
def ottieni_messaggio(message):
    msg = bot.send_message(message.chat.id, "Invia il tuo messaggio")
    bot.register_next_step_handler(msg, ottieni_key)
def ottieni_key(message):
        encmessage = message.text
        user = User()
        user.encmessage=encmessage
        user_dict[message.chat.id] = user
        msg = bot.send_message(message.chat.id, 'Invia la key ricevuta insieme al messaggio criptato')
        bot.register_next_step_handler(msg, decripta_messaggio)
def decripta_messaggio(message):
    try:
        key = message.text
        user = user_dict[message.chat.id]
        user.key = key
        plain_text=Fernet(user.key.encode(encoding='UTF-8')).decrypt(user.encmessage.encode(encoding='UTF-8'))
        bot.send_message(message.chat.id,"Il messaggio decriptato è il seguente:")
        try:
            bot.send_message(message.chat.id,plain_text.decode(encoding='UTF-8'))
        except Exception as e:
         if "400" in str(e):
            splitted_text=util.split_string(plain_text.decode(encoding='UTF-8'))
            for text in splitted_text:
                bot.send_message(message.chat.id,text)
         else:
               print(str(e)+" in funzione decripta_messaggio")
    except Exception as e:
        risposta(message,'Si è verificato un errore, sicuro di aver copiato bene il messaggio?')
        print(str(e)+" in funzione decripta_messaggio")
@bot.message_handler(commands=["coinflip"])
def soldi_da_scommettere(message):
    print("coinflip")
    msg=bot.send_message(message.chat.id,"Quanti soldi vuoi scommettere?")
    bot.register_next_step_handler(msg,Testa_o_Croce)
def Testa_o_Croce(message):
   try:
    user = User()
    user_dict[message.chat.id] = user
    user.key=float(message.text)
    markup=types.InlineKeyboardMarkup()
    testa=types.InlineKeyboardButton("Testa",callback_data="Testa")
    croce=types.InlineKeyboardButton("Croce",callback_data="Croce")
    markup.row(testa)
    markup.row(croce)
    bot.send_message(chat_id=message.chat.id,text="Testa o Croce?",reply_markup=markup,parse_mode="Markdown")
   except ValueError:
    risposta(message,"Devi inserire un numero, non lettere! Riprova da capo con /coinflip")
@bot.message_handler(commands=["playmate"])
def invia_playmate(message):
 try:
    print("playmate")
    nome_file=(random.choice(lista_playmate))
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, open(search_path+"/playmates/"+nome_file,'rb'))
    nome_file=nome_file.replace(".jpg","")
    nome_file=nome_file[6:]
    bot.send_message(message.chat.id,nome_file)
 except Exception as e:
     risposta(message,"si è verificato un errore")
     print(str(e)+" in playmate")
@bot.message_handler(commands=["pornvid"])
def invia_video_porno(message):
    print("pornvid")
    bot.send_chat_action(message.chat.id, 'upload_video')
    try:
     bot.send_video(message.chat.id,open(search_path+"/videoporno/"+random.choice(lista_video_porno_mp4),'rb'))
    except requests.exceptions.ChunkedEncodingError:
        print("ChunkedEncodingError in pornvid")
        risposta(message,"Si è verificato un errore, contatta @Kaykin se vuoi/puoi, oppure riprova")
    except telebot.apihelper.ApiException:
        print("ApiException in pornvid")
        risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
@bot.message_handler(commands=["pornsrc"])
def cerca_porno(message,y=0):
 try:
  print("pornsrc")
  elenco_link=[]
  sito="http://www.xvideos.com/?k="
  messaggio=message.text.replace("/pornsrc","")
  if messaggio==("" or "@provabotprovabot"):
    risposta(message,"inserisici un termine da cercare insieme a /pornsrc")
  else:
    messaggio=messaggio.lower()
    messaggio=messaggio[1:]
    while True:
        conta=1
        if conta==1:
         if messaggio[-1:].isdigit():
             y=int(messaggio[-1:])
             messaggio=messaggio[:-1]
             conta=2
        if conta ==2:
           if messaggio[-1:].isdigit():
                y2=messaggio[-1:]
                y=(y+int(y2)*10)
                messaggio=messaggio[:-1]
        else:
            break
    messaggio_keyboard=messaggio
    if messaggio_keyboard.endswith(" "):
        messaggio_keyboard=messaggio_keyboard[:-1]
    messaggio=messaggio.replace(" ","+")
    sito+=messaggio
    sito2=sito+"&p=2"
    sito3=sito+"&p=3"
    sito4=sito+"&p=4"
    sito5=sito+"&p=5"
    def get_html(website):
     req = urllib.request.Request(website, headers={'User-Agent': 'Mozilla/5.0'})
     html = urllib.request.urlopen(req).read()
     soup= BeautifulSoup(html, 'html.parser')
     return soup
    soup1=get_html(sito)
    soup2=get_html(sito2)
    soup3=get_html(sito3)
    soup4=get_html(sito4)
    soup5=get_html(sito5)
    link_usabili_duplicati=[]
    link_usabili=[]
    lista_soup=[soup1,soup2,soup3,soup4,soup5]
    def ottieni_link_porno(soup):
     for link in soup.find_all('a'):
      elenco_link.append(link.get('href',messaggio))
      #ottiene elenco con link porno e duplicati
    for x in lista_soup:
        ottieni_link_porno(x)
        #ottiene l'elenco dei dei link senza duplicati
    for x in range(0,len(elenco_link)):
     if "/video" in elenco_link[x]:
        link_usabili_duplicati.append(elenco_link[x])
    for x in range(0,len(link_usabili_duplicati)):
        if link_usabili_duplicati[x] not in link_usabili:
            link_usabili.append(link_usabili_duplicati[x])
    if y<=len(link_usabili):
     risposta(message,"xvideos.com"+link_usabili[y])
    else:
        risposta(message,"L'indice specificato è maggiore di quanti sono i link trovati")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for x in range(0,len(link_usabili)):
        markup.add(str("/pornsrc "+messaggio_keyboard+ " "+str(x)))
    bot.reply_to(message, 'Ancora?', reply_markup=markup)
 except UnicodeEncodeError:
     risposta(message,"@Kaykin è un programmatore stupido e non sa implementare i caratteri unicode, come ad esempio 'è', quindi per adesso ti tocca aspettare, oppure vai direttamente su xvideos.com")
 except urllib.error.HTTPError:
     risposta(message,"http error, e @KayKin non sa il perché")
 except AttributeError:
     risposta(message,"Il programmatore delle api ha creato un bug con l'update 2.0 e @kaykin sta aspettando un fix perché è pigro e non ha voglia di correggerlo da solo")
@bot.message_handler(commands=["pornimg"])
def invia_immagine_porno(message):
    print("pornimg")
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id,open(search_path+"/fotoporno/"+random.choice(lista_foto_porno),'rb'))
    except:
     risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
@bot.message_handler(commands=["cibo"])
def invia_cibo(message):
    print("cibo")
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id, open(search_path+"/cibo/"+random.choice(lista_cibo),'rb'))
    except Exception as e:
      risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
      print(str(e)+" in cibo")
@bot.message_handler(commands=["striscia"])
def invia_striscia(message):
    print("striscia")
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id, open(search_path+"/strisce/"+random.choice(lista_strisce),'rb'))
    except Exception as e:
      risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
      print(str(e)+" in striscia")
@bot.message_handler(commands=["xkcd"])
def invia_xkcd(message):
    print("xkcd")
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id, open(search_path+"/xkcd/"+random.choice(lista_xkcd),'rb'))
    except Exception as e:
      risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
      print(str(e)+" in xkcd")
@bot.message_handler(commands=["insulta"])
def insulta(message):
 try:
        print("insulta")
        messaggio=message.text.replace("/insulta","")
        lista_insulti=["sei proprio una troia, " + messaggio, "caro, "+messaggio+" sei proprio una testa di cazzo", messaggio+" sei così spaventoso che quando caghi la tua stessa merda dice di fotterti!", messaggio+" sei come la minchia: sempre tra le palle", messaggio+" sei cosi brutto che chi ti guarda vomita", messaggio+", tua madre é peggio di un canestro da basket, gli entrano tutte le palle", messaggio+", io non capisco se sei cretino di tuo oppure ci hai studiato per esserlo", messaggio+",tua mamma ce l'ha così pelosa che per depilarsela deve chiamare la guardia forestale", messaggio+",come ti senti se ti dico che sei solo uno schizzo di sborra di tuo padre?", messaggio+",dall'alito sembra che ti si sia arenato il cadavere di un'orca in gola", messaggio+",sei cosi testa di cazzo che quando un'uomo pensa a te puo diventare gay!", messaggio+",tua madre è come Buffon, ha sempre palle tra le mani", messaggio+",prova a trattenere il respiro cinque minuti così tutti si accorgeranno che l'aria che respiriamo è migliorata"]
        if messaggio != "":
           risposta(message, random.choice(lista_insulti))
        else:
           risposta(message,"aggiungi un nome o qualcuno da insultare dopo il comando(ad esempio /insulta mario), coglione!")
 except Exception as e:
        print(str(e)+" in insulta")
#the following loop is made to prevent bot crashes, as they are very frequent
while True:
 try:
  bot.polling(none_stop=False)
 except Exception as e:
    print("ATTENZIONE ATTENZIONE ATTENZIONE \n \n \n "+str(e))
    continue
