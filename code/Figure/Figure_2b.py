import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

Methods = ['CamSol', 'Protein-Sol', 'PaRSnIP', 'DeepSol-S2', 'SKADE', 'SWI', 'SoluProt', 'GraphSol', 'EPSOL', 'NetSolP', 'DeepSoluE', 'HybridGCN', 'ProG-SOL']
ACC = [0.57, 0.65, 0.55, 0.45, 0.39, 0.68, 0.62, 0.65, 0.52, 0.73, 0.64, 0.65, 0.74]
AUC = [0.64, 0.68, 0.66, 0.60, 0.54, 0.69, 0.63, 0.68, 0.65, 0.76, 0.66, 0.69, 0.78]
F1 = [0.59, 0.74, 0.54, 0.31, 0.16, 0.77, 0.71, 0.73, 0.48, 0.79, 0.71, 0.72, 0.81]

bar_width = 0.2
index = np.arange(len(Methods))

fig, ax = plt.subplots(figsize=(8, 6))

bar1 = ax.bar(index - bar_width, ACC, bar_width, label='ACC')
bar2 = ax.bar(index, AUC, bar_width, label='AUC')
bar3 = ax.bar(index + bar_width, F1, bar_width, label='F1')

ax.set_xlabel('Methods', fontsize=16)
ax.set_ylabel('Values', fontsize=16)
ax.set_title('Performance on NESG dataset', fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels(methods, rotation=45, fontsize=16)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.tick_params(axis='y', labelsize=16)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#ax.legend(fontsize=20, loc='center', bbox_to_anchor=(0.5, 0.5))

plt.tight_layout()
plt.savefig('fig-2b.pdf')
plt.show()
