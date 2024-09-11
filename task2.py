import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/user/Downloads/train.xlsx')
print(df.head())
plt.figure(figsize=(10, 6))
plt.boxplot(df['Sales'], vert=False)
plt.title('Коробочный сюжет для продаж')
plt.xlabel('Продажи')
plt.show()
mean_sales = df['Sales'].mean()
std_sales = df['Sales'].std()
lower_bound = mean_sales - 3 * std_sales
upper_bound = mean_sales + 3 * std_sales
filtered_sales = df[(df['Sales'] >= lower_bound) & (df['Sales'] <= upper_bound)]


plt.figure(figsize=(10, 6))
plt.boxplot(filtered_sales['Sales'], vert=False)
plt.title('Коробочный сюжет для продаж (без аномалий)')
plt.xlabel('Продажи')
plt.show()

