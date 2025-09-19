import matplotlib.pyplot as plt
import seaborn as sns

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 12, 36, 29]

plt.figure(figsize=(7, 5))
sns.barplot(x=categories, y=values, palette="viridis")
plt.title("Bar Chart - Categorical Data")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140,
        colors=sns.color_palette("viridis"))
plt.title("Pie Chart - Categorical Data")
plt.show()
