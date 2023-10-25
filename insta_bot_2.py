from instabot import Bot
import webbrowser
import time
import random
from database_controller import get_target, delet_target
user = input('Ведите имя  пользоватея  ').strip()
password = input('Ведите ваш пароль  ').strip()
print('Пытаюсь войти  в систему')
target = []
get_target(target)
print('Знаю кого нужно отписать')
bot = Bot()
bot.login(username = user, password = password )
print('Бот вошел  в аккаун')
time.sleep(random.randrange(5-10))
counter = len(target)
time.sleep(random.randrange(5-10))
for follower in target:
    time.sleep(random.randrange(5-10))
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

