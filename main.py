import telebot
from telebot import types

token = '5399496836:AAF136tW1X_DbZcaa-4o4W0315RSI1-4co0'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/привет", "/help", "/пока")
    keyboard.row("Хочу", "МТУСИ?", "Адрес?")
    keyboard.row("Факультеты?", "Спасибо!")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['привет'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/привет", "/help", "/пока")
    keyboard.row("Хочу", "МТУСИ?", "Адрес?")
    keyboard.row("Факультеты?", "Спасибо!")
    bot.send_message(message.chat.id, 'Привет! Я бот, умею много интересного. Напиши мне /help, чтобы узнать, что я умею!', reply_markup=keyboard)



@bot.message_handler(commands=['пока'])
def bye(message):
    bot.send_message(message.chat.id, 'До встречи! Надеюсь, еще увидимся!')


@bot.message_handler(commands=['help'])
def help(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/привет", "/help", "/пока")
    keyboard.row("Хочу", "МТУСИ?", "Адрес?")
    keyboard.row("Факультеты?", "Спасибо!")
    bot.send_message(message.chat.id, 'Все очень просто!\nВот команды которые я знаю:')
    bot.send_message(message.chat.id, '/привет - Мы поздороваемся)\n/пока - мы попорощаемся))\n/help - ты уже про нее знаешь, тут я расскажу что я умею')
    bot.send_message(message.chat.id, 'А вот что ты мне можешь сказать:')
    bot.send_message(message.chat.id, '\"Хочу\" - расскажу как поступить к нам\n\"МТУСИ?\" - поясню за расшифровку\n\"Адрес?\" - расскажу где мы находимся\n\"Факультеты?\" - расскажу, какие у нас есть факультеты', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "мтуси?":
        bot.send_message(message.chat.id, 'Аббревиатура \"МТУСИ\" расшифровывается как\n \"Московский Технический Университет Связи и Информатики\"')
    elif message.text.lower() == "адрес?":
        bot.send_message(message.chat.id, 'У нас 2 адреса:\n111024, г. Москва, ул. Авиамоторная, 8а\n123423, г. Москва, ул. Народного Ополчения, д. 32')
    elif message.text.lower() == "факультеты?":
        bot.send_message(message.chat.id, 'Наши факультеты:\nИнформационные технологии;\nКибернетика и информационная безопасность;\nРадио и телевидение;\nСети и системы связи;\nЦифровая экономика и массовые коммуникации.')
    elif message.text.lower() == "спасибо!":
        bot.send_message(message.chat.id, 'Пожалуйста!\nБыло приятно рассказать о нашем университете!')


bot.polling(none_stop=True, interval=0)

