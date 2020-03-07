# coding=utf-8
import requests
import random
import datetime as dt
import telebot

realtime = dt.datetime.utcnow()
nowtime = realtime.strftime("%H:%M")

version = ' 0.2.7⍺'

gd_dy = ['Добрый день!',
         'День добрый!',
         'Have a nice day!']

gd_mnng = ['Доброе утречко',
           'Доброе!',
           'Good morning!']

love_answer = ['Любит, и очень сильно, рррр',
               'Конечно любит, рыка',
               'Я люблю тебя, моя милая',
               'Очень любит и скучает по тебе',
               'K.,k.',
               'Он говорит, что ты рыка любимая']

message_about = ('Привет, я Адель, меня создали чтобы помогать тебе\n'
                 'Мой ленивый отец постепенно учит меня, я становлюсь умнее\n'
                 ' Сейчас он говорит что моя '
                 'версия ' + str(version) + ' ,но я верю, что я когда нибудь выйду из альфы')

invest_wrong_message = ('Ты не указал цену, повтори свой запрос, в конце указав цену через двоеточие '
                        'Например Посчитай сколько надо купить акций на сумму: 1000')

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


def weather_snow_rain(text):
    if text.find(":") != -1:
        message_weather = text.split(": ")
        city = message_weather[1]
        bot.send_message(text.from_user.id, what_weather(city))
    else:
        bot.send_message(text.from_user.id, what_weather(cityNN))


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


def invest(price):
    # first_cost = 0
    first_cost = price
    # profit = 10
    # fee = 1.03
    total_cost = (1000 / 103) + first_cost
    return total_cost


def how_are_you():
    return random.choice(answers)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.find("Hello") != -1:
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    # version
    elif message.text.find("себе") != -1:
        bot.send_message(message.from_user.id, message_about)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Я могу много всего, просто пни моего создателя @msimakoff")
    elif message.text == "How are U":
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text.find("иш") != -1:
        if message.text.find("люб") != -1:
            bot.send_message(message.from_user.id, random.choice(love_answer))
    elif message.text.find("ак дел") != -1:
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text.find("монет") != -1:
        answer = process_coin()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "/weather":
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text.find("погод") != -1:
        weather_snow_rain(message.text)
    elif message.text.find("дождь") != -1:
        weather_snow_rain(message.text)
    elif message.text.find("снег") != -1:
        weather_snow_rain(message.text)
    elif message.text.find("обр") != -1:
        if message.text.find("ое утр") != -1:
            bot.send.message(message.from_user.id, random.choice(gd_mnng))
        elif message.text.find("рый ден") != -1:
            bot.send.message(message.from_user.id, random.choice(gd_dy))
    elif message.text.find("акци") != -1:
        if message.text.find(":") != -1:
            message_price = message.text.split(": ")
            price = message_price[1]
            final_price = str(invest(price))
            bot.send_message(message.from_user.id, 'Чтобы получить выгоду, тебе надо купить на'
                                                   '' + final_price + 'рублей')
        else:
            bot.send_message(message.from_user.id, invest_wrong_message)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


# bot.polling(none_stop=True, interval=1)


bot.polling(none_stop=True, interval=5)
