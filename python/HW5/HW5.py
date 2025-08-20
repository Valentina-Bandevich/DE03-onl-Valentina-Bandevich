"""1.Откройте файл example.txt и выведите его содержимое на экран."""

with open(r"python/example.txt", "r") as file:
    content=file.read()
    print(content)


"""2. Создайте файл output.txt и запишите в него строку "Hello, World!" """

with open(r"python/output.txt", "r+") as file:
    file.write ('Hello, World!')
    content=file.read()
    print(content)


"""3.  Напишите программу, которая считает количество строк, 
слов и символов в заданном текстовом файле и выводит результаты."""

with open(r"python/example.txt", "r") as file:
    content=file.read()
    lines = content.count('\n')+1
    words = len(content.split())
    chars = len(content)
print(f"Строк: {lines} \nСлов: {words} \nСимволов: {chars}")