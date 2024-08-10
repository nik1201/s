import telebot
import config

bot = telebot.TeleBot(config.token)
from telebot import types

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    

    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, Хочешь получить крутой стикерпак?\nЖми кнопку!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    text = 'Вот держи - <i><a href="https://t.me/addstickers/d222c4b9_c1c9_49f5_9f75_d37742796302_by_sticat_bot">стикерпак!</a></i>'
    try:
        if call.message:
            if call.data == 'test':
                bot.send_message(call.message.chat.id, text, parse_mode='html')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')        
    except Exception as e:
        print(repr(e))            
#run
bot.polling(none_stop=True)