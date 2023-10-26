from instabot import Bot
import webbrowser
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from database_controller import get_target, delet_target
from instabot.api import API


browser = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
try:
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(3, 5))
    #username = 'TatyanaF7222@yandex.ru'
    #password = "tanaavde123!"
    username = 'nataly72.os@yandex.ru'
    password = "NataliaOS1!"
    username_input = browser.find_element(by = By.NAME, value = 'username')
    username_input.clear()
    username_input.send_keys(username)
    target = []
    get_target(target)
    print('Знаю кого нужно отписать')
  
    time.sleep(2)
  
    password_input = browser.find_element(by = By.NAME, value ="password")
    password_input.clear()
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)
    time.sleep(30)
    button = browser.find_element(by=By.CLASS_NAME,value="_ac8f")
    button.click()
    time.sleep(50)
    #time.sleep(20)
    button = browser.find_element(by=By.XPATH,value="//button[text()= 'Не сейчас']")
    button.click()
    time.sleep(300)
    button = browser.find_element(by=By.XPATH,value='//*[@id="mount_0_0_d/"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[6]/div/span/div/a/div/div/div/div/span/img')
    button.click()
    time.sleep(50)
    button = browser.find_element(by=By.XPATH,value='//*[@id="mount_0_0_d/"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span')
    button.click()
    time.sleep(20)
    
        
except Exception as ex:
    print(ex)