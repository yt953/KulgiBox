import telebot
import os
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    video_button = types.KeyboardButton("🎬 Menga video top")

    markup.add(video_button)

    bot.send_message(
        message.chat.id,
        "😂 Salom! KulgiBox'ga xush kelibsiz! 🔥\n\n"
        "Qanday kulgili video kerakligini yozish uchun "
        "pastdagi tugmani bosing 👇",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "🎬 Menga video top")
def video_request(message):
    bot.send_message(
        message.chat.id,
        "🤖 Qanday mavzuda kulgili video kerak?\n\n"
        "Masalan:\n"
        "🐱 Mushuklar pasport olyapti\n"
        "🐶 It maktabga boribdi\n"
        "😂 Ustoz darsda uxlab qolibdi"
    )


bot.infinity_polling()
