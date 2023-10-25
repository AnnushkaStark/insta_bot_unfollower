# В этом файле запросы для базы данны #
import sqlite3 as sql
querry_add_accounts = '''INSERT INTO trash_accounts (username,insta_id,link,category) VALUES (?,?,?,?)''' # Запрос добавляет аккаунты в базу данных
querry_get_targets = '''SELECT insta_id  FROM trash_accounts'''# Запрос выводит целевые аккаунты в бот
querry_del_target = '''DELETE FROM  trash_accounts WHERE insta_id LIKE ?'''#Запрос удалаяте аккаунты из базы данных после отписки


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
    
def get_target(target:list):
    '''Функця получения всех аккаунов из базы данных'''
    try:
        with sql.connect('unfollowers.db') as conn:
            res = conn.cursor().execute(querry_get_targets).fetchall()
            for row in res:
                target.append(row[0])
            return target
    except sql.ProgrammingError:
        return 'Ошибка запроса'
    except ConnectionError:
        return 'Ошибка подключения к базе'

def delet_target(follower):
    '''Функция удаления подписчика которого мы отписали из базы данных'''
    try:
        with sql.connect('unfollowers.db') as conn:
            res = conn.cursor().execute(querry_del_target,(follower,))
            if res:
                return (f' id {follower} отписан от вас')
    except sql.ProgrammingError:
        return 'Ошибка запроса'
    except ConnectionError:
        return 'Ошибка подключения к базе'

#target =  []
#get_target(target)