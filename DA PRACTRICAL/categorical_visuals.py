
"""Bar chart and pie chart for categorical data using seaborn + matplotlib"""
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Example categorical data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 12, 36, 29]

    # Bar chart
    plt.figure(figsize=(7, 5))
    sns.barplot(x=categories, y=values, palette="viridis")
    plt.title("Bar Chart - Categorical Data")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()

    # Pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140,
            colors=sns.color_palette("viridis"))
    plt.title("Pie Chart - Categorical Data")
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    main()
