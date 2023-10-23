# В этом файле запросы для базы данны #
import sqlite3 as sql
querry_add_accounts = '''INSERT INTO unfollowers (username,insta_id,link,category) VALUES (?,?,?,?)''' # Запрос добавляет аккаунты в базу данных
querry_get_targets = '''SELECT username insta_id FROM unfollowers'''# Запрос выводит целевые аккаунты в бот
querry_del_target = '''DELETE FROM unfollowers WHERE username LIKE ? OR insta_id LIKE ?'''#Запрос удалаяте аккаунты из базы данных после отписки
  
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