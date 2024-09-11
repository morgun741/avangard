import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из Excel (укажите правильный путь к вашему файлу)
df = pd.read_excel('C:/Users/user/Downloads/train.xlsx')

# Проверка загрузки данных
print(df.head())

# Построение коробочного сюжета для продаж (Sales)
plt.figure(figsize=(10, 6))
plt.boxplot(df['Sales'], vert=False)
plt.title('Коробочный сюжет для продаж')
plt.xlabel('Продажи')
plt.show()

# Применим правило трех сигм для удаления выбросов
mean_sales = df['Sales'].mean()
std_sales = df['Sales'].std()

# Границы по правилу трех сигм
lower_bound = mean_sales - 3 * std_sales
upper_bound = mean_sales + 3 * std_sales

# Фильтрация данных для исключения аномалий
filtered_sales = df[(df['Sales'] >= lower_bound) & (df['Sales'] <= upper_bound)]

# Построение обновленного коробочного сюжета без аномалий
plt.figure(figsize=(10, 6))
plt.boxplot(filtered_sales['Sales'], vert=False)
plt.title('Коробочный сюжет для продаж (без аномалий)')
plt.xlabel('Продажи')
plt.show()

