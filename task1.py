import pandas as pd

# Загрузка данных
df = pd.read_excel('C:/Users/user/Downloads/train.xlsx')

# Преобразуем колонку с датами в формат datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# а) Наиболее часто покупаемые подгруппы товаров за всё время продаж
top_subcategories_all_time = df['Sub-Category'].value_counts().head(4)

# б) Наиболее часто покупаемые подгруппы товаров за последние два года
latest_two_years = df[df['Order Date'] >= pd.Timestamp.now() - pd.DateOffset(years=2)]
top_subcategories_last_two_years = latest_two_years['Sub-Category'].value_counts().head(4)

# в) Наиболее часто покупаемые подгруппы товаров за последний год
latest_one_year = df[df['Order Date'] >= pd.Timestamp.now() - pd.DateOffset(years=1)]
top_subcategories_last_one_year = latest_one_year['Sub-Category'].value_counts().head(4)

# Вывод результатов
print("Наиболее часто покупаемые подгруппы за всё время:")
print(top_subcategories_all_time)

print("\nНаиболее часто покупаемые подгруппы за последние два года:")
print(top_subcategories_last_two_years)

print("\nНаиболее часто покупаемые подгруппы за последний год:")
print(top_subcategories_last_one_year)
