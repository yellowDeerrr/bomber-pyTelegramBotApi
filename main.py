import time

import chromeDriver.main
from MySQLDB.main import addLogsRequests, checkUserInDB, checkInterval, addUserInDBRequests, getDt, createTable
import telebot

bot = telebot.TeleBot('5894871653:AAGz5ybhLreUY7YdaTXWdkkRFjGv40TwOhA')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    createTable()
    user_input_number = bot.send_message(message.chat.id, 'Enter number 380: ')
    bot.register_next_step_handler(user_input_number, setNumber)


def setNumber(message):
    global number

    if message.text == "88424645":
        bot.send_message(message.chat.id, "👍🏿", parse_mode="HTML")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Неа, а всьо</b>", parse_mode="HTML")
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


@bot.message_handler(commands=['startAttack'])
def startAttack(message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    addLogsRequests(id, first_name, number, howMuch)
    if checkUserInDB(id, first_name):
        if checkInterval(id):
            bot.send_message(message.chat.id, "Wait")
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


@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == "688424645":
        bot.send_message(message.chat.id, "👍🏿", parse_mode="HTML")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Неа, а всьо</b>", parse_mode="HTML")


bot.infinity_polling()
