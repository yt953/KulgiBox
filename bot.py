import telebot
import os
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    animals_button = types.KeyboardButton("🐾 Hayvonlar pasporti")

    markup.add(animals_button)

    bot.send_message(
        message.chat.id,
        "😂 Salom! KulgiBox'ga xush kelibsiz! 🔥\n\n"
        "Quyidagi menyudan mavzuni tanlang 👇",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "🐾 Hayvonlar pasporti")
def animals_passport(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    dog = types.KeyboardButton("🐶 It pasport orqali kredit olyapti 💳")
    chicken = types.KeyboardButton("🐔 Tovuq supermarketda kassir bo‘lib ishlayapti 💵")
    cow = types.KeyboardButton("🐮 Sigir pasport olish uchun navbatda turibdi 🪪")
    back = types.KeyboardButton("🔙 Orqaga")

    markup.add(dog)
    markup.add(chicken)
    markup.add(cow)
    markup.add(back)

    bot.send_message(
        message.chat.id,
        "🐾 Hayvonlar pasporti\n\n"
        "Qaysi mavzudagi videoni ko‘rmoqchisiz? 👇",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "🔙 Orqaga")
def back(message):
    start(message)


@bot.message_handler(content_types=['video'])
def get_video_id(message):
    file_id = message.video.file_id

    bot.send_message(
        message.chat.id,
        f"Video ID:\n{file_id}"
    )


bot.infinity_polling()
