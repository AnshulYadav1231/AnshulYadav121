data = [50, 100, 75, 25]
total = sum(data)

print("Values:", data)
print("Total:", total)
print("\nPercentage Distribution:")
for i, value in enumerate(data, 1):
    percentage = (value / total) * 100
    print(f"Value {i}: {value} -> {percentage:.2f}%")
