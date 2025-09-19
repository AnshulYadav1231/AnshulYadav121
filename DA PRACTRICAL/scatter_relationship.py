import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Hours_Studied': [1,2,3,4,5,6,7,8,9,10],
    'Exam_Score':    [40,45,50,55,60,65,70,75,85,95]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8,6))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', data=df, s=80)
sns.regplot(x='Hours_Studied', y='Exam_Score', data=df, scatter=False)
plt.title("Relationship Between Hours Studied and Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()
