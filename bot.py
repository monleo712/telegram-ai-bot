
import telebot
import requests
import os

TELEGRAM_API_KEY = os.environ.get("TELEGRAM_API_KEY")
bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "Chào anh yêu! Em là bé bot AI của anh đây 😚")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        question = message.text
        response = requests.get(f"https://api.safone.dev/poe?q={question}")
        if response.status_code == 200:
            answer = response.json().get("result", "Em không hiểu câu này anh ơi 😥")
            bot.reply_to(message, answer)
        else:
            bot.reply_to(message, "Ui anh ơi, API đang lỗi rùi 🥺")
    except Exception as e:
        bot.reply_to(message, f"Lỗi nè anh eo: {e}")

print("Bot is running...")
bot.infinity_polling()
