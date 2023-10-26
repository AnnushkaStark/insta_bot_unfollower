from instabot import Bot
import webbrowser 
import time
import random
from database_controller import get_target, delet_target

from instabot.api import API
from instabot.api import api_login
print('Пытаюсь войти  в систему')
target = []
get_target(target)
print('Знаю кого нужно отписать')
bot = Bot()
api = API(bot)
bot.login()
time.sleep(random.randrange(5-10))
counter = len(target)
time.sleep(random.randrange(5-10))
for follower in target:
    time.sleep(random.randrange(5-10))
    user_info = bot.get_user_info(follower)
    bot.like_followers(follower)
    bot.unfollow(follower)
    time.sleep(random.randrange(5-10))
    delet_target(follower)
    time.sleep(random.randrange(5-10))
    counter -=1
    time.sleep(random.randrange(5-10))
    print(f'Осталось {counter} oтписок')
if counter == 0:
    print('Аккаунты отписаны')
if counter == len(target):
    print('Вы не были подписаны на этих людей')
    
bot.logout()

