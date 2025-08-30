"""Создайте программу, которая загружает данные из REST API, выполняет предварительную обработку данных
(удаление пропущенных значений, преобразование типов), и сохраняет очищенные данные в новый CSV файл."""

import requests
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/users')   # загрузка из API

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")

# df = df.drop_duplicates(subset=['customer_name']) # удаление строк с пропущенными значениями

df_clean = df.dropna ()   # удаление строк с пропущенными значениями
df_clean.to_csv('Python/HW9/cleaned_data.csv', index = False)   # сохранение в CSV
print('Данные сохранены в cleaned_data.csv')