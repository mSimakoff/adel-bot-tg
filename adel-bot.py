# coding=utf-8
import requests
import random

import telebot

answers = ['Норм.',
           'Лучше всех :)',
           'Ну такое', 'Отличненько!',
           'Ничего, жить буду',
           'Поговори мне еще тут!',
           'Хочу обнимашек))',
           'Хочу обнимашек)'
           ]

bot = telebot.TeleBot('1001294980:AAHK0Ich3vr7dJ8i7p3PGZwpYSBP1Tisbj8')


def make_url():
    return "http://wttr.in/Нижний_Новгород"


def process_coin():
    coin = random.randrange(0, 3)
    if coin == 0:
        return 'Орёл!'
    elif coin == 1:
        return 'Решка!'
    else:
        return random.choice(['Зависла в воздухе', 'Закатилась за угол', 'Ребро!', 'Тебе так нужен этот выбор?'])


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


def what_weather():
    try:
        response = requests.get(make_url(), params=make_parameters())
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
    elif message.text == "How are U" or "Как дела" or "Как дела?":
        answer = how_are_you()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "Подбрось монетку" or "/coin":
        answer = process_coin()
        bot.send_message(message.from_user.id, answer)
    elif message.text == "/weather" or "Как погода?" or "Погода" or "Сегодня будет дождь?" or "Сегодня будет снег?":
        city = "Нижний Новгород"
        # weather = what_weather(city)
        bot.send_message(message.from_user.id, what_weather())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help или /weather")


bot.polling(none_stop=True, interval=1)
