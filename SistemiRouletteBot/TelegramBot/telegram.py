from TelegramBot.models import Cliente, Subscription
from datetime import datetime
import re
import threading
import telebot

bot = telebot.TeleBot("1923790206:AAGzmJdXrKACWGWdczVTZcz0AsQbqj3DIE4")

serieNumeri = {}

class threadTelegramReader(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        checkTelegramMessages()

# Definisco le funzioni che possono essere chiamate
def checkTelegramMessages():
    # '/start' or '/help'
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        
        username = message.from_user.username

        if checkPermission(user_id):
            bot.send_message(
                chat_id,
                "Benvenuto " + username + " nel bot di SistemiRoulette!\n" +
                "Per avere qualsiasi tipo di assistenza contattare @Trip6900 o @ZdiZanti\n\n" +
                "Iniziare a digitare i numeri per avere le predizioni:"
            )    
        else:
            bot.send_message(
                chat_id, 
                "Benvenuto " + username + " nel bot di SistemiRoulette!\n\n" +
                "Per poter utilizzare il bot bisogna essere registrati nella whitelist.\n\n" +
                "Nel caso non sei nella whitelist ma vuoi entrare:\n" +
                "- Scrivere /join per entrare nella coda degli account da approvare.\n" + 
                "- Contattare @Trip6900 o @ZdiZanti per fare approvare l'account\n\n" +
                "Nel caso tu sia già nella whitelist avrai bisogno di un'iscrizione per poter utilizzare il bot. Reperibile contattando @Trip6900 o @ZdiZanti"
            )

    # un numero a una cifra della roulette
    @bot.message_handler(func = lambda message: re.match("^[0-9]{1}$", message.text))
    def read_number(message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        numero = message.text

        if checkPermission(user_id):
            if aggiungiNumeroASerie(user_id, numero, chat_id):
                if previsioneDisponibile(user_id, numero):
                    bot.reply_to(
                        message, 
                        "Puntare su {}".format(getPrevisione(numero))  
                    )

    # un numero a due cifre della roulette
    @bot.message_handler(func = lambda message: re.match("^[0-9]{2}$", message.text))
    def read_numbers(message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        numero = message.text

        if checkPermission(user_id):
            if aggiungiNumeroASerie(user_id, numero, chat_id):
                if previsioneDisponibile(user_id, numero):
                    bot.reply_to(
                        message, 
                        "Puntare su {}".format(getPrevisione(numero))  
                    )

    # '/reset'
    @bot.message_handler(commands=['reset'])
    def reset_numbers(message):
        bot.reply_to(
            message,
            "TODO: implementare reset"
        )
    
    # '/join'
    @bot.message_handler(commands=['join'])
    def new_guest_user(message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        
        username = message.from_user.username

        cliente = Cliente.objects.filter(id_telegram=user_id)

        if (cliente.count() == 0):
            cliente = Cliente(username=username, id_telegram=user_id, note="Guest")
            cliente.save()

            bot.send_message(
                chat_id, 
                "Grazie " + username + " per esserti registrato nel bot di SistemiRoulette!\n" +
                "Dovrai aspettare che @Trip6900 o @ZdiZanti approvino la tua registrazione"
            )
        else:
            bot.send_message(
                chat_id, 
                "Ciao " + username + ", sembra che tu sia già registrato.\n" +
                "Dovrai aspettare che @Trip6900 o @ZdiZanti approvino il tuo profilo per poter utilizzare il bot, contattali se hai bisogno di assistenza."
            )

    bot.polling()

def checkPermission(user_id):
    # Prendo il primo cliente con quell'id telegram
    cliente = Cliente.objects.filter(id_telegram=user_id).first()

    if cliente != None:
        # Prendo tutte le iscrizioni valide
        iscrizione = Subscription.objects.filter(cliente=cliente, inizio__lte=datetime.now(), scadenza__gt=datetime.now())

    if cliente != None and cliente.verificato == True and iscrizione.count() >= 1:
        return True
    else:
        return False

def aggiungiNumeroASerie(user_id, numero, chat_id):
    numero = int(numero)

    if numero >= 0 and numero <= 36:
        if user_id in serieNumeri:
            serieNumeri[user_id].append(numero)
        else:
            serieNumeri[user_id] = [numero]

        print(serieNumeri)
        return True
    else:
        bot.send_message(
            chat_id, 
            "Inserire solo numeri compresi tra 0 e 36!"
        )
        return False
        
def previsioneDisponibile(user_id, ultimo_numero):
    ultimo_numero = int(ultimo_numero)
    if user_id in serieNumeri:
        countNumeri = len(serieNumeri[user_id])

        if (countNumeri >= 2):
            # Prendo i 9 numeri inseriti prima di questo dall'utente per controllare se è possibile fare una previsione
            numeriDaControllare = serieNumeri[user_id][-10:]
            del numeriDaControllare[-1]

            return ultimo_numero in numeriDaControllare
        else:
            return False
    else:
        return False

def getPrevisione(numero):
    previsioni = {
        0: "34 10 9",
        1: "4 36 28",
        2: "30 20 12",
        3: "25 8 14",
        4: "13 33 7",
        5: "0 34 22",
        6: "32 24 18",
        7: "4 36 1",
        8: "21 20 3",
        9: "26 17 23",
        10: "0 34 22",
        11: "4 33 12",
        12: "4 11 33",
        13: "19 16 7",
        14: "2 8 35",
        15: "6 24 18",
        16: "19 27 29",
        17: "26 10 9",
        18: "6 24 15",
        19: "27 16 29",
        20: "2 30 12",
        21: "8 20 35",
        22: "0 34 10",
        23: "17 9 26",
        24: "15 6 18",
        25: "8 14 3",
        26: "17 23 9",
        27: "19 16 29",
        28: "4 36 1",
        29: "19 16 27",
        30: "2 20 12",
        31: "25 10 35",
        32: "6 24 18",
        33: "4 11 12",
        34: "0 5 22",
        35: "25 10 31",
        36: "4 1 7",
    }
    
    numero = int(numero)
    
    frase = "{} e vicini".format(previsioni[numero])
    
    return frase