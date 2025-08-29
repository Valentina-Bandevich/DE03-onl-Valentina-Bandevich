
""" Загрузите данные из CSV файла """

import numpy as np
import pandas as pd

df=pd.read_csv(r'python/sales.csv')
print(df)


""" Выполните основные операции с данными: фильтрация,
сортировка, агрегация с использованием pandas """

prices = [10.99, 20.50, 15.75, 30.00, 25.00, 18.25, 22.10]
df['price'] = prices
print(df)

count = [56, 24, 12, 5, 6, 23, 4]
df['count'] = count
print(df)

df['total_price'] = df['price']* df['count']
low_counterbale = df[df['count']<12]
print(f'мало продаваемый товар: {low_counterbale}')

sorted = df.sort_values(by='total_price')
print(f'{sorted}')

max_total_price = df.groupby('category')['total_price'].max()
print(max_total_price)


""" Применить numpy для числовых вычислений """

avr_total_price = np.mean(df['total_price'])
print(avr_total_price)

value = np.median(df['total_price'])
print(value)