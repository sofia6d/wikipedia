import telebot
from config import *
from wikipediaapi import Wikipedia

bot = telebot.TeleBot(TOKEN)
wiki = Wikipedia('ru')
def send_long_message(chat_id, text):
    while len(text) > 4096:
        bot.send_message(chat_id, text[0:4096])
        text = text[4096::]

        bot.send_message(chat_id, text)
@bot.message_handler(commands=['help', 'start'])
def handler_command(message):
    bot.send_message(message.chat.id, 'О чем вы хотите узнать?')

@bot.message_handler(content_types=["text"])
def handler_message(message):
    page = wiki.page(message.text)
    if page.exists():
        send_long_message(message.chat.id, page.summary)
    else:
        bot.send_message(message.chat.id, 'Ничего не найдено')

    #bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(True)
