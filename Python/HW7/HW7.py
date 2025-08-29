"""1.Напишите функцию, которая принимает список чисел и возвращает их среднее значение. 
Обработайте исключения, связанные с пустым списком и некорректными типами данных."""

def calculate_average(numbers):
    if not numbers:
        raise ValueError("Список не может быть пустым")
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError("Список должен содержать только числа")
print(calculate_average([1, 2, 3, 4]))
print(calculate_average([]))
print(calculate_average([1, 2, 'три', 4]))


"""2. Создайте программу, которая считывает список чисел из файла, 
проверяет каждое число на чётность и записывает результаты (чётное или нечётное) в другой файл. 
Используйте обработку исключений для возможных ошибок ввода-вывода."""

try:
    with open(r"Python/HW7/input.txt", "r+", encoding = "utf-8") as input_file:
        list = input_file.readlines()
        for i in list:
            output_file = open(r"Python/HW7/output.txt", "a+", encoding = "utf-8")
            if int(i) % 2 == 0:
                output_file.write(f"Чётное число: {i}")
            else:
                output_file.write(f"Нечётное число: {i}")
            output_file.close
except PermissionError:
    print('Нет доступа к файлу!')
except FileNotFoundError:
    print("Файл не найден!")
except IOError:
    print("Ошибка ввода-вывода файла")
except IsADirectoryError:
    print("Указан пусть к папке, а не к файлу")
except UnicodeDecodeError:
    print("Неправильная кодировка файла")
else:
    print("Файл успешно прочитан!")
finally:
    print("Завершение обработки файла.")




    