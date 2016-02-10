import requests
import base64
import sys
import os
import logging
import telegram
import time
import pycurl
import urllib.request
import mmap

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
bot = telegram.Bot(token='149991058:AAH5hdk1-oNXlwinJhhomxpGmfdTn10WlZo')
def controlla_aggiornamento():
    with open(search_path+'source.txt', 'rb', 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    #stringa da cercare
     if s.find(b"""<div class="coming_soon">""") != -1:
        print('true')
     else:
           #scrive un messaggio se il sito viene aggiornato
               bot.sendMessage(chat_id="@vivalacacca", text="c'è stato un aggiornamento su " + target)
               controllo=0
               exit()
        #seconda condizione, da rimuovere nel caso
     if s.find(b"100216") != -1:
        print('true')

     else:
   #scrive un messaggio se il sito viene aggiornato
       bot.sendMessage(chat_id="@vivalacacca", text="c'è stato un aggiornamento su " + target)
       controllo=0
       exit()

target = "www.adidas.it/yeezy"
controllo=1

if not target.startswith("http"):
    target = "http://" + target

if target.endswith("/"):
    target = target[:-1]
# da riciclare nel caso servisse   target_url = target + "/admin/Cms_Wysiwyg/directive/index/"

# Ask the user to enter the path
search_path = input("Enter directory path to search : ")
search_str = "<!-- page content last update : Tue, 09 Feb 2016 09:27:46 GMT -->"

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ):
        search_path = search_path + "/"

# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path ="."
while controllo==1:
 req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
 html = urllib.request.urlopen(req).read()
 file = open("source.txt", "wb")
 file.write(html)
 file.close()
 controlla_aggiornamento()
 time.sleep(60)
