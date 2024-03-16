from config import token
import telebot
from gpt import gpt

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите свой запрос:')

@bot.message_handler(content_types=['text'])
def gptMessage(message):
    resp = gpt(message)
    bot.send_message(message.chat.id, f'Ответ от ЧатGPT: {resp}')

bot.infinity_polling()
