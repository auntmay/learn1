def cut_cake(persons):
    try:
        parts = 1 / persons
        print(f'Каждый человек получит {parts} пирога')
    except (ZeroDivisionError, TypeError):
        print('Не могу делить.')

cut_cake(0)
cut_cake('124')