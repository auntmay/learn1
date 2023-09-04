'''
типы данных:

integer
float
complex
bool
string
NoneType
list
tuple
set
frozenset
range
dictionary
bytes
byrearray
memoryview

'''

from datetime import datetime

dt_now = f'{datetime.now()}'
dt_now = dt_now.split('-')[0]

birth_year = int(input('Введите год рождения: '))
real_age = int(dt_now) - birth_year

print(real_age)