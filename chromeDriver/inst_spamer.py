from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\bomber-pyTelegramBotApi\chromeDriver\chromedriver.exe")
url = "https://www.instagram.com/"

try:
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


def startInstagram(link):
    pass



