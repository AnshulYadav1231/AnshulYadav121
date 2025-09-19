import matplotlib.pyplot as plt

subjects = ['Maths', 'Science', 'English', 'History', 'Computer']
marks = [85,78,92,74,88]

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(subjects, marks, edgecolor='black')
plt.title("Marks in Subjects (Vertical Bar Chart)")
plt.xlabel("Subjects"); plt.ylabel("Marks")

plt.subplot(1,2,2)
plt.barh(subjects, marks, edgecolor='black')
plt.title("Marks in Subjects (Horizontal Bar Chart)")
plt.xlabel("Marks"); plt.ylabel("Subjects")

plt.tight_layout()
plt.show()
