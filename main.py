import requests
import telebot

TOKEN = '5860708137:AAFNF2TzSFwuMXGfNCr-fO7CSuFAVELN8Ns'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello, <b>{message.from_user.first_name}! </b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')

    url = "https://urban-dictionary7.p.rapidapi.com/v0/random"

    headers = {
        "X-RapidAPI-Key": "6b6e1a3c26msh94b311eb50f9340p1aa36ejsnb4652545d2da",
        "X-RapidAPI-Host": "urban-dictionary7.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    answer = response.json()
    word = answer['list'][0]['word']
    definition = answer['list'][0]['definition']
    example = answer['list'][0]['example']
    link = answer['list'][0]['permalink']

    definition_string = ""
    example_string = ""
    index = ["]", "["]
    for i in definition:
        if i not in index:
            definition_string += i
    for i in example:
        if i not in index:
            example_string += i

    random_word = f"Here's your random word: <b>{word}</b> \n\nIts <b>definition</b>: {definition_string}. \n\nIn case you need an <b>example</b>: \n<u>{example_string}</u>"
    bot.send_message(message.chat.id, random_word, parse_mode="html")
    bot.send_message(message.chat.id, link)


bot.polling()
