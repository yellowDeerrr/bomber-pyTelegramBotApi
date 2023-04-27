from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"C:\bomber-pyTelegramBotApi\chromeDriver\chromedriver.exe")
url = "https://www.instagram.com/"

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


def startInstagram(link):
    pass



