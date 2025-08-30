import pandas as pd
import numpy as np

# pandas
df=pd.read_csv("python/HW8/customers.csv")

df['age'] = np.random.randint(18, 68, size=len(df))  # новый столбец 'age' со случайными значениями
df['type of product'] = np.random.randint(1, 4, size=len(df))  # новый столбец 'type of product' со случайными значениями
df['amount oders'] = np.random.randint(1, 10, size=len(df))  # новый столбец 'amount oders' со случайными значениями
df['price'] = np.random.randint(100, 5000, size=len(df))  # новый столбец 'price' со случайными значениями
df['nds'] = 0.2  # новый столбец 'nds' со значением 0.2
df['final_price'] = df['price'] * (1 + df['nds']).round(2)  # финальная стоимость с ндс

max_price = df.groupby('type of product')['final_price'].max()  # максимальная стоимость в каждой категории
print('Максимальное значение: ', max_price)

sum_price = df.groupby('type of product')['final_price'].sum()  # сумма стоимости в каждой категории
print('Сумма по категории: ', sum_price)

mean_price = df.groupby('type of product')['final_price'].mean()  # средняя стоимость в каждой категории
print('Среднее значение price:', mean_price)

expencive = df[df['final_price'] > 4000]  # стоимость больше 4000
print('Самый дорогой товар: ', expencive)

max_total_price = df.groupby('type of product')['final_price'].max()  # максимальная стоимость товара
print('Максимальная стоимость товара: ', max_total_price)

sorted_df = df.sort_values(by='final_price', ascending=False)  # сортирует DataFrame по столбцу 'final_price' в порядке убывания
print('Сортировка по final_price (по убыванию): ', sorted_df)

sorted_df = df.sort_values(by='age', ascending=True)  # сортирует DataFrame по столбцу 'age' в порядке возрастания
print('Сортировка по age (по возрастанию): ', sorted_df)

filter_age = df[df['age']>30]  # фильтр по столбцу 'age' больше 30

average_amount_oders = np.mean(df['amount oders'])  # среднее колличество заказов
print(f"Среднее количество заказов: {average_amount_oders}")

print(df.head()) # первые 5 строк
print(df.describe()) # статистика числовых столбцов
print(df[['age', 'price']]) # вывод столбцов 'age' и 'price'

# numpy
avr_total_price = np.mean(df['final_price'])
print(avr_total_price)

array = np.array(df['age'])
print(array)
print(np.mean(array))  # среднее значение элементов массива в столбце 'age'
