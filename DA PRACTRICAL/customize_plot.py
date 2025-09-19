import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

fig, ax = plt.subplots(figsize=(6,4))
fig.patch.set_facecolor("lightyellow")
ax.set_facecolor("lightblue")
ax.plot(x, y, marker='o', linestyle='--', label='Line')
ax.grid(True, linestyle=':', linewidth=1.2, color='black')
ax.set_title("Customized Plot", fontsize=18, fontweight='bold')
ax.set_xlabel("X-axis", fontsize=14); ax.set_ylabel("Y-axis", fontsize=14)
ax.tick_params(axis='both', labelsize=12)
ax.legend(fontsize=12)
plt.show()
