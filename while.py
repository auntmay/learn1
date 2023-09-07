"""

while True:
    user_say = input('Скажи что-нибудь:')
    if user_say == 'Пока':
        print('Ну пока.')
        break
    else:
        print('Сам ты {}!'.format(user_say))
        
______________________________________________________________
        

names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name_to_find, names_array):
    for name in names_array:
        if name == name_to_find:
            print('{} нашелся!'.format(name_to_find))
            break

find_person('Саша', names)

______________________________________________________________


def find_person(name_to_find, names_array):
    for name in names_array:
        if name == name_to_find:
            print('{} нашелся!'.format(name_to_find))
            break
        else:
            names_array = names_array

find_person('Саша', names)

______________________________________________________________

names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name_to_find, names_array):
    while names_array[0] != name_to_find:
        print(names_array.pop(0))

    print('{} нашелся!'.format(name_to_find))

find_person('Саша', names)

______________________________________________________________


def ask_user(howsgoing = input('Как дела?')):
    while howsgoing != 'Хорошо':
        howsgoing = str(input('Как дела?'))

ask_user()

______________________________________________________________

def hello_user():
    while True:
        try:
            user_say = input('Скажи что-нибудь:')
            if user_say == 'Пока':
                print('Ну пока.')
                break
            else:
                print('Сам ты {}!'.format(user_say))
        except KeyboardInterrupt:
            print()
            print('Пока!')
            break

hello_user()

"""