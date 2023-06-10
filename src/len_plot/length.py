import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams

seqs_length = pd.read_csv("g_p.txt")
#print(seqs_length)
# Create two separate datasets for the different values of AMP
amp_Y = seqs_length[seqs_length['AMP'] == 'Y']
amp_N = seqs_length[seqs_length['AMP'] == 'N']

plt.figure(figsize=(12, 6), dpi=600)
#sns.histplot(data=seqs_length, x="Length", color=['#e74c3c'], kde=True)
sns.histplot(data=amp_Y, x="Length", kde=True, label='AMPs (8,791)')
sns.histplot(data=amp_N, x="Length", kde=True, label='Non-AMPs (34,775)')
plt.xlabel("Sequence Length", fontsize='large')
plt.ylabel("Frequency", fontsize='large')
plt.legend()
plt.savefig("test1.png")
plt.show()
