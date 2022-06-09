import time
import os

def question():
    print('Программа для работы с процентами')
    time.sleep(2)
    print('Выберите, что требуется сделать...')
    print('1. Найти процент от числа \n2. Узнать сколько процентов составляет число X от числа Y \n3. Узнать полное число от его процента \n4. Прибавить процент к числу \n5. Вычесть процент от числа')
    time.sleep(2)

def answer():
    task = input('Введите номер задания: ')
    os.system('cls')
    if task == '1':
        print('Найти процент от числа')
        time.sleep(2)
        x = float(input('Введите процент: '))
        n = float(input('Введите число: '))
        time.sleep(2)
        print(f'Требуется найти {x} процентов от числа {n}')
        a = n*x/100
        time.sleep(2)
        print(f'Ответ: {a}')

    elif task == '2':
        print('Узнать сколько процентов составляет число X от числа Y')
        time.sleep(2)
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        time.sleep(2)
        print(f'Требуется узнать сколько процентов составляет число {x} от числа {y}')
        a = x*100/y
        time.sleep(2)
        print(f'Ответ: {a}')

    elif task == '3':
        print('Узнать полное число от его процента')
        time.sleep(2)
        n = float(input('Введите число: '))
        x = float(input('Введите процент: '))
        time.sleep(2)
        print(f'Требуется узнать - число {n} это {x} процентов какого числа?')
        a = n*100/x
        time.sleep(2)
        print(f'Ответ: {a}')

    elif task == '4':
        print('Прибавить процент к числу')
        time.sleep(2)
        z = float(input('Введите процент: '))
        n = float(input('Введите число: '))
        time.sleep(2)
        print(f'Требуется прибавить {z} процентов к числу {n}')
        y = 100+z
        x = n*y/100
        time.sleep(2)
        print(f'Ответ: {x}')

    elif task == '5':
        print('Вычесть процент от числа')
        time.sleep(2)
        z = float(input('Введите процент: '))
        n = float(input('Введите число: '))
        time.sleep(2)
        print(f'Требуется вычесть {z} процентов от числа {n}')
        y = 100-z
        x = n*y/100
        time.sleep(2)
        print(f'Ответ: {x}')

question()
answer()

while True:
    end = input('\nХотите продолжить? \n1. Да \n2. Нет \n')
    if end.lower() == 'да' or end == '1':
        os.system('cls')
        question()
        answer()

    else:
        break