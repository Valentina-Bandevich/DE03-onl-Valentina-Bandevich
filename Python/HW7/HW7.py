"""1.Напишите функцию, которая принимает список чисел и возвращает их среднее значение. 
Обработайте исключения, связанные с пустым списком и некорректными типами данных."""

# def calculate_average(numbers):
#     if not numbers:
#         raise ValueError("Список не может быть пустым")
#     try:
#         return sum(numbers) / len(numbers)
#     except TypeError:
#         raise TypeError("Список должен содержать только числа")
# print(calculate_average([1, 2, 3, 4]))
# print(calculate_average([]))
# print(calculate_average([1, 2, 'три', 4]))


"""2. Создайте программу, которая считывает список чисел из файла, 
проверяет каждое число на чётность и записывает результаты (чётное или нечётное) в другой файл. 
Используйте обработку исключений для возможных ошибок ввода-вывода."""

# input_file = "r"Python/HW7/input.txt""
# output_file = "r"Python/HW7/output.txt""
def process_numbers(input_file, output_file): # input - файл с числами, output - файл с результатами
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                line = line.strip()
                if line:
                    try:
                        number = int (line) # Преобразуем строку в число
                        if number % 2 == 0:
                            result = f"{number} - Чётное"
                        else:
                            result = f"{number} - Нечётное"
                        outfile.write(result)
                    except ValueError:
                        outfile.write(f"Ошибка: '{line}' - не целое число\n")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except IOError:
        print(f"Ошибка: Произошла ошибка ввода-вывода при работе с файлами.")
input_file = 'input.txt'
output_file = 'output.txt'     
process_numbers(input_file, output_file)
print(f"Проверка завершена. Результаты записаны в '{r'output_filePython/HW7/output.txt'}'.")

    