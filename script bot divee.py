import telebot
import random
import requests
import base64
import sys
import os
import logging
import time
import urllib.request
import mmap
import ssl
import os.path
import botan
import shutil
from cryptography.fernet import Fernet
from telebot import types
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
bot = telebot.TeleBot('149991058:AAH5hdk1-oNXlwinJhhomxpGmfdTn10WlZo')
botan_token='11tcT_JQrMxklU2NntbWEI32FbY40vfS'
user_dict={}
search_path =os.getcwd()
        # Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ):
                search_path = search_path + "/"
botan_token = '2PcvvgRcYce75mDj7q2M8_Gd7BGb3-YW' # Token got from @botaniobot
def risposta(sender, messaggio):
    bot.send_chat_action(sender.chat.id, action="typing")
    bot.send_message(sender.chat.id, messaggio)
lista_cartelle=["/videoporno","/fotoporno","/playmates","/strisce","/cibo"]
#check if folder exists
for x in lista_cartelle:
    if os.path.exists(search_path+x)==False:
     print("Manca la cartella "+x.replace("/","")+", la creo inserendoci un file .jpg vuoto")
     os.makedirs(search_path+x)
     shutil.copy2(search_path+"/nope.jpg",search_path+x)
lista_video_porno_mp4=[f for f in listdir(search_path+"/videoporno") if isfile(join(search_path+"/videoporno", f))]
lista_foto_porno=[f for f in listdir(search_path+"/fotoporno") if isfile(join(search_path+"/fotoporno", f))]
lista_playmate=[f for f in listdir(search_path+"/playmates") if isfile(join(search_path+"/playmates", f))]
lista_cibo=[f for f in listdir(search_path+"/cibo") if isfile(join(search_path+"/cibo", f))]
lista_strisce = [f for f in listdir(search_path+"/strisce") if isfile(join(search_path+"/strisce", f))]
class User:
    def __init__(self):
        self.encmessage = None
        self.key=None
        self.message=None
@bot.message_handler(commands=["citazione"])
def invia_citazione(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    elenco_citazioni_himym=["""Ted: Ragazzi, sto per raccontarvi una storia incredibile. La storia di come ho conosciuto vostra madre!
Figlio di Ted: Abbiamo fatto qualche cosa di male?
Ted: No!
Figlia di Ted: E senti, ci vorrà molto?
Ted: Sì. Venticinque anni fa, prima che diventassi papà, la mia vita era diversa...""", "Sì! Perfetto. Così sarai fidanzato, stapperai lo champagne, farai un brindisi e farai sesso sul pavimento! No, non farlo sul pavimento...", "Ragazzi, una cosa che imparerete è che non si finisce mai di conoscere la persona con cui si sta. Tutti abbiamo dei segreti, alcuni piacevoli, altri meno piacevoli, altri invece sono strani", "Una cosa che ho imparato quell'estate è l'inizio di un amore e la fine di un amore per i primi trenta giorni sono incredibilmente simili. Tanto per cominciare passi un sacco di tempo a letto, i tuoi amici non ti sopportano più e giri perennemente in mutande" , "Il baseball, le spogliarelliste, le armi possono anche aiutare, ma l'unica cosa che può guarire un cuore spezzato è il tempo", "Verso i trenta si ha ormai un discreto numero di relazioni alle spalle, ma con la persona con cui si sta si finge che non sia così", "Sfida accettata!", "Lo conosci Ted?", "Sai perché non hai dimenticato Lily? Perché te la ricordi ancora nuda. Non puoi dimenticare una donna finché ti ricordi ancora le sue tette: è un dato scientifico. Il cervello del maschio medio può immagazzinare solo un numero limitato di immagini di tette o di meloni... e il tuo disco rigido è saturo di quelle di Lily" , "Ora ti spiegherò il mio sistema per far sì che la mente controlli il corpo. Vedi, tutte le volte che mi sento male, dico al mio corpo che è soltanto un eccesso di splendore e funziona!","Le uniche gnocche che cercano su Internet un uomo, o sono pazze o sono prostitute o sono maschi","Una ragazza può essere pazza purché però sia altrettanto gnocca. Se è pazza tanto così, sarà tanto così gnocca. Se è pazza tanto così, sarà tanto così gnocca. Una ragazza non deve trovarsi al di sotto di questa riga nota anche come diagonale di Vicky-Mendoza", "Ma dico sei impazzita? Questo comporterebbe che io parlassi con una donna con cui sono già andatto a letto, il che francamente è un po' come cambiare l'olio a un'auto a noleggio","Puoi aspettare un mese per il sesso solo se la tua ragazza ha 17 anni e 11 mesi","Se una ragazza è una ex-fidanzata di un fratello, lei è off-limits per sempre fino alla fine dei tempi. Ricorda sempre: con la ex di un fratello non fare il porcello", """Robin: Non posso credere che la mia sorellina voglia perdere la verginità con un pivello con quella crestina orribile in testa! Non è possibile! Dovete aiutarmi a dissuaderla.
Marshall: Argomenti per convincere una ragazza a non fare sesso...
Ted: Io non ne ho nel database!
Barney: Dissuadere dal fare sesso è contro la mia religione!""", "Una bugia è solo una grande storia che qualcuno ha rovinato﻿ con la verità!", """Lily Aldrin: «Ehi, genio del diritto! Sei pronto a prenderti una pausa di un quarto d'ora!».
Marshall Eriksen: «Scusa tesoro, devo lavorare e ho bisogno che il sangue vada qui»""", "o solo tre cose per cui combatterei: il gancio ostinato di un reggiseno, le accuse di molestia sessuale, tutte scampate, ed infine l'impulso di vomitare quando vedo un uomo che indossa scarpe marroni con un completo nero","A volte la vita va così, scolleghi il cervello per una sera e al mattino ti trovi stroncato dai postumi di una sbornia, con una caviglia slogata e un ananas. Ah.. Non si scopri mai come fosse arrivato sul mio comodino ma... era molto buono!","""Marshall Eriksen: «Sono gnocche!».
Barney Stinson: «Uh! Avete ancora tanto da imparare! Voi praticamente siete delle vittime dell'Effetto Cheerleader. Grazie della domanda! L'Effetto Cheerleader c'è quando alcune donne sembrano gnocche ma solamente se sono in gruppo. Lo stesso per le Cheerleader. Sembrano delle gnocche ma se poi andiamo a vederle individualmente sono delle gran cozze!».""", "Ah ti prego, tanto è il solito film, non ne posso più! I ragazzi sono come il metrò, se ne perdi uno, tempo 5 minuti ne passa un altro!", """Frena! Ci sono solo due motivi per rivederti con una che hai scaricato:
1. tette
2. tette finte""", """Barney Stinson: «Sapete perchè amo Halloween? Le ragazze tirano fuori la Pamela Anderson che è in loro almeno per una sera! Se una si veste da strega diventa una sexy strega, se una si da gatta diventa una sexy gatta, da infermiera...».
Lily Aldrin: «Barney si è capito!».
Barney Stinson: «...Una sexy infermiera»""", """Robin Scherbatsky: «Scusa come può un costume da zucca essere sexy?».
Ted Mosby: «Basta solo tagliarlo nei punti strategici»""", """Barney Stinson: «...E' il bello dell'essere sbronzi, si fanno cose che non da sobri uno non farebbe mai».
Lily Aldrin: «Lo dicono anche quelle che sono venute a letto con te! Cinque?»""", """Trudy: «Sto uscendo da un brutto periodo e forse dovrei fare qualcosa di stupido!».
Ted Mosby: «Io sono stupido, potresti farti me!»""", "Ragazzi spesso la vita ci offre momenti belli e romantici che la rendono degna di essere vissuta ma c'è un problema: quei momenti passano.. e nascosta dietro l'angolo c'è una strega brutta, cattiva e con i capelli crespi che si chiama realtà", """Ted Mosby: «Ehi Robyn, Marshall ti ha guardato il culo!».
Robin Scherbatsky: «Mi ha guardato il sedere? Beh, ringrazialo perchè oggi mi sentivo poco interessante!»""", """Marshall Eriksen: «Hai su il push-up o no?».
Lily Aldrin: «Hai fatto la lampada ai polpacci?».
Marshall Eriksen: «Ritiro la domanda»""", """obin Scherbatsky: «Quando è morta mia nonna mi sono fatta bionda!».
Lily Aldrin: «Oh! Due tragedie in un giorno solo!»""", """Barney Stinson: «Ted, le ragazze trovano sexy gli architetti. Pensaci, tu credi qualcosa dal nulla Sei come Dio. E non c'è niente di più attraente di Dio!».
Ted Mosby: «Hai studiato le sacre scritture?»""", """Marshall Eriksen: «Due ragazzi che sono amici non posso fare il brunch?».
Ted Mosby: «Perchè è una cosa poco...».
Robin Scherbatsky: «Virile!».
Marshall Eriksen: «Non lo è? La colazione invece si, e il pranzo anche. Perchè il brunch non lo è?».
Ted Mosby: «Non lo so! Un cavallo non è strano e non lo è nemmeno un corno mse se li metti insieme hai l'unicorno!»""", "Ragazzi, guardate bene questa faccia perchè la prossima volta che l'avrete davanti sarà sfigurata in modo assolutamente sexy! Questa è la mia natura, sono un uomo, adoro combattere, fare a pugni e lordarmi tutto....... me l'appendi così non si stropiccia?" ]
    elenco_citazioni_tbbt=["Da quel che so, il sesso non ha avuto aggiornamenti con grafica ad alta definizione e armamenti potenziati!", "Signore e signori, mentre il signor Kimi in virtù della sua giovinezza e della sua ingenuità è caduto preda dell'inesplicabile bisogno di contatto umano, posso rassicurarvi sul fatto che la mia ricerca continuerà senza interruzione e che le relazioni umane continueranno a sconcertarmi e a farmi schifo. Grazie!", "Sheldon: Osservando i vostri freschi volti mi torna in mente quando anche io stavo decidendo del mio futuro accademico in qualità di semplice specializzando. Avevo 14 anni. Ed ero già infinitamente più avanti di voi nonostante dovessi andare a letto alle 21. Ora, potranno esserci una o due persone in questa stanza che hanno quel che serve per aver successo nel campo della fisica teorica, sebbene più plausibilmente passerete la vita ad insegnare alle elementari come costruire vulcani con lava di bicarbonato di sodio. Per farla breve, chiunque vi abbia detto che un giorno sarete in grado di dare un contributo significativo alla fisica vi ha giocato un brutto scherzo, uno scherzo davvero crudele", """Leonard: “Quindi, hai intenzione di arrenderti così?”
Sheldon: No, non mi sto arrendendo. Io non mi arrendo mai
Leonard: E cosa staresti facendo?
Sheldon: Sto…trascendendo la situazione. Sono chiaramente troppo evoluto per guidare""", "Sheldon: A volte dimentico che gli altri hanno dei limiti. E’ così triste", """Sheldon: Cosa avevi di più importante della serata Wii-Bowling?
Leonard: In realtà ero..
Sheldon: Era una domanda retorica, niente è più importante della serata Wii-Bowling""", """Sheldon: E se alla fine si ritrovasse con un bambino che non saprà se usare un integrale o un differenziale per trovare l´area sottesa da una curva?
Leonard: Sono sicuro che lo amerebbe ugualmente.
Sheldon: Io non lo amerei""", """Penny: Scusami, hai provato a costruire una macchina per la TAC?
Sheldon: Non ci ho provato, ci sono riuscito. Per un attimo ho visto l’interno del criceto di mia sorella, Palla di Neve, prima che prendesse fuoco. Questo generò una curiosa espressione a casa nostra, una palla di neve non ha speranza in una TAC""", """Sheldon: Sai qual e’, dal punto di vista statistico, la causa di morte piu’ probabile alla mia eta’?
Leonard: Per mano del tuo coinquilino?
Sheldon: Un incidente.
Leonard: E’ cosi’ che lo faro’ sembrare…""", """Sheldon: Amy, mi stavo chiedendo se dovremmo effettivamente indulgere al coito almeno una volta nella nostra relazione.
Bazinga.""", """Page: Sono l’Agente Speciale Page, FBI.
Sheldon: Lei dice di essere l’Agente Speciale Page dell’FBI.
Page: Ecco il mio distintivo.
Sheldon: Ed ecco il mio…tesserino di membro della Justice League. Ma questo non prova che io conosca Batman""", """Leonard: No, sul serio, credo di aver finalmente capito qual e’ il mio problema con le donne.
Sheldon: Il capibara e’ il piu’ grande esemplare della famiglia dei roditori.
Leonard: E questo cosa c’entra con i miei problemi con le donne?
Sheldon: Niente. Era un tentativo disperato di proporre un argomento alternativo""", "Sheldon: Gesù, invece, in realtà è nato in estate. Il giorno della sua nascita è stato spostato per coincidere con la tradizionale ricorrenza pagana in cui si celebrava il solstizio d’inverno accendendo fuochi e sgozzando capretti. Il che, a dirla tutta, sembra molto piu’ divertente di dodici ore in chiesa con mia madre, seguite da una semplice torta di frutta secca", """Howard: E tu pensi di poter sopportare Sheldon?
Raj: Beh, sono Hindu. La mia religione mi insegna che se soffrirò in questa vita sarò ricompensato nella prossima. Tre mesi al Polo Nord con Sheldon e rinascerò come un miliardario superdotato con le ali""", """Leonard: Ok, hai davvero bisogno della tessera di membro onorario della Justice League of America?
Sheldon: E’ stata in tutti i miei portafogli da quando avevo cinque anni.
Leonard: Perchè?
Sheldon: Dice: “Tenere sempre con sé”. E’ proprio qui, sotto l’autografo di Batman""", """Penny: Sheldon, cosa vuoi?
Sheldon: Una Coca Cola Light.
Penny: Per favore, puoi ordinare un cocktail? Devo fare pratica con gli alcolici!
Sheldon:Va bene. Prendo un Virgin Cuba Libre.
Penny: Cioè rum e coca senza il rum.
Sheldon: Si.
Penny: Quindi… Coca.
Sheldon: Si. Me la faresti light?""", """Sheldon: Sai come faccio a sapere che non siamo dentro Matrix?
Leonard: Come?
Sheldon: Se lo fossimo, il cibo sarebbe migliore""", """Penny: Senti, perchè non ti compriamo questo robot e ce ne andiamo a casa?
Sheldon: Voglio quello lì.
Penny: Ok, puoi avere quello.
Leonard: Oh, ma andiamo… Ci giocherà due volte e poi finirà nell’armadio con tutte le altre cianfrusaglie.
Penny: Compragli quel robot, Leonard!
Sheldon: Posso prendere anche questo fumetto?
Penny: Certo che puoi.""", "Sheldon: Che computer possiede? E la prego non mi dica “uno bianco”", """Leonard: Quindi l’intera comunita’ scientifica deve crederti sulla parola?
Sheldon: Non devono, ma dovrebbero.""", """Sheldon: Invece di una centrifuga al titanio, i miei genitori mi regalarono… E’ difficile da dire… Mi regalarono… una mini-moto da cross.
Penny: No!
Sheldon: Quale ragazzino di 12 anni vorrebbe mai una mini-moto da cross?
Penny:Tutti?"""]
    random_himym=random.choice(elenco_citazioni_himym)+"""
Da How I met your mother"""
    random_tbbt=random.choice(elenco_citazioni_tbbt)+"""
Da The big bang theory"""
    elenco_citazioni_random=[random_tbbt,random_himym]
    risposta(message,random.choice(elenco_citazioni_random))
@bot.message_handler(commands=["aiuto","start"])
def invia_comandi(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    risposta(message,"""i comandi sono:
/aiuto
/citazione
/congratula
/insulta
/striscia
/playmate
/pornimg
/pornvid
/pornsrc
/cibo
/encrypt
/decrypt""")
#@bot.message_handler(commands=["prova"])
#def invia_striscia_xdcd(message):
 #   from lxml import html
  #  import requests
   # page=requests.get("http://xdcd.com/1645/")
    #tree=html.fromstring(page.content)
    #cacca=tree.xpath('//*[@id="comic"]/img')
    #risposta(message,cacca)
    #bot.send_photo(message.chat.id, open(cacca))


#inizio comandi personali
@bot.message_handler(commands=["aggiorna_elenco_file_strisce"])
def aggiorna_elenco_file_strisce(message):
 from os import listdir
 from os.path import isfile, join
 onlyfiles = [f for f in listdir(search_path+"/strisce") if isfile(join(search_path+"/strisce", f))]
 risposta(message, "elenco aggiornato")
@bot.message_handler(commands=['aggiungi'])
def aggiungi_risposta(message):
    html=message.text.replace("/aggiungi","")
    file = open(search_path+"testi.txt", "a")
    file.write(html+"\n")
    file.close()
#fine comandi personali

@bot.message_handler(commands=["congratula"])
def congratula(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    messaggio=message.text.replace("/congratula","")
    risposta(message,"congratulazioni"+messaggio+"!")
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
    bot.send_message(message.chat.id,cipher_text.decode(encoding='UTF-8'))
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
        bot.send_message(message.chat.id,plain_text.decode(encoding='UTF-8'))
    except:
        risposta(message,'Si è verificato un errore')
@bot.message_handler(commands=["playmate"])
def invia_playmate(message):
 try:
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    nome_file=(random.choice(lista_playmate))
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, open(search_path+"/playmates/"+nome_file,'rb'))
    nome_file=nome_file.replace(".jpg","")
    nome_file=nome_file[6:]
    bot.send_message(message.chat.id,nome_file)
 except:
     risposta(message,"si è verificato un errore")
@bot.message_handler(commands=["pornvid"])
def invia_video_porno(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    bot.send_chat_action(message.chat.id, 'upload_video')
    try:
     bot.send_video(message.chat.id,open(search_path+"/videoporno/"+random.choice(lista_video_porno_mp4),'rb'))
    except requests.exceptions.ChunkedEncodingError:
        print("ChunkedEncodingError")
        risposta(message,"Si è verificato un errore, contatta @Kaykin se vuoi/puoi, oppure riprova")
    except telebot.apihelper.ApiException:
        print("ApiException")
        risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
@bot.message_handler(commands=["pornsrc"])
def cerca_porno(message,y=0):
 try:
  uid = message.text
  message_dict = "1"
  event_name = message.text
  print(botan.track(botan_token, uid, message_dict, event_name))
  elenco_link=[]
  sito="http://www.pornhub.com/video/search?search="
  messaggio=message.text.replace("/pornsrc","")
  if messaggio=="":
    risposta(message,"inserisici un termine da cercare")
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
    sito2=sito[:-1]+"&page=2"
    sito3=sito[:-1]+"&page=3"
    sito4=sito[:-1]+"&page=4"
    sito5=sito[:-1]+"&page=5"
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
    for x in lista_soup:
        ottieni_link_porno(x)
    for x in range(0,len(elenco_link)):
     if "viewkey" in elenco_link[x]:
        link_usabili_duplicati.append(elenco_link[x])
    for x in range(0,len(link_usabili_duplicati)):
        if link_usabili_duplicati[x] not in link_usabili:
            link_usabili.append(link_usabili_duplicati[x])
    risposta(message,"pornhub.com"+link_usabili[y])
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for x in range(0,len(link_usabili)):
        markup.add(str("/pornsrc "+messaggio_keyboard+ " "+str(x)))
    bot.reply_to(message, 'Ancora?', reply_markup=markup)
 except UnicodeEncodeError:
     risposta(message,"@Kaykin è un programmatore stupido e non sa implementare i caratteri unicode, come ad esempio 'è', quindi per adesso ti tocca aspettare, oppure vai direttamente su pornhub.com")
 except urllib.error.HTTPError:
     risposta(message,"http error, e @KayKin non sa il perché")
 except AttributeError:
     risposta(message,"Il programmatore delle api ha creato un bug con l'update 2.0 e @kaykin sta aspettando un fix perché è pigro e non ha voglia di correggerlo da solo")
@bot.message_handler(commands=["pornimg"])
def invia_immagine_porno(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id,open(search_path+"/fotoporno/"+random.choice(lista_foto_porno),'rb'))
    except:
     risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
@bot.message_handler(commands=["cibo"])
def invia_cibo(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id, open(search_path+"/cibo/"+random.choice(lista_cibo),'rb'))
    except:
      risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")
@bot.message_handler(commands=["striscia"])
def invia_striscia(message):
    uid = message.text
    message_dict = "1"
    event_name = message.text
    print(botan.track(botan_token, uid, message_dict, event_name))
    bot.send_chat_action(message.chat.id, 'upload_photo')
    try:
     bot.send_photo(message.chat.id, open(search_path+"/strisce/"+random.choice(lista_strisce),'rb'))
    except:
      risposta(message,"Si è verificato un errore, contatta @kaykin se vuoi/puoi, oppure riprova")

@bot.message_handler(commands=["insulta"])
def insulta(message):
        uid = message.text
        message_dict = "1"
        event_name = message.text
        print(botan.track(botan_token, uid, message_dict, event_name))
        messaggio=message.text.replace("/insulta","")
        lista_insulti=["sei proprio una troia, " + messaggio, "caro, "+messaggio+" sei proprio una testa di cazzo", messaggio+" sei così spaventoso che quando caghi la tua stessa merda dice di fotterti!", messaggio+" sei come la minchia: sempre tra le palle", messaggio+" sei cosi brutto che chi ti guarda vomita", messaggio+", tua madre é peggio di un canestro da basket, gli entrano tutte le palle", messaggio+", io non capisco se sei cretino di tuo oppure ci hai studiato per esserlo", messaggio+",tua mamma ce l'ha così pelosa che per depilarsela deve chiamare la guardia forestale", messaggio+",come ti senti se ti dico che sei solo uno schizzo di sborra di tuo padre?", messaggio+",dall'alito sembra che ti si sia arenato il cadavere di un'orca in gola", messaggio+",sei cosi testa di cazzo che quando un'uomo pensa a te puo diventare gay!", messaggio+",tua madre è come Buffon, ha sempre palle tra le mani", messaggio+",prova a trattenere il respiro cinque minuti così tutti si accorgeranno che l'aria che respiriamo è migliorata"]
        if messaggio != "":
           risposta(message, random.choice(lista_insulti))
        else:
           risposta(message,"aggiungi un nome o qualcuno da insultare, coglione!")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text=="<3":
     risposta(message, "<3 <3")
    if message.text.lower()=="nope":
         risposta(message,"nope")
    if "ciao" in message.text.lower():
      #gesù gegiù questa riga salvami tu(nome dell'id dell'user)
      b = message.from_user.username
      risposta(message, "ciao "+ str(b) +" <3")
    if message.text=="?":
       risposta(message, "ahahahahah")
    if "eh?" in message.text.lower():
        risposta(message, "lo so che non hai capito niente")
    if "ti voglio bene" in message.text.lower():
        risposta(message, "anche il bot te ne vuole :3")
    if "ehi" in message.text.lower():
        risposta(message, "ehiiii")
    if "san schifosino" in message.text.lower():
        risposta(message, "anche barney ne sa qualcosa")



#parte del bot che controlla siti
    if message.text.lower()=="secret":
        risposta(message,"segreto avviato")
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        def controlla_aggiornamento(target):
            if not target.startswith("http"):
                    target = "http://" + target
            if target.endswith("/"):
                 target = target[:-1]
            req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
            gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            html = urllib.request.urlopen(req, context=gcontext).read()
            file = open(search_path+"source.txt", "wb")
            file.write(html)
            file.close()
            with open(search_path+'source.txt', 'rb', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            #stringa da cercare
             if (target != "http://www.back-door.it"):
                if (s.find(b"per essere uno dei primi ad acquistarlo.") != -1):
                   print('tutto ok '+ target)
                else:
                   #scrive un messaggio se il sito viene aggiornato
                   bot.send_message(chat_id="@vogliolescarpe", text="c'è stato un aggiornamento su " + target)
                   #exit()
             if (target == "http://www.back-door.it"):
              #while (s.find(b"error 503")!= -1) or (s.find(b"database")!=-1):
               #   print("sito offline" + target)
                #  time.sleep(10)
              if (s.find(b"ovo") != -1) or (s.find(b"JORDAN X") != -1):
                    bot.send_message(chat_id="@vogliolescarpe", text="c'è stato un aggiornamento su " + target)
                    exit()
              else:
                 print("tutto ok "+ target)
        while True:
         try:
         #controlla_aggiornamento("www.adidas.it/yeezy")
         #time.sleep(120)
          controlla_aggiornamento("http://store.nike.com/it/it_it/pd/nikelab-supreme-air-max-98-scarpa/pid-11070888/pgid-11294114")
          time.sleep(60)
         except urllib.error.HTTPError:
             print("httperror")
             continue
         except urllib.error.URLError:
             print("URLError")
             continue
         except:
             print("other error")
             continue
bot.polling(none_stop=False)
