import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Updated Data
Methods = ['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5', 'All']
ACC = [0.78, 0.70, 0.70, 0.70, 0.77, 0.73]
AUC = [0.82, 0.73, 0.73, 0.74, 0.81, 0.77]
F1 = [0.85, 0.77, 0.77, 0.77, 0.83, 0.80]

# Set the width of the bars
bar_width = 0.2
# Set the position of the bars
index = np.arange(len(Methods))

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot each metric as a bar
bar1 = ax.bar(index - bar_width, ACC, bar_width, label='ACC')
bar2 = ax.bar(index, AUC, bar_width, label='AUC')
bar3 = ax.bar(index + bar_width, F1, bar_width, label='F1')

# Add labels and title
ax.set_xlabel('Folds', fontsize=16)
ax.set_ylabel('Values', fontsize=16)
ax.set_title('Five-fold cross validation result', fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels(Methods, rotation=30, fontsize=16)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.tick_params(axis='y', labelsize=16)

# Set Y-axis interval to 0.2
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust the legend position to the center of the image
#ax.legend(fontsize=12, loc='center', bbox_to_anchor=(0.5, 0.8))

# Display the figure
plt.tight_layout()
plt.savefig('fig-1a.pdf')
plt.show()
