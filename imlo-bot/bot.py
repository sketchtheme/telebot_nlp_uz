import telebot
from telebot import types
import re
from typing import List
from main import checkWord
from transliterate import to_cyrillic, to_latin

bot = telebot.TeleBot('5850566514:AAGY9Ow5L43ZthUjKRntFC6iAEBx6GMoeys') #tocken

@bot.message_handler(commands=['boshlash'])
def send_welcome(message):
    if message.from_user.last_name is None:
        mess = f'Assalomu Allaykum, @{message.from_user.username}. Yordamchi sizning xizmatingizda, so\'z kiriting!'
    else:
        mess = f'Assalomu Allaykum, {message.from_user.first_name} {message.from_user.last_name}. Yordamchi sizning xizmatingizda, so\'z kiriting!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(commands=['yordam'])
# def help(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     item1 = types.KeyboardButton('Imlo tekshirish')
#     item2 = types.KeyboardButton("Bo'g'inlash")  # this one has
#     markup.add(item1, item2)
#     bot.send_message(message.chat.id, 'Tanlang', reply_markup=markup)


@bot.message_handler()
def check(message):
    word = message.text.split()
    for a in word:
        trans = False

        if a.isascii():
            a = to_cyrillic(str(a))
            print(a)
            trans = True
        result = checkWord(a)
        if result['available']:
            if trans:
                a = to_latin(a)
            response = f"✅ {a.capitalize()}"
        else:
            if trans:
                a = to_latin(a)
            response = f"❌{a.capitalize()}\n"
            for text in result['matches']:
                if trans:
                    text= to_latin(text)
                response += f"✅ {text.capitalize()}\n"

        bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)
