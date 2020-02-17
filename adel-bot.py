# coding=utf-8
import requests
import random
import datetime as dt
import telebot

realtime = dt.datetime.utcnow()
nowtime = realtime.strftime("%H:%M")

answers = ['Норм.',
           'Лучше всех :)',
           'Ну такое', 'Отличненько!',
           'Ничего, жить буду',
           'Поговори мне еще тут!',
           'Хочу обнимашек))',
           'Хочу обнимашек)'
           ]

cityNN = 'Нижний Новгород'

bot = telebot.TeleBot('1001294980:AAHK0Ich3vr7dJ8i7p3PGZwpYSBP1Tisbj8')


def make_url(city):
    return 'http://wttr.in/' + city


def process_coin():
    coin = random.randrange(0, 3)
    if coin == 0:
        return 'Орёл!'
    elif coin == 1:
        return 'Решка!'
    else:
        return random.choice(['Зависла в воздухе', 'Закатилась за угол', 'Ребро!', 'Тебе не нужен этот выбор, поверь)'])

def tickers(price):
    first_full_price = (price*1.03)
    profit = 10 # in rubles
    



def make_parameters():
    params = {
        # 'format': 1,  # погода одной строкой
        'M': '',  # скорость ветра в "м/с"
        '0': '',
        'T': '',
        'Q': '',
        'lang': 'ru'
    }
    return params


def what_weather(city):
    try:
        response = requests.get(make_url(city), params=make_parameters())
        code = response.status_code
        if code == 200:
            return response.text
        else:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<сетевая ошибка>\nНо в душе всегда солнце)\n\nПроверь соединение и повтори попытку'


def how_are_you():
    return random.choice(answers)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Я могу много всего, просто пни моего создателя @msimakoff")
    elif message.text == "How are U":
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text.find("Как дел") != -1:
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text.find("монет") != -1:
        answer = process_coin()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "/weather":
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text.find("погод") != -1:
        if message.text.find(":") != -1:
            message_weather = message.text.split(": ")
            city = message_weather[1]
            bot.send_message(message.from_user.id, what_weather(city))
        else:
            bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text == "Сегодня будет дождь?":
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text == "Сегодня будет снег?":
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text.find("акци") != -1:
        bot.send_message(message.from_user.id, "Скоро я смогу рассчитывать акции для тебя")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


# bot.polling(none_stop=True, interval=1)


def timebrew():
    message = ''
    realtime = dt.datetime.utcnow()
    nowtime = realtime.strftime("%H:%M")
    if nowtime.split(':')[0] == 12:
        mssg = 'Хватит отдыхать, работай!'
        # bot.send_message(message.from_user.id, mssg)
        bot.send_message(message.from_user.id, mssg)
    elif nowtime.split(':')[0] == 14:
        return 'Прошло два часа, а ты не изменил мир к лучешму'
    elif nowtime.split(':')[0] == 16:
        return 'Если я бы была буратино, то, говоря что ты работаешь, мой нос увеличивался бы до огромных размеров'
    elif nowtime.split(':')[0] == 18:
        return 'Скажи мне, что полезного ты сделал за этот день?'



bot.polling(none_stop=True, interval=5)


while (True):
    timebrew()

#python /Users/mSimakoff/Documents/PycharmProjects/criptexx/adel_bot_heroku.py
