
"""Calculate and print percentage distribution for a list of numbers"""
def percentage_distribution(data):
    total = sum(data)
    if total == 0:
        raise ValueError("Total of data is zero — cannot compute percentages.")
    result = []
    for i, value in enumerate(data, 1):
        percentage = (value / total) * 100
        result.append((i, value, percentage))
    return result

def main():
    # Sample data (can be marks, expenses, etc.)
    data = [50, 100, 75, 25]

    print("Values:", data)
    print("Total:", sum(data))
    print("\nPercentage Distribution:")

    for idx, value, pct in percentage_distribution(data):
        print(f"Value {idx}: {value} → {pct:.2f}%")

if __name__ == '__main__':
    main()
