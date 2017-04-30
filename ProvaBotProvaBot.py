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
    print("You must provide a telegram api key as the first argument")
bot = telebot.TeleBot(API)
user_dict={}
search_path =os.getcwd()
def risposta(sender, messaggio):
    bot.send_chat_action(sender.chat.id, action="typing")
    bot.send_message(sender.chat.id, messaggio)
lista_cartelle=["/playmates","/strisce","/cibo","/xkcd"]
#check if folders exist
print("inizializzation, this may take a while...\n")
for x in lista_cartelle:
    if os.path.exists(search_path+x)==False:
     print("Manca la cartella "+x.replace("/","")+", la creo inserendoci un file .jpg vuoto")
     os.makedirs(search_path+x)
     if os.path.isfile(search_path+"/nope.jpg") ==False:
      urllib.request.urlretrieve("http://www.neacuho.org/resource/resmgr/EBoard_Photos/2015-2016/No_Image.jpg", "nope.jpg")
     shutil.copy2(search_path+"/nope.jpg",search_path+x)
lista_playmate=[f for f in listdir(search_path+"/playmates") if isfile(join(search_path+"/playmates", f))]
lista_cibo=[f for f in listdir(search_path+"/cibo") if isfile(join(search_path+"/cibo", f))]
lista_strisce = [f for f in listdir(search_path+"/strisce") if isfile(join(search_path+"/strisce", f))]
lista_xkcd= [f for f in listdir(search_path+"/xkcd") if isfile(join(search_path+"/xkcd", f))]
if os.path.isfile(search_path+"/nope.jpg") ==True:
    os.remove(search_path+"/nope.jpg")
print("Done! The bot is ready and operative :)")
class User:
    def __init__(self):
        self.encmessage=None
        self.key=None
        self.message=None
        self.name=None
        self.money=None
@bot.message_handler(commands=["aiuto","start"])
def invia_comandi(message):
    print("aiuto")
    risposta(message,"""i comandi sono:
/insulta
/striscia
/playmate
/pornsrc
/cibo
/xkcd
/coinflip
/citazione
/encrypt
/decrypt""")
@bot.message_handler(commands=["citazione"])
def invia_citazione(message):
    print("citazione")
    elenco_citazioni_himym=["""Ma dico sei impazzita? Questo comporterebbe che io parlassi con una donna con cui sono già andatto a letto, il che francamente è un po' come cambiare l'olio a un'auto a noleggio""","""Puoi aspettare un mese per il sesso solo se la tua ragazza ha 17 anni e 11 mesi""","""Se una ragazza è una ex-fidanzata di un fratello, lei è off-limits per sempre fino alla fine dei tempi. Ricorda sempre: con la ex di un fratello non fare il porcello""", """Robin: Non posso credere
 che la mia sorellina voglia perdere la verginità con un pivello con quella crestina orribile in testa! Non è possibile! Dovete aiutarmi a dissuaderla.\nMarshall: Argomenti per convincere una ragazza a non fare sesso...\nTed: Io non ne ho nel database!
Barney: Dissuadere dal fare sesso è contro la mia religione!""", "Una bugia è solo una grande storia che qualcuno ha rovinato﻿ con la verità!", """Lily Aldrin: «Ehi, genio del diritto! Sei pronto a prenderti una pausa di un quarto d'ora!».
Marshall Eriksen: «Scusa tesoro, devo lavorare e ho bisogno che il sangue vada qui»""", """Ho solo tre cose per cui combatterei: il gancio ostinato di un reggiseno, le accuse di molestia sessuale, tutte scampate, ed infine l'impulso di vomitare quando vedo un uomo che indossa scarpe marroni con un completo nero","A volte la vita va così, scolleghi il cervello per una sera e al mattino ti trovi stroncato dai postumi di una sbornia, con una caviglia slogata e un ananas. Ah.. Non si scopri mai come
fosse arrivato sul mio comodino ma... era molto buono!""","""Marshall Eriksen: «Sono gnocche!».
Barney Stinson: «Uh! Avete ancora tanto da imparare! Voi praticamente siete delle vittime dell'Effetto Cheerleader. Grazie della domanda! L'Effetto Cheerleader c'è quando alcune donne sembrano gnocche ma solamente se sono in gruppo. Lo stesso per le Cheerleader. Sembrano delle gnocche ma se poi andiamo a vederle individualmente sono delle gran cozze!».""", "Ah ti prego, tanto è il solito film, non ne posso più! I ragazzi sono come il metrò, se ne perdi uno, tempo 5 minuti ne passa un altro!",
 """Frena! Ci sono solo due motivi per rivederti con una che hai scaricato:\n1. tette\n2. tette finte""", """Barney Stinson: «Sapete perchè amo Halloween? Le ragazze tirano fuori la Pamela Anderson che è in loro almeno per una sera! Se una si veste da strega diventa una sexy strega, se una si da gatta diventa una sexy gatta, da infermiera...».\nLily Aldrin: «Barney si è capito!».
Barney Stinson: «...Una sexy infermiera»\nRobin Scherbatsky: «Scusa come può un costume da zucca essere sexy?».
Ted Mosby: «Basta solo tagliarlo nei punti strategici»""", """Barney Stinson: «...E' il bello dell'essere sbronzi, si fanno cose che non da sobri uno non farebbe mai».
Lily Aldrin: «Lo dicono anche quelle che sono venute a letto con te! Cinque?»""", """Trudy: «Sto uscendo da un brutto periodo e forse dovrei fare qualcosa di stupido!».
Ted Mosby: «Io sono stupido, potresti farti me!»""", "Ragazzi spesso la vita ci offre momenti belli e romantici che la rendono degna di essere vissuta ma c'è un problema: quei momenti passano.. e nascosta dietro l'angolo c'è una strega brutta, cattiva e con i capelli crespi che si chiama realtà", """Ted Mosby: «Ehi Robyn, Marshall ti ha guardato il culo!».
Robin Scherbatsky: «Mi ha guardato il sedere? Beh, ringrazialo perchè oggi mi sentivo poco interessante!»""", """Marshall Eriksen: «Hai su il push-up o no?».
Lily Aldrin: «Hai fatto la lampada ai polpacci?».
Marshall Eriksen: «Ritiro la domanda»""", """obin Scherbatsky: «Quando è morta mia nonna mi sono fatta bionda!».
Lily Aldrin: «Oh! Due tragedie in un giorno solo!»""", """Barney Stinson: «Ted, le ragazze trovano sexy gli architetti. Pensaci, tu credi qualcosa dal nulla Sei come Dio. E non c'è niente di più attraente di Dio!».
Ted Mosby: «Hai studiato le sacre scritture?»""", """Marshall Eriksen: «Due ragazzi che sono amici non posso fare il brunch?».\nTed Mosby: «Perchè è una cosa poco...».\nRobin Scherbatsky: «Virile!».
Marshall Eriksen: «Non lo è? La colazione invece si, e il pranzo anche. Perchè il brunch non lo è?».
Ted Mosby: «Non lo so! Un cavallo non è strano e non lo è nemmeno un corno mse se li metti insieme hai l'unicorno!»""", """Ragazzi, guardate bene questa faccia perchè la prossima volta che l'avrete davanti sarà sfigurata in modo assolutamente sexy! Questa è la mia natura, sono un uomo, adoro combattere, fare a pugni e lordarmi tutto....... me l'appendi così non si stropiccia?""" ]
    elenco_citazioni_tbbt=["""Da quel che so, il sesso non ha avuto aggiornamenti con grafica ad alta definizione e armamenti potenziati!""", "Signore e signori, mentre il signor Kimi in virtù della sua giovinezza e della sua ingenuità è caduto preda dell'inesplicabile bisogno di contatto umano, posso rassicurarvi sul fatto che la mia ricerca continuerà senza interruzione e che le relazioni umane continueranno a sconcertarmi e a farmi schifo. Grazie!","""Sheldon: A volte dimentico che gli altri
    hanno dei limiti. E’ così triste""", """Sheldon: Cosa avevi di più importante della serata Wii-Bowling?\nLeonard: In realtà ero..\nSheldon: Era una domanda retorica, niente è più importante della serata Wii-Bowling""", """Sheldon: E se alla fine si ritrovasse con un bambino che non saprà se usare un integrale o un differenziale per trovare l´area sottesa da una curva?\nLeonard: Sono sicuro che lo amerebbe ugualmente.
Sheldon: Io non lo amerei""", """Penny: Scusami, hai provato a costruire una macchina per la TAC?
Sheldon: Non ci ho provato, ci sono riuscito. Per un attimo ho visto l’interno del criceto di mia sorella, Palla di Neve, prima che prendesse fuoco. Questo generò una curiosa espressione a casa nostra, una palla di neve non ha speranza in una TAC""", """Sheldon: Sai qual e’, dal punto di vista statistico, la causa di morte piu’ probabile alla mia eta’?
Leonard: Per mano del tuo coinquilino?\nSheldon: Un incidente.\nLeonard: E’ cosi’ che lo faro’ sembrare…""", """Sheldon: Amy, mi stavo chiedendo se dovremmo effettivamente indulgere al coito almeno una volta nella nostra relazione.
Bazinga.""", """Page: Sono l’Agente Speciale Page, FBI.\nSheldon: Lei dice di essere l’Agente Speciale Page dell’FBI.\nPage: Ecco il mio distintivo.
Sheldon: Ed ecco il mio…tesserino di membro della Justice League. Ma questo non prova che io conosca Batman""", """Leonard: No, sul serio, credo di aver finalmente capito qual e’ il mio problema con le donne.
Sheldon: Il capibara e’ il piu’ grande esemplare della famiglia dei roditori.\nLeonard: E questo cosa c’entra con i miei problemi con le donne?
Sheldon: Niente. Era un tentativo disperato di proporre un argomento alternativo""", "Sheldon: Gesù, invece, in realtà è nato in estate. Il giorno della sua nascita è stato spostato per coincidere con la tradizionale ricorrenza pagana in cui si celebrava il solstizio d’inverno accendendo fuochi e sgozzando capretti. Il che, a dirla tutta, sembra molto piu’ divertente di dodici ore in chiesa con mia madre, seguite da una semplice torta di frutta secca", """Howard: E tu pensi di poter sopportare
 Sheldon?\nRaj: Beh, sono Hindu. La mia religione mi insegna che se soffrirò in questa vita sarò ricompensato nella prossima. Tre mesi al Polo Nord con Sheldon e rinascerò come un miliardario superdotato con le ali""", """Leonard: Ok, hai davvero bisogno della tessera di membro onorario della Justice League of America?
Sheldon: E’ stata in tutti i miei portafogli da quando avevo cinque anni.\nLeonard: Perchè?\nSheldon: Dice: “Tenere sempre con sé”. E’ proprio qui, sotto l’autografo di Batman""", """Penny: Sheldon, cosa vuoi?\nSheldon: Una Coca Cola Light.\nPenny: Per favore, puoi ordinare un cocktail? Devo fare pratica con gli alcolici!\nSheldon:Va bene. Prendo un Virgin Cuba Libre.\nPenny: Cioè rum e coca senza il rum.\nSheldon: Si.\nPenny: Quindi… Coca.
Sheldon: Si. Me la faresti light?""", """Sheldon: Sai come faccio a sapere che non siamo dentro Matrix?
Leonard: Come?\nSheldon: Se lo fossimo, il cibo sarebbe migliore""", """Penny: Senti, perchè non ti compriamo questo robot e ce ne andiamo a casa?\nSheldon: Voglio quello lì.\nPenny: Ok, puoi avere quello.\nLeonard: Oh, ma andiamo… Ci giocherà due volte e poi finirà nell’armadio con tutte le altre cianfrusaglie.\nPenny: Compragli quel robot, Leonard!\nSheldon: Posso prendere anche questo fumetto?\nPenny: Certo che puoi.""", "Sheldon: Che computer possiede? E la prego non mi dica “uno bianco”",
"""Leonard:Quindi l’intera comunita’ scientifica deve crederti sulla parola?\n Sheldon: Non devono, ma dovrebbero.""", """Sheldon: Invece di una centrifuga al titanio, i miei genitori mi regalarono… E’ difficile da dire… Mi regalarono… una mini-moto da cross.\nPenny: No!\nSheldon: Quale ragazzino di 12 anni vorrebbe mai una mini-moto da cross?\nPenny:Tutti?"""]
    random_himym=random.choice(elenco_citazioni_himym)+"""
Da How I met your mother"""
    random_tbbt=random.choice(elenco_citazioni_tbbt)+"""
Da The big bang theory"""
    elenco_citazioni_random=[random_tbbt,random_himym]
    risposta(message,random.choice(elenco_citazioni_random))
@bot.callback_query_handler(func=lambda call: True)
def coinflip_callback(call):
 try:
    user=user_dict[call.message.chat.id]
    user.message=str(call.data)
    if(call.from_user.first_name==user.name): #avoid other people in groups to be able to click your buttons
     coinflip=["Testa","Croce"]
     if (user.money==0):
        bot.edit_message_text(text="Volevi aver vinto qualcosa eh? Invece no",message_id=call.message.message_id,chat_id=call.message.chat.id)
     elif random.choice(coinflip)==user.message:
        user.money=user.money*2
        if str(user.money).endswith(".0"):
            user.money=int(user.money)
        try:
         bot.edit_message_text(text=call.from_user.first_name+" ha vinto "+str(user.money)+" euro", message_id=call.message.message_id,chat_id=call.message.chat.id)
        except Exception as e:
         if "400" in str(e):
             splitted_text=str(user.money)
             for text in splitted_text:
                 bot.send_message(call.message.chat.id,text)
         else:
                print(str(e)+" in funzione coinflip durante l'invio del messaggio all'utente ")
     else:
        bot.edit_message_text(text=call.from_user.first_name+" ha perso tutto", message_id=call.message.message_id,chat_id=call.message.chat.id)
     user.money=0 #reset to avoid betting from old buttons
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
    user.money=float(message.text)
    user.name=message.from_user.first_name
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
     risposta(message,"Il programmatore delle api di questo bot ha creato un bug con l'update 2.0 e @kaykin sta aspettando un fix perché è pigro e non ha voglia di correggerlo da solo")
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
        lista_insulti=[messaggio+" sei come la minchia: sempre tra le palle",messaggio+" quando Dio diede l'intelligenza all'umanità tu dov'eri? Al cesso!?",messaggio+" sei cosi brutto che chi ti guarda vomita",messaggio+" sei cosi scemo che guardi pure peppa pig."+messaggio+" tua madre é peggio di un canestro da basket, gli entrano tutte le palle",messaggio+" sei così brutto che quando sei nato tua mamma ha inviato i biglietti di scuse a tutti."+messaggio+""" di solito si dice Scusate le
        spalle.. tu invece devi dire "Scusate la faccia!""",messaggio+" tua mamma ce l'ha così pelosa che per depilarsela deve chiamare la guardia forestale",messaggio+" come ti senti se ti dico che sei solo uno schizzo di sborra di tuo padre?",messaggio+" di a tua madre di smettere di cambiare rossetto! Ho il pisello che sembra un arcobaleno!",messaggio+" lo sai perchè sulla bandiera della Mongolia c'é la tua faccia? Perché sei il re dei mongoloidi",messaggio+""" dall'alito sembra che ti sia
        arenato il cadavere di un' orca in gola""",messaggio+" sei cosi brutto ma cosi brutto che tua mamma appena ti ha fatto pensava che fossi uscito dal culo",messaggio+" le tue gambe sono così pelose che per farti la ceretta devi affittare un tagliaerba",messaggio+" tua madre è come Buffon, ha sempre palle tra le mani", messaggio+" sai contare fino ad un trilione? Allora prima di parlare.. comincia la conta!",messaggio+""" prova a trattenere il respiro cinque minuti così tutti si
        accorgeranno che l'aria che respiriamo è migliorata""",messaggio+" se Dio ha creato l'ignoranza protesta, perchè ne sei l'unico beneficiario",messaggio+" meglio se non pensi, altrimenti il tuo cervello va in carenza d'ossigeno",messaggio+" sai che cos'è una disgrazia? Conoscerti e incontrarti"]
        if messaggio != "":
           risposta(message, random.choice(lista_insulti))
        else:
           risposta(message,"aggiungi un nome o qualcuno da insultare dopo il comando(ad esempio /insulta mario), coglione!")
 except Exception as e:
        print(str(e)+" in insulta")
#the following loop has been made to prevent bot crashes, as they are very frequent
while True:
 try:
  bot.polling(none_stop=False)
 except Exception as e:
    print("ATTENZIONE ATTENZIONE ATTENZIONE \n \n \n "+str(e))
    continue
