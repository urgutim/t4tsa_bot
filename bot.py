import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.full_name
    text = (
        f"👋 Welcome, {username}!\n\n"
        "🔎 Use the *search button* below to find any #movie or #series.\n\n"
        "📢 Join [@T4TSAI](https://t.me/T4TSAI) for the latest updates.\n\n"
        "⚠️ If the search button doesn’t work, visit our website: 🌐 [T4TSA.CC](https://t4tsa.cc)"
    )

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔍 Search", switch_inline_query=""))

    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

bot.infinity_polling()
