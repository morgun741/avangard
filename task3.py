import pandas as pd

df = pd.read_excel('C:/Users/user/Downloads/train.xlsx')
df['Sale_group'] = pd.qcut(df['Sales'], q=3, labels=['Малые продажи', 'Средние продажи', 'Высокие продажи'])
region_sales_group = df.groupby(['Region', 'Sale_group']).size().unstack()
print(region_sales_group)

most_profitable_group = df.groupby('Sale_group')['Sales'].sum().idxmax()
print(f'Наиболее прибыльная группа продаж: {most_profitable_group}')
