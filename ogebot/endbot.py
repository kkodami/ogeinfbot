from telebot import * # Импортируем библиотеку
import settings

bot = telebot.TeleBot(settings.API_KEY) # переменная, которая хранит в себе токен



# Задание 1
z1e1 = 'https://imgur.com/a/SpRHaCC'
z1e2 = 'https://imgur.com/RZaohV5'
z1e3 = 'https://imgur.com/7V668iG'
z1e4 = 'https://imgur.com/iR65SuM'
z1e5 = 'https://imgur.com/LCvySM4'
z1m1 = 'https://imgur.com/asHAkp7'
z1h1 = 'https://imgur.com/b9ylYvq'
# Задание 2
z2e1 = 'https://imgur.com/jZQzNY0'
z2e2 = 'https://imgur.com/KV1QYkI'
z2e3 = 'https://imgur.com/9OzPrnu'
z2e4 = 'https://imgur.com/kPoK7vK'

z2m1 = 'https://imgur.com/ii9POiy'
z2m2 = 'https://imgur.com/fuz5GW2'
z2m3 = 'https://imgur.com/3VE8rEW'

z2h1 = 'https://imgur.com/i9edidB'
z2h2 = 'https://imgur.com/RjmyObp'
z2h3 = 'https://imgur.com/PdPn7Ze'
z2h4 = 'https://imgur.com/7Zz8aSX'
# Задание 3
z3e1 = 'https://imgur.com/yweOPQO'
z3e2 = 'https://imgur.com/TKyug9u'
z3e3 = 'https://imgur.com/6wSXNBO'
z3e4 = 'https://imgur.com/cInn7r0'

z3m1 = 'https://imgur.com/AIJjAmb'

z3h1 = 'https://imgur.com/JA8nWmB'
# Задание 4
z4e1 = 'https://imgur.com/UtExV2s'
z4e2 = 'https://imgur.com/tHxqrdm'
z4e3 = 'https://imgur.com/D87jU4t'
z4e4 = 'https://imgur.com/GsRqDe0'

z4m1 = 'https://imgur.com/W46UanW'
z4m2 = 'https://imgur.com/49jqYNq'

z4h1 = 'https://imgur.com/UiJeLtO'
# Задание 5
z5e1 = 'https://imgur.com/09oqVY2'
z5e2 = 'https://imgur.com/hvL61bo'
z5e3 = 'https://imgur.com/Y50T9Xd'
z5e4 = 'https://imgur.com/JLeOiPH'

z5m1 = 'https://imgur.com/8MYnTGv'
z5m2 = 'https://imgur.com/isEXsI2'

z5h1 = 'https://imgur.com/MRMcNpr'
# Задание 6
z6e1 = 'https://imgur.com/vXqivh2'
z6e2 = 'https://imgur.com/SpAlUQZ'
z6e3 = 'https://imgur.com/QzEjXBV'
z6e4 = 'https://imgur.com/4JO51pD'
z6e5 = 'https://imgur.com/F5KyHVd'
z6e6 = 'https://imgur.com/9T82URA'
z6e7 = 'https://imgur.com/L0az8Gp'
z6e8 = 'https://imgur.com/FD62ZXX'
z6e9 = 'https://imgur.com/Ume3U2b'
z6e10 = 'https://imgur.com/btMd1dP'

z6m1 = 'https://imgur.com/xJQ9vwE'
z6m2 = 'https://imgur.com/ywIBLPW'
z6m3 = 'https://imgur.com/ALgYKiM'
z6m4 = 'https://imgur.com/rkzLoDh'
z6m5 = 'https://imgur.com/hjY8GOH'

z6h1 = 'https://imgur.com/nV1hDPN'
z6h2 = 'https://imgur.com/IBG7Gf0'
z6h3 = 'https://imgur.com/iI2dme3'
# Задание 7
z7e1 = 'https://imgur.com/iZXcFJ8'
z7e2 = 'https://imgur.com/x2Rmc8p'

z7m1 = 'https://imgur.com/vBfJWlZ'
z7m2 = 'https://imgur.com/g9VIrZ8'
z7m3 = 'https://imgur.com/SXTAKAB'

z7h1 = 'https://imgur.com/GOCC3tn'
z7h2 = 'https://imgur.com/fwWdatd'
# Задание 8
z8e1 = 'https://imgur.com/6eQtDCv'
z8e2 = 'https://imgur.com/OurA0zu'
z8e3 = 'https://imgur.com/N509g4b'

z8m1 = 'https://imgur.com/gHdcB9I'
z8m2 = 'https://imgur.com/cZYHLzR'

z8h1 = 'https://imgur.com/6Y7VdIw'
z8h2 = 'https://imgur.com/kODiccm'
z8h3 = 'https://imgur.com/5aIn4xE'
# Задание 9
z9e1 = 'https://imgur.com/9ivEDyT'
z9e2 = 'https://imgur.com/aV7WOTQ'
z9e3 = 'https://imgur.com/fbQxsAe'

z9m1 = 'https://imgur.com/Wd9GYFy'
z9m2 = 'https://imgur.com/9vxg6Pb'
z9m3 = 'https://imgur.com/oBKKtLZ'

z9h1 = 'https://imgur.com/TduMD6V'
# Задание 10
z10e1 = 'https://imgur.com/sSkvNlk'

z10m1 = 'https://imgur.com/av8UnWL'

z10h1 = 'https://imgur.com/EDaQUUu'




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    btn10 = types.KeyboardButton('10')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4,btn5, btn6)
    markup.row(btn7, btn8, btn9)
    markup.row(btn10)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name},\
 я телеграм - бот, который поможет тебе в подготовкее с ОГЭ по информатике, \
здесь ты можешь найти все типы заданий\
 с сайта https://oge.sdamgia.ru/. Введи цифру нужного задания для получения заданий КИМ', reply_markup=markup)
    bot.register_next_step_handler(message, process_button)
    
    

def process_button(message): # Создаем функцию
    if message.text == '1':   #Если пользователь выберет задание номер 1, то предлагаем ему выбрать сложность
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process1) #Если пользователь выбрал все верно, то переходим к следующей функции
        
        
    if message.text == '2':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process2)

        
        
    if message.text == '3':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process3)
        
        
    elif message.text == '4':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process4)
        
        
    elif message.text == '5':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process5)
        
        
    elif message.text == '6':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process6)
        
        
    elif message.text == '7':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process7)
        
        
    elif message.text == '8':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process8)
        
        
    elif message.text == '9':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process9)
        
        
    elif message.text == '10':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button1 = types.KeyboardButton('Простое')
        button2 = types.KeyboardButton('Среднее')
        button3 = types.KeyboardButton('Сложное')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Выберите сложность:", reply_markup=markup)
        bot.register_next_step_handler(message, process10)

def process1(message):
    if message.text == 'Простое': 
        bot.send_photo(message.chat.id, z1e1)
        bot.send_photo(message.chat.id, z1e2)
        bot.send_photo(message.chat.id, z1e3)
        bot.send_photo(message.chat.id, z1e4)
        bot.send_photo(message.chat.id, z1e5)
    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z1m1)
    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z1h1)
        # К соответвующему ответу высылаем пользователю конкретные скриншоты с заданиями  
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        # Проверка на корректность введенных данных пользователя


def process2(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z2e1)
        bot.send_photo(message.chat.id, z2e2)
        bot.send_photo(message.chat.id, z2e3)
        bot.send_photo(message.chat.id, z2e4)
    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z2m1)
        bot.send_photo(message.chat.id, z2m2)
        bot.send_photo(message.chat.id, z2m3)
    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z2h1)
        bot.send_photo(message.chat.id, z2h2)
        bot.send_photo(message.chat.id, z2h3)
        bot.send_photo(message.chat.id, z2h4)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process3(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z3e1)
        bot.send_photo(message.chat.id, z3e2)
        bot.send_photo(message.chat.id, z3e3)
        bot.send_photo(message.chat.id, z3e4)
    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z3m1)

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z3h1)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process4(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z4e1)
        bot.send_photo(message.chat.id, z4e2)
        bot.send_photo(message.chat.id, z4e3)
        bot.send_photo(message.chat.id, z4e4)
    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z4m1)
        bot.send_photo(message.chat.id, z4m2)

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z4h1)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process5(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z5e1)
        bot.send_photo(message.chat.id, z5e2)
        bot.send_photo(message.chat.id, z5e3)
        bot.send_photo(message.chat.id, z5e4)
    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z5m1)
        bot.send_photo(message.chat.id, z5m2)

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z5h1)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process6(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z6e1)
        bot.send_photo(message.chat.id, z6e2)
        bot.send_photo(message.chat.id, z6e3)
        bot.send_photo(message.chat.id, z6e4)
        bot.send_photo(message.chat.id, z6e5)
        bot.send_photo(message.chat.id, z6e6)
        bot.send_photo(message.chat.id, z6e7)
        bot.send_photo(message.chat.id, z6e8)
        bot.send_photo(message.chat.id, z6e9)
    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z6m1)
        bot.send_photo(message.chat.id, z6m2)
        bot.send_photo(message.chat.id, z6e3)
        bot.send_photo(message.chat.id, z6e4)
        bot.send_photo(message.chat.id, z6e5)

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z6h1)
        bot.send_photo(message.chat.id, z6e2)
        bot.send_photo(message.chat.id, z6e3)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
def process7(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z7e1)
        bot.send_photo(message.chat.id, z7e2)

    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z7m1)
        bot.send_photo(message.chat.id, z7m2)
        bot.send_photo(message.chat.id, z7m3)

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z7h1)
        bot.send_photo(message.chat.id, z7h2)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process8(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z8e1)
        bot.send_photo(message.chat.id, z8e2)
        bot.send_photo(message.chat.id, z8e3)

    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z8m1)
        bot.send_photo(message.chat.id, z8m2)
        

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z8h1)
        bot.send_photo(message.chat.id, z8h2)
        bot.send_photo(message.chat.id, z8h3)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process9(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z9e1)
        bot.send_photo(message.chat.id, z9e2)
        bot.send_photo(message.chat.id, z9e3)

    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z9m1)
        bot.send_photo(message.chat.id, z9m2)
        bot.send_photo(message.chat.id, z9m3)
        

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z9h1)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
def process10(message):        
    if message.text == 'Простое':
        bot.send_photo(message.chat.id, z10m1)

    elif message.text == 'Среднее':
        bot.send_photo(message.chat.id, z10m1)
        
        

    elif message.text == 'Сложное':
        bot.send_photo(message.chat.id, z10h1)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов: Простое, Среднее или Сложное.")
        
        
# Запуск бота
bot.polling(none_stop=True)