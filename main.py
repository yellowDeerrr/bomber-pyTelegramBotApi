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
    item2 = types.KeyboardButton('згенерувати текст')
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


def bot_message(message):
    if message.text == 'згенерувати текст':
        bot.send_message(message.chat.id('Ты абортыш абортыш уебок даун нищий уебок гей ты никто абортыш пидор попуск '
                                         'ничтожество глупый еблан гей даун попуск пидор бомж сосун пидорас слабый '
                                         'выебанный мать в канаве бомж абортыш трахнутый слитый тупой чмо слитый '
                                         'мамонт попуск ты никто пидорас лох ты никто бомж пидорас слабый абортыш '
                                         'пидорас выебанный аутист ахахаха слитый нищий абортыш мамонт выебанный '
                                         'еблан ты никто тупой слабый тупой сосун пидорас ничтожество гей гей ты '
                                         'никто пидор лох уебан глупый абортыш негр пидор ты никто мать в канаве даун '
                                         'выебанный кастрированный сосун выебанный ахахаха даун тупой пидорас аутист '
                                         'абортыш уебан аутист выебанный слитый даун уебок гей чмо пидор пидорас гей '
                                         'глупый чмо гей бот ахахаха ахахаха ты никто бот уебан чмо гей попуск гей '
                                         'абортыш слабый ничтожество еблан лох попуск выебанный мамонт бомж слабый '
                                         'тупой ничтожество гей абортыш хуйло хуйло выебанный абортыш мразь мамонт ты '
                                         'никто выебанный аутист трахнутый трахнутый уебок мать в канаве мамонт '
                                         'глупый слитый абортыш глупый слитый мать в канаве попуск уебан мамонт мать '
                                         'в канаве мразь аутист лох чмо слитый гей негр ахахаха нищий негр хуйло лох '
                                         'чмо тупой абортыш глупый попуск глупый мамонт выебанный кастрированный '
                                         'пидорас пидор хуйло пидор мразь ничтожество уебан нищий гей трахнутый даун '
                                         'хуйло ничтожество трахнутый абортыш пидор сосун хуйло мразь выебанный нищий '
                                         'лох лох гей мамонт сосун сосун тупой трахнутый аутист хуйло глупый сосун '
                                         'трахнутый слитый нищий гей глупый негр гей ты никто мать в канаве даун '
                                         'тупой пидорас уебок выебанный тупой тупой уебан мать в канаве хуйло лох '
                                         'мать в канаве аутист чмо уебан кастрированный чмо слабый пидорас гей '
                                         'выебанный ничтожество еблан гей аутист тупой мать в канаве глупый трахнутый '
                                         'бомж мразь ничтожество глупый тупой слабый нищий бот слабый пидорас '
                                         'ничтожество пидорас мамонт бот ахахаха еблан мать в канаве глупый слитый '
                                         'слитый попуск хуйло чмо слабый бомж слитый абортыш ты никто выебанный пидор '
                                         'нищий слабый абортыш бомж аутист чмо еблан гей слабый бот ничтожество '
                                         'кастрированный даун кастрированный гей абортыш мамонт бомж чмо ахахаха '
                                         'пидорас хуйло попуск трахнутый гей даун абортыш мать в канаве еблан мать в '
                                         'канаве мразь мамонт гей ничтожество ты никто ахахаха слитый еблан аутист '
                                         'чмо абортыш слитый ты никто лох ты никто слабый слабый аутист попуск еблан '
                                         'абортыш нищий ты никто уебок мать в канаве еблан хуйло бот аутист выебанный '
                                         'аутист чмо пидор выебанный уебок кастрированный выебанный гей даун негр '
                                         'трахнутый глупый мамонт пидорас попуск лох ты никто ничтожество пидорас '
                                         'глупый уебок выебанный гей глупый хуйло пидор бот трахнутый ахахаха гей '
                                         'трахнутый ахахаха абортыш трахнутый уебан тупой гей ахахаха глупый пидор '
                                         'трахнутый мамонт бот бомж ничтожество негр даун хуйло ты никто нищий гей '
                                         'чмо чмо мать в канаве выебанный чмо мамонт чмо гей бот слабый мать в канаве '
                                         'глупый аутист выебанный ты никто тупой лох гей слабый ахахаха бомж слитый '
                                         'гей абортыш нищий уебок кастрированный трахнутый негр кастрированный негр '
                                         'глупый уебок хуйло мать в канаве аутист даун гей слитый абортыш трахнутый '
                                         'ты никто гей гей аутист абортыш уебан лох мать в канаве ты никто мать в '
                                         'канаве трахнутый выебанный бот кастрированный пидорас абортыш абортыш чмо '
                                         'чмо чмо бомж аутист тупой мразь ты никто еблан сосун слабый лох еблан гей '
                                         'хуйло трахнутый мать в канаве гей негр мразь уебан пидорас выебанный '
                                         'трахнутый аутист чмо попуск глупый кастрированный сосун глупый тупой попуск '
                                         'ты никто слабый аутист гей слабый мамонт мать в канаве сосун еблан мразь '
                                         'аутист слабый бот выебанный еблан кастрированный попуск тупой выебанный '
                                         'тупой выебанный хуйло кастрированный абортыш еблан пидор мразь попуск '
                                         'абортыш сосун абортыш уебан пидор попуск лох глупый кастрированный мразь '
                                         'попуск бот хуйло ничтожество гей сосун лох бомж еблан лох бот гей трахнутый '
                                         'уебок негр мать в канаве еблан негр ахахаха уебан хуйло чмо чмо гей еблан '
                                         'попуск выебанный лох бомж лох сосун сосун выебанный ничтожество мразь '
                                         'попуск мразь уебан гей мать в канаве даун мразь глупый слабый абортыш '
                                         'кастрированный лох тупой ничтожество тупой гей уебок глупый гей тупой уебан '
                                         'слабый хуйло пидорас уебан бот хуйло тупой гей бот ничтожество'))


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
    elif message.text == 'Instagram Spammer':
        jopa = bot.send_message(message.chat.id, 'Enter number 380: ')
        bot.register_next_step_handler(jopa, setNumber)
    else:
        bot.send_message(message.chat.id, "I don't understand you")
        send_welcome(message)


bot.infinity_polling()
