# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import telebot
from aiogram.dispatcher.event import telegram
from telebot import types




bot = telebot.TeleBot('token')


def get_schedule():
    return """
*Расписание на понедельник:*
🕘 *9:00-9:50* 
📚 Java lecture 
🚪 423 B 

🕙 *10:00-10:50*
📚 TWIX lecture 
🚪 423 B

🕚 *11:00-11:50*
📚 Data base lecture 
🚪 423 B

🕛 *12:10-13:00*
📚 Philosophy lecture 
🚪 423 B

🕐 *13:10-14:00*
📚 Java practice 
🚪 417 B
"""



@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("schedule")
        btn2 = types.KeyboardButton("additionally")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Я возможно помогу тебе".format(
                                 message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
        if (message.text == "schedule"):
                bot.send_message(message.chat.id, text="расписание вот такое: \n" + get_schedule(), parse_mode='Markdown')
        elif (message.text == "additionally"):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Как меня зовут?")
                btn2 = types.KeyboardButton("Что я могу?")
                back = types.KeyboardButton("Main_menu")
                markup.add(btn1, btn2, back)
                bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

        elif (message.text == "Как меня зовут?"):
                bot.send_message(message.chat.id, "У меня нет имени..")

        elif message.text == "Что я могу?":
                bot.send_message(message.chat.id, text="Поздороваться с читателями")

        elif (message.text == "Main_menu"):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("schedule")
                button2 = types.KeyboardButton("additionally")
                markup.add(button1, button2)
                bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        else:
                bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)


@bot.message_handler(commands=['start'])
def start(message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineQueryResultsButton("schedule")
        markup.add(button1)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
        if(message.text == '/schedule'):
                bot.send_message(message.chat.id, text="Notion [Schedule](https://www.notion.so/Horaire-2d2ae5440199469eab0e4dfa909eaa19?pvs=4)", parse_mode='Markdown')
        elif(message.text == 'что то еще'):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('Main_menu')
                markup.add(btn1)
                bot.send_message(message.chat.id, text="else question", reply_markup=markup)


bot.polling(none_stop=True)









# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#         bot.send_message(message.from_user.id, "Notion [Schedule](https://www.notion.so/Horaire-2d2ae5440199469eab0e4dfa909eaa19?pvs=4)", parse_mode='Markdown')
# bot.polling(none_stop=True, interval=0)
