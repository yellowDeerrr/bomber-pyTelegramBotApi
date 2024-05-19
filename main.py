import time

import chromeDriver.main
from MySQLDB.main import addLogsRequests, checkUserInDB, checkInterval, addUserInDBRequests, getDt
import telebot
from telebot import types

bot = telebot.TeleBot('5894871653:AAGz5ybhLreUY7YdaTXWdkkRFjGv40TwOhA')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('SMS Bomber')
    item2 = types.KeyboardButton('Generate text')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Виберіть", reply_markup=markup)


def setNumber(message):
    global number

    if message.text == "688424645":
        bot.send_message(message.chat.id, "👍🏿", parse_mode="HTML")
        time.sleep(1)
        bot.send_message(message.chat.id, "👮🏿‍<b>Вже їду</b>", parse_mode="HTML")
        send_welcome(message)
        time.sleep(1)
    elif message.text == "972536871":
        bot.send_message(message.chat.id, "👍🏿", parse_mode="HTML")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>УДАЧІ В ЖИЗНІ </b>", parse_mode="HTML")
        send_welcome(message)
        time.sleep(1)
    else:
        number = str(message.text)
        print(number)

        user_input_howMuch = bot.send_message(message.chat.id, 'How much: ')
        bot.register_next_step_handler(user_input_howMuch, setHowMuch)


def setHowMuch(message):
    global howMuch
    if int(message.text) > 5:
        bot.send_message(message.chat.id, "В безплатній вірсії доступно тільки < 5")
    else:
        howMuch = str(message.text)
        print(howMuch)
        bot.send_message(message.chat.id, "/startAttack")


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, "Okay, one second")
    chromeDriver.main.stop()
    bot.send_message(message.chat.id, "Bot has been stopped")
    send_welcome(message)


@bot.message_handler(commands=['startAttack'])
def startAttack(message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    addLogsRequests(id, first_name, number, howMuch)
    if checkUserInDB(id, first_name):
        if checkInterval(id):
            bot.send_message(message.chat.id, "Wait")
            bot.send_message(message.chat.id, "If you want to stop")
            bot.send_message(message.chat.id, "/stop")
            chromeDriver.main.main(number, howMuch)
            bot.send_message(message.chat.id, "End")
            send_welcome(message)
        else:
            bot.send_message(message.chat.id, f"You can send sms bombers, only one time in 5 minutes"
                                              f"\nYou will can send {getDt(id)}")
            send_welcome(message)
    else:
        addUserInDBRequests(id, first_name)
        bot.send_message(message.chat.id, "Wait")
        chromeDriver.main.main(number, howMuch)
        bot.send_message(message.chat.id, "End")
        send_welcome(message)

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, "Okay, one second")
    chromeDriver.main.stop()
    bot.send_message(message.chat.id, "Bot has been stopped")
    send_welcome(message)


@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == 'SMS Bomber':
        user_input_number = bot.send_message(message.chat.id, 'Enter number 380: ')
        bot.register_next_step_handler(user_input_number, setNumber)
    else:
        bot.send_message(message.chat.id, "I don't understand you")
        send_welcome(message)


bot.infinity_polling()
