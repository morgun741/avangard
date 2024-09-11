import pandas as pd
import matplotlib.pyplot as plt

#Загрузка данных
data = pd.read_excel('/mnt/data/train.xlsx')
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%Y-%m-%d')

#a) Наиболее часто покупаемые подгруппы за все время
subcat_all_time = data['Sub-Category'].value_counts().nlargest(4)

#b) Наиболее часто покупаемые подгруппы за последние два года
last_two_years = data[data['Order Date'] >= (data['Order Date'].max() - pd.DateOffset(years=2))]
subcat_last_two_years = last_two_years['Sub-Category'].value_counts().nlargest(4)

#c) Наиболее часто покупаемые подгруппы за последний год
last_year = data[data['Order Date'] >= (data['Order Date'].max() - pd.DateOffset(years=1))]
subcat_last_year = last_year['Sub-Category'].value_counts().nlargest(4)

#Визуализация
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

#Подгруппы за все время
axes[0].bar(subcat_all_time.index, subcat_all_time.values, color='blue')
axes[0].set_title('Часто покупаемые подгруппы (Все время)')
axes[0].set_ylabel('Частота покупок')

#Подгруппы за последние два года
axes[1].bar(subcat_last_two_years.index, subcat_last_two_years.values, color='green')
axes[1].set_title('Часто покупаемые подгруппы (Последние 2 года)')

#Подгруппы за последний год
axes[2].bar(subcat_last_year.index, subcat_last_year.values, color='red')
axes[2].set_title('Часто покупаемые подгруппы (Последний год)')

plt.tight_layout()
plt.show()