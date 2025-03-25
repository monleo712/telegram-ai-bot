
import telebot
from config import TELEGRAM_API_KEY
import requests

bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Em iu nè! Anh gõ gì em cũng trả lời nha! 😚")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        question = message.text
        response = requests.get(f"https://api.safone.dev/poe?q={question}")
        if response.status_code == 200:
            answer = response.json().get("result", "Em chưa hiểu câu này anh ơi 😥")
            bot.reply_to(message, answer)
        else:
            bot.reply_to(message, "Ui anh ơi, API đang bị lỗi rồi!")
    except Exception as e:
        bot.reply_to(message, f"Lỗi nè anh eo: {e}")

print("Bot is running...")
bot.infinity_polling()
