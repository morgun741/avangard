import pandas as pd

# Загрузка данных из Excel
df = pd.read_excel('C:/Users/user/Downloads/train.xlsx')

# Разбиение на группы продаж с использованием квантилей
df['Sale_group'] = pd.qcut(df['Sales'], q=3, labels=['Малые продажи', 'Средние продажи', 'Высокие продажи'])

# Группировка данных по региону и группе продаж
region_sales_group = df.groupby(['Region', 'Sale_group']).size().unstack()

# Вывод данных по продажам в разрезе регионов и групп
print(region_sales_group)

# Поиск наиболее прибыльной группы продаж
most_profitable_group = df.groupby('Sale_group')['Sales'].sum().idxmax()
print(f'Наиболее прибыльная группа продаж: {most_profitable_group}')
