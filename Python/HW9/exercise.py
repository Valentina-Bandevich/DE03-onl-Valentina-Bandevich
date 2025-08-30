"""Напишите программу на Python, которая загружает данные из CSV файла, очищает их 
(удаляет пропущенные значения и дубликаты) и выводит итоговый DataFrame"""

import pandas as pd

df = pd.read_csv('Python/HW9/data.csv')
print (df)
# df = df.drop_dublicates(subset=['customer_name'])
# df = df.fillna({'product': 'Unknown'})
df = df.dropna()
df["total_price"] = df ["quantity"]*df["price"]
sort = df[df["product"]=="Mouse"]
print(df)

df['order_date'] = df['order_date'].astype('datetime64[ns]')
df.info()
sors_volue = df.sort_values(by = 'order_date', ascending=False)
print(sors_volue)