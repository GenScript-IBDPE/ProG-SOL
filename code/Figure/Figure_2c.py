import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

Methods = ['CamSol', 'PaRSnIP', 'DeepSol-S2', 'SKADE', 'SWI', 'SoluProt', 'EPSOL', 'NetSolP', 'DeepSoluE', 'ProG-SOL']
ACC = [0.70, 0.46, 0.45, 0.45, 0.63, 0.66, 0.45, 0.64, 0.66, 0.76]
AUC = [0.79, 0.70, 0.64, 0.59, 0.83, 0.72, 0.72, 0.74, 0.74, 0.85]
F1 = [0.60, 0.62, 0.62, 0.62, 0.70, 0.67, 0.62, 0.65, 0.69, 0.76]
PCC = [0.40, 0.26, 0.03, 0.12, 0.48, 0.32, 0.04, 0.37, 0.35, 0.57]

bar_width = 0.2
index = np.arange(len(Methods))

fig, ax = plt.subplots(figsize=(8, 6))

bar1 = ax.bar(index - 1.5*bar_width, ACC, bar_width, label='ACC')
bar2 = ax.bar(index - 0.5*bar_width, AUC, bar_width, label='AUC')
bar3 = ax.bar(index + 0.5*bar_width, F1, bar_width, label='F1')
bar4 = ax.bar(index + 1.5*bar_width, PCC, bar_width, label='PCC')

ax.set_xlabel('Methods', fontsize=16)
ax.set_ylabel('Values', fontsize=16)
ax.set_title('Performance on eSol dataset', fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels(Methods, rotation=45, fontsize=16)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.tick_params(axis='y', labelsize=16)

ax.legend(fontsize=12, loc='center', bbox_to_anchor=(0.3, 0.85))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.tight_layout()
plt.savefig('fig-2c.pdf')
plt.show()
