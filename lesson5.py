# JSON(javascript object natation)универсальный формат для передачи данных 

# import json
# db = {'name': 'Tom', 'age': 30, 'gender': 'male'}
# json_obj = json.dumps(db)
# # print(json_obj)
# python_obj = json.loads(json_obj)
# print(python_obj)

# Python            JSON
# dict              object
# list              Array(массив)
# set               -
# str               String
# int               Number
# float             Number
# True              true
# False             false
# None              null
# tuple             Array

# import json
# dict1 = {'name': 'Tom', 'age': 30, 'gender': 'male'}
# with open('db.json', 'a+') as f: 
#     json.dump(dict1, f)

# import json
# with open('db.json', 'r+') as f:
#     python_obj = json.loads(f.read())
#     print(python_obj)

# import json
# with open('db.json', 'r+') as f:
# #     python_obj = json.load(f)
# #     print(python_obj)
#       print(f)

# import json
# with open('db.json', 'r+') as f:
#     python_obj = json.load(f)
#     print(python_obj)

# Написать программу, которая запрашивает у 
# пользователя данные такие как:
# Имя персонажа, его силу атаки(макс 100) 
# и его ловкость(макс 100), 
# затем сохраняет данные в файл db.json и 
# сохраняет до тех пор, 
# пока пользоваетль не решит сам остановиться. 
# Также есть функция, 
# которая в рандомном порядке вытаскивает 2х 
# игроков(использовать библиотеку random) 
# и между ними идет бой, победит тот у кого больше 
# силы и ловкости, если у первого игрока силы больше, 
# но ловкости меньше мин на 10 пунктов, то побеждает 
# игрок у которого больше ловкости,
# после боя программа спрашивает у пользователя хочет 
# ли он устроить еще один 
# бой либо добавить еще одного игрока или может вообще 
# выйти из игры.
# Вывод программы должен сопровождаться сообщениями 
# типа: Данные сохранены!, Бой начался!, 
# Победил игрок: Игрок1! и тд.

import json

db = []

def battle():
    pass 
def write_db():
    global db
    name_of_hero = input('Введите имя героя: ')
    power_of_hero = input('Введите силу героя(макс100): ')
    agility_of_hero = input('Введите ловкость героя(макс100): ')
    new_db = {"name": name_of_hero,"power": power_of_hero,"agility": agility_of_hero}

    with open('db.json', 'r+') as f:
        db = json.loads(f.read())
        db.append(new_db)

    with open('db.json', 'w+') as j:
        json.dump(db, j)

    answ = input('Данные записаны! Добавить еще? db/f')
    if answ == 'db':
        write_db()
    elif answ == 'f':
        battle
    else:
            print('До встречи!')


def manager():
    answ = input('Вы хотите добавить данные или устроить бой? db/f')
    if answ  == 'db':
        write_db()
    elif answ == 'f':
        battle()
    else:
        print('Введены неккоректные данные!')

manager()


