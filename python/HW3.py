# 1. Создайте переменную x и присвойте ей значение 10. Выведите значение переменной на экран.

x = 10 
print (x)

# 2. Создайте переменные name (строка), age (число) и is_student (булевый тип). Выведите их значения.

name = 'python'
age = 10
is_student = True
print(name)
print(age)
print(is_student)


# 3.  Напишите программу, которая запрашивает у пользователя три числа, сравнивает их между собой n/
# и выводит максимальное и  минимальное число

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a>=b and a>=c: # нахожу максимум
    max_number = a
    print(f'{a} больше, чем {b} и {c}') # сравниваю
elif b>=a and b>=c:
    max_number = b
    print(f'{b} больше, чем {c} и {a}')
else:
    max_number = c

if a<=b and a<=c: # нахожу минимум
    min_number = a
    print(f'{a} меньше, чем {b} и {c}') # сравниваю
elif b<=a and b<=c:
    min_number = b
    print(f'{b} меньше, чем {a} и {c}')
else:
    min_number = c

max_number = max(a, b, c)
min_number = min(a, b, c)

print('максимальное число: ', max_number)
print('минимальное: ', min_number)


# ДОПОЛНИТЕЛЬНО:
# 1. Напишите программу, которая запрашивает у пользователя его возраст, n/
# преобразует введенное значение в целое число, добавляет к нему 5 и n/
# выводит сообщение: "Через 5 лет вам будет X лет", где X — рассчитанное значение

age = int(input('Введите ваш возраст: '))
x = age + 5

print(f"Через пять лет вам будет: ", {x})


# 2. Количество чётных и нечётных чисел в диапазоне Задача: Пользователь вводит числа a и b (a ≤ b). n/
# Вывести количество чётных и нечётных чисел в этом диапазоне.
 
a = int(input('Введите первое число a: '))
b = int(input('Введите второе число b: '))
if a > b:
    print('Неверно! a должно быть меньше или равно b')
else:
    even = 0 # Четные
    odd = 0 # Нечетные

    for number in range (a, b + 1):
        if number % 2 == 0:
            even+= 1
        else:
            odd+= 1
    print('четных: ', even)
    print('нечетных: ', odd)


# Напишите программу,которая запрашивает у пользователя строку /n
# и выводит количество гласных и согласных букв в этой строке.

a = 'ayiuoe'
b = 'bcdfgklmnpqwxz'
our_srt = str(input())
a_count = 0
b_count = 0
for char in our_srt:
    if char in a:
        a_count = a_count + 1   
    elif char in b:
        b_count = b_count + 1
print(a_count, b_count, sep=';')