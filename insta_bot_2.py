from instabot import Bot
import webbrowser
import time
import random
from database_controller import get_target, delet_target
user = input('Ведите имя  пользоватея  ').strip()
password = input('Ведите ваш пароль  ').strip()
target = []
get_target(target)
bot = Bot()
bot.login(username = user, password = password )
followers = bot.get_user_followers(target)
counter = len(target)
for follower in followers:
    bot.unfollow(follower)
    time.sleep(random.randrange(5-10))
    delet_target(follower)
    counter -=1
    print(f'Осталось {counter} oтписок')
    if counter == 0:
        bot.logout()

