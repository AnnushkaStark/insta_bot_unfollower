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
    #username = input('Введите ваш юзверьнейм   ')
    #password = input('Введите ваш пароль   ')
    username = 'vizhu-tebya@yandex.ru'
    password = "Squre45"
    username_input = browser.find_element(by = By.NAME, value = 'username')
    username_input.clear()
    username_input.send_keys(username)
  
    time.sleep(2)
    target1 = ['_enaivanina','maksym_frelanser','malysheva657425','klimova584596','krylova555262']


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
    browser.get('https://www.instagram.com/vrrbens1717/followers/') #вот тут между знаками слэш вместо Zaceni_pricoll вписатьимяпользователя от которого нужно отписать подписчиков 
    time.sleep(50)
    follower = browser.find_element(by=By.CSS_SELECTOR,value= 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div')
    time.sleep(30)
    loops_count = int(len(target) / 12)
    actions = ActionChains(browser)
    actions.move_to_element(follower)
    actions_speed = 1.5
    scroller =follower.find_element(by= By.CSS_SELECTOR,value= 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano')
    actions = ActionChains(browser)
    actions.move_to_element(follower)
    time.sleep = actions_speed = 1.5
    unfollows = follower.find_elements(by=By.XPATH,value= '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a/div/div/span')
    for unfollow in unfollows:
        unfollower = unfollow.text
        print(unfollower)
        if unfollower  in target1:
            button =unfollow.find_element(by=By.XPATH,value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/div')
            button.click()
            #button = follower.find_element(by= By.CSS_SELECTOR, value = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div > div')
            time.sleep(5)
            time.sleep(12)
            deleter = browser.find_element(by =By.CSS_SELECTOR,value = 'body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div')
            time.sleep(10)
            button  = deleter.find_element(by = By.CSS_SELECTOR,value = "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9-_")
            button.click()
            time.sleep(20)
            continue
        for i in range(0,200,300):
            browser.execute_script(f'window.scrollTo({i},{i + 200})')
    time.sleep(random.randrange(200,500))
    #time.sleep(500)
    
        
except Exception as ex:
    print(ex)