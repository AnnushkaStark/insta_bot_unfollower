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
from selenium.webdriver.common.action_chains import ActionChains

target = []
get_target(target)
print('Знаю кого нужно отписать')
counter = len(target)
print(counter)




browser = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
try:
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(3, 5))
    username = input('Введите ваш юзверьнейм   ')
    password = input('Введите ваш пароль   ')
    #username = 'vizhu-tebya@yandex.ru'
    #password = "Squre45"
    username_input = browser.find_element(by = By.NAME, value = 'username')
    username_input.clear()
    username_input.send_keys(username)
  
    time.sleep(2)
    #target1 = ['mahireser2023','leontieva789438','karpova981001']



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
    time.sleep(30)
    for user in target:
        try:
            browser.get('https://www.instagram.com/Zaceni_prikoll/followers/') #вот тут между знаками слэш вместо Zaceni_pricoll вписатьимяпользователя от которого нужно отписать подписчиков 
            time.sleep(70)
            follower = browser.find_element(by=By.CSS_SELECTOR,value= 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div')
            found_input = follower.find_element(by= By.XPATH, value = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/input')
            found_input.clear()
            found_input.send_keys(user)
            time.sleep(50)
            unfollower = follower.find_element(by=By.XPATH,value= '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a/div/div/span')
            if unfollower:
                button =unfollower.find_element(by=By.XPATH,value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/div')
                button.click()
                deleter = browser.find_element(by =By.CSS_SELECTOR,value = 'body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div')
                button  = deleter.find_element(by = By.CSS_SELECTOR,value = 'body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9-_')
                button.click()
                time.sleep(50)
                delet_target(user)
                time.sleep(30)
        except Exception:
            delet_target(user)
            button = follower.find_element(by=By.XPATH,value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button')
            button.click()
            continue
        
    browser.back()
    print("Ботяра работу закончил")
    time.sleep(50)   
   
        
except Exception:
    print('Что то пошло не так')
    time.sleep(500)
    