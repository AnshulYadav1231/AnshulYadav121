import matplotlib.pyplot as plt
import seaborn as sns

class_A_scores = [55,60,65,70,72,75,78,80,82,85,88,90,92,95]
class_B_scores = [50,52,58,62,67,73,76,79,81,83,87,89,91,94]

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
sns.histplot(class_A_scores, kde=True, label="Class A", bins=8, alpha=0.6)
sns.histplot(class_B_scores, kde=True, label="Class B", bins=8, alpha=0.6)
plt.title("Distribution of Test Scores (Histogram)")
plt.xlabel("Scores"); plt.ylabel("Frequency"); plt.legend()

plt.subplot(1,2,2)
sns.boxplot(data=[class_A_scores, class_B_scores])
plt.xticks([0,1], ["Class A","Class B"])
plt.title("Comparison of Test Scores (Boxplot)")
plt.ylabel("Scores")

plt.tight_layout()
plt.show()
