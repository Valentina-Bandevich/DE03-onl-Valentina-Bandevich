# 1. Напишите программу, которая запрашивает у пользователя строку /n
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

# 2. Напишите программу, которая запрашивает у пользователя числа, /n
# вычисляет их сумму и среднее значение. Программа должна использовать /n
# циклы для обработки ввода и условные операторы для проверки корректности ввода.

sum_numbers = 0
count = 0
print ("Введите числа по одному. Для завершения введите 'stop': ")
while True:
    user_input = input('Введите число: ')
    if user_input == 'stop':
        if count == '0':
            print('Некорректный ввод.') 
        else:   
            print(f'Сумма введенных чисел: {sum_numbers}')
            print(f'Среднее значение: {sum_numbers / count}')   
        break
    try:
        number = int(user_input)
        sum_numbers += number
        count += 1
    except ValueError:
        print("Некорректный ввод. Введите число или 'stop' для завершения.")  


# 3. Разработайте программу, которая запрашивает у пользователя число /n
# и выводит таблицу умножения для этого числа до 10.

number = int(input('Введите число: '))
print(f'таблица умножения для числа {number}:')
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")