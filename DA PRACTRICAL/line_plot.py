
"""Simple line graph using matplotlib"""
import matplotlib.pyplot as plt

def main():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Plotting the line graph
    plt.plot(x, y, marker='o', linestyle='-', label='y=2x')

    # Adding labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Simple Line Graph")
    plt.legend()
    plt.grid(True)

    # Display the graph
    plt.show()

if __name__ == '__main__':
    main()
