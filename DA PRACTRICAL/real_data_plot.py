import pandas as pd
import matplotlib.pyplot as plt

# Update 'data.csv' path if needed
data = pd.read_csv("data.csv")
print(data.head())

plt.figure(figsize=(8,5))
plt.plot(data['Time'], data['Value'], marker='o', linestyle='-')
plt.xlabel("Time"); plt.ylabel("Value"); plt.title("Real Data Plot from External Source")
plt.grid(True)
plt.show()
