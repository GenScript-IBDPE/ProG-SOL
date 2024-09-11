import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


methods = ['CamSol', 'Protein-Sol', 'PaRSnIP', 'DeepSol-S2', 'SKADE', 'SWI', 'SoluProt', 'GraphSol', 'EPSOL', 'NetSolP', 'DeepSoluE', 'HybridGCN', 'ProG-SOL']
ACC = [0.60, 0.78, 0.58, 0.44, 0.29, 0.78, 0.75, 0.82, 0.60, 0.51, 0.74, 0.82, 0.85]
AUC = [0.80, 0.86, 0.51, 0.52, 0.75, 0.82, 0.61, 0.85, 0.56, 0.82, 0.62, 0.87, 0.89]
F1 = [0.64, 0.83, 0.71, 0.50, 0.11, 0.87, 0.85, 0.87, 0.72, 0.51, 0.85, 0.87, 0.90]
PCC = [0.44, 0.53, 0.04, 0.08, 0.29, 0.45, 0.18, 0.57, 0.11, 0.53, 0.19, 0.60, 0.64]

bar_width = 0.2
index = np.arange(len(methods))

fig, ax = plt.subplots(figsize=(8, 6))

bar1 = ax.bar(index - 1.5*bar_width, ACC, bar_width, label='ACC')
bar2 = ax.bar(index - 0.5*bar_width, AUC, bar_width, label='AUC')
bar3 = ax.bar(index + 0.5*bar_width, F1, bar_width, label='F1')
bar4 = ax.bar(index + 1.5*bar_width, PCC, bar_width, label='PCC')


ax.set_xlabel('Methods', fontsize=16)
ax.set_ylabel('Values', fontsize=16)
ax.set_title('Performance on S. cerevisiae dataset', fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels(methods, rotation=45, fontsize=16)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.tick_params(axis='y', labelsize=16)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.tight_layout()
plt.savefig('fig-1d.pdf')
plt.show()
