import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Apply seaborn style
sns.set(style="whitegrid")

# Data
time = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
flow = np.array([5734.04, 5748.32, 5761.76, 5775.12, 5786.27, 5799.65, 5812.54,
                 5825.02, 5839.25, 5853.14, 5867.42, 5880.06, 5893.44])

# Linear regression
slope, intercept = np.polyfit(time, flow, 1)
regression_line = slope * time + intercept

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(time, flow, 'o', color='royalblue', label='Measured Flow', markersize=7)
plt.plot(time, regression_line, '--', color='crimson', label=f'Regression Line\nF = {slope:.2f}t + {intercept:.2f}', linewidth=2)

# Titles and labels
plt.title('Flow Rate vs Time', fontsize=16, weight='bold')
plt.xlabel('Time (minutes)', fontsize=14)
plt.ylabel('Flow (liters)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Grid, legend, and layout
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()

# Show plot
plt.show()

# Print gradient
print(f"Gradient (slope) of the regression line: {slope:.4f} liters/min")

