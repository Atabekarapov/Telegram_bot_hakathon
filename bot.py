from telebot import TeleBot, types
import parsing

bot = TeleBot("1414554899:AAF62y92KYhhm5L2NGZQdJNJbfwuNUuqpSw")
main_keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton("USD", callback_data="America")
btn2 = types.InlineKeyboardButton("EUR", callback_data="Europe")
btn3 = types.InlineKeyboardButton("RUB", callback_data="Russia")
btn4 = types.InlineKeyboardButton("KZT", callback_data="Kazakhstan")
main_keyboard.add(btn1, btn2, btn3, btn4)

data = {}
file_name = None
@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "КУРСЫ ВАЛЮТ НА СЕГОДНЯ В БИШКЕКЕ", reply_markup=main_keyboard)
def income():

    income_expenses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    a = types.KeyboardButton("Покупка")
    b = types.KeyboardButton("Продажа")
    income_expenses_keyboard.add(a, b)
    return income_expenses_keyboard

@bot.callback_query_handler(func = lambda x:True)
def callback(x):
    income_expenses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if x.data == "America":
        msg = bot.send_message(x.message.chat.id, "Выберите категорию", reply_markup=income())
        bot.register_next_step_handler(msg, USD)
    elif x.data == "Europe":
        msg = bot.send_message(x.message.chat.id, "Выберите категорию", reply_markup=income())
        bot.register_next_step_handler(msg, EURO)
    elif x.data == "Russia":
        msg = bot.send_message(x.message.chat.id, "Выберите категорию", reply_markup=income())
        bot.register_next_step_handler(msg, RUB)
    elif x.data == "Kazakhstan":
        msg = bot.send_message(x.message.chat.id, "Выберите категорию", reply_markup=income())
        bot.register_next_step_handler(msg, KZT)


def Dollar_min(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = a[1]
                list_.append(linee)

            except:
                a = ''
        minim = min(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
def Dollar_max(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = a[2]
                list_.append(linee)

            except:
                a = ''
        minim = max(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the quit button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
       
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)


def Euro_min(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = a[3]
                list_.append(linee)

            except:
                a = ''
        minim = min(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
       
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)

def Euro_max(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = " В " + a[4]
                list_.append(linee)

            except:
                a = ''
        minim = max(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
       
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)

def Rub_min(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = a[5]
                list_.append(linee)

            except:
                a = ''
        minim = min(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)

def Rub_max(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = " В " + a[6]
                list_.append(linee)

            except:
                a = ''
        minim = max(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
       
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)


def Kzt_min(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = a[7]
                list_.append(linee)

            except:
                a = ''
        minim = min(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
       
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
def Kzt_max(message):
    chat_id = message.chat.id
    file = open(file='valuta.csv', mode='r')
    content = file.read()
    lines = content.split('\n')
    if message.text == "Лучшая цена":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = " В " + a[8]
                list_.append(linee)

            except:
                a = ''
        minim = max(list_)
        bot.send_message(chat_id, minim)
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)
       
    elif message.text == "Сохранить":
        file = open('valuta.csv', 'r')
        bot.send_document(chat_id, file)
        file.close()
        msg = bot.send_message(chat_id, "Press the button, if you wanna quit! ", reply_markup=quit_button())
        bot.register_next_step_handler(msg, the_end)


def key1():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn5 = types.KeyboardButton("Сохранить")
    
    btn6 = types.KeyboardButton("Лучшая цена")
    keyboard.add(btn5, btn6)
    return keyboard

  
#----------------Obrobokta soobsheniye--------------||||||----------


def USD(message):
    chat_id = message.chat.id
    if message.text == "Покупка":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Dollar_max)
    elif message.text == "Продажа":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Dollar_min)
def EURO(message):
    chat_id = message.chat.id
    if message.text == "Покупка":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Euro_max)
    elif message.text == "Продажа":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Euro_min)


def RUB(message):
    chat_id = message.chat.id
    if message.text == "Покупка":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Rub_max)
    elif message.text == "Продажа":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Rub_min)
def KZT(message):
    chat_id = message.chat.id
    if message.text == "Покупка":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Kzt_max)
    elif message.text == "Продажа":
        msg = bot.send_message(chat_id, "Выберите категорию", reply_markup=key1())
        bot.register_next_step_handler(msg, Rub_min)

def quit_button():
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn7 = types.KeyboardButton("Quit")
    keyboard2.add(btn7)
    return keyboard2

def the_end(message):
    chat_id = message.chat.id 
    if message.text == "Quit":
        bot.send_sticker(chat_id, "CAACAgIAAxkBAAJeo1-5YexgAhfI3Uko8bcj5g-EGpeZAAIBBwACeVziCWji44hI1IjHHgQ")
        bot.send_message(chat_id, "See you next time" + "🙂!" )
bot.polling()

