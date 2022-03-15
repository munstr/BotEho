import telebot
from flask import Flask, request

bot = telebot.TeleBot("5254391359:AAHHzp56Sx79SP0q9MrsRc3klaXwUAk21Do")

server = Flask(__name__)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()