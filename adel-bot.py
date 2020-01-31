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
    return f"http://wttr.in/{city}"


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
        bot.send_message(message.from_user.id, "Я могу много всего, но пока я в разработке ты можешь узнать погоду "
                                               "(/weather) или подбросить монетку (/coin)")
    elif message.text == "How are U":
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "Как дела":
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "Как дела?":
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "Подбрось монетку":
        answer = process_coin()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "/coin":
        answer = process_coin()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "/weather":
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text == "Как погода?":
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text == "Сегодня будет дождь?":
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather(cityNN))
    elif message.text == "Сегодня будет снег?":
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather(cityNN))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help или /weather")


def process_weather(message):
    token = message.split(': ')
    if token[0] == 'Какая погода в городе':
        city = token[1]
        what_weather(city)


# bot.polling(none_stop=True, interval=1)


def timebrew():
    message = ''
    realtime = dt.datetime.utcnow()
    nowtime = realtime.strftime("%H:%M")
    if nowtime.split(':')[0] == 12:
        mssg = f'Хватит отдыхать, работай!'
        # bot.send_message(message.from_user.id, mssg)
        bot.send_message(message.from_user.id, mssg)
    elif nowtime.split(':')[0] == 14:
        return f'Прошло два часа, а ты не изменил мир к лучешму'
    elif nowtime.split(':')[0] == 16:
        return f'Если я бы была буратино, то, говоря что ты работаешь, мой нос увеличивался бы до огромных размеров'
    elif nowtime.split(':')[0] == 18:
        return f'Скажи мне, что полезного ты сделал за этот день?'


bot.polling(none_stop=True, interval=5)

while (True):
    timebrew()
