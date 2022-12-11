day = int(input('Введите число от 1 до 7: '))
if day > 0 and day < 6:
    print('Рабочий день')
elif day > 5 and day < 8:
    print('Выходной')
else:
    print('Введите число от 1 до 7')
