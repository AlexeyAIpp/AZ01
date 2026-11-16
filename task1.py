import pandas as pd

# 1. Загружаем набор данных из CSV-файла в DataFrame
df = pd.read_csv(
    "World-happiness-report-updated_2024.csv",
    encoding="cp1252"
)

# 2. Выводим первые 5 строк
print("Первые 5 строк данных:")
print(df.head())

# 3. Выводим информацию о данных
print("\nИнформация о данных:")
df.info()

# 4. Выводим статистическое описание
print("\nСтатистическое описание:")
print(df.describe())