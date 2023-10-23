# В этом файле запросы для базы данны #
import sqlite3 as sql
querry_add_accounts = '''INSERT INTO unfollowers (username,insta_id,link,category) VALUES (?,?,?,?)''' # Запрос добавляет аккаунты в базу данных
querry_get_targets = '''SELECT insta_id,  FROM unfollowers'''# Запрос выводит целевые аккаунты в бот
querry_del_target = '''DELETE FROM unfollowers WHERE link LIKE ?'''#Запрос удалаяте аккаунты из базы данных после отписки


def add_accounts(a,b,c,d):
    '''Функция добавления аккаунтов в базу данныч'''
    try:
        with sql.connect('unfollowers.db') as conn:
            res = conn.cursor().execute(querry_add_accounts,(a,b,c,d))
            if res:
                return True
            return False
    except sql.ProgrammingError:
        return 'Ошибка запроса'
    except ConnectionError:
        return 'Ошибка подключения к базе'
    
def get_target(target):
    '''Функця получения всех аккаунов из базы данных'''
    try:
        with sql.connect('unfollowers.db') as conn:
            res = conn.cursor().execute(querry_get_targets).fetchall()
            for row in res:
                target.append(row)
            return target
    except sql.ProgrammingError:
        return 'Ошибка запроса'
    except ConnectionError:
        return 'Ошибка подключения к базе'

def delet_target(target):
    '''Функция удаления подписчика которого мы отписали из базы данных'''
    try:
        with sql.connect('unfollowers.db') as conn:
            for row in target:

                conn.cursor().execute(querry_del_target,(row[0]))
            return target
    except sql.ProgrammingError:
        return 'Ошибка запроса'
    except ConnectionError:
        return 'Ошибка подключения к базе'
