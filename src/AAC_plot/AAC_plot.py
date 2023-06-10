import numpy as np
import matplotlib.pyplot as plt

# Load the data from AMP.csv and non_AMP.csv
data_amp = np.genfromtxt('AMP.csv', delimiter=',')
data_non_amp = np.genfromtxt('non_AMP.csv', delimiter=',')

# Calculate the mean occurrence frequency for each dataset
mean_frequency_amp = np.mean(data_amp, axis=0)
mean_frequency_non_amp = np.mean(data_non_amp, axis=0)

# Get the counts of AMP and non-AMP datasets
count_amp = data_amp.shape[0]
count_non_amp = data_non_amp.shape[0]

# Increase the font size for labels and tick labels
plt.rcParams.update({'font.size': 20})  # Set the font size to 12

# Plotting the comparison bar chart
x = np.arange(20)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mean_frequency_amp, width, label='AMPs (1,463)')
rects2 = ax.bar(x + width/2, mean_frequency_non_amp, width, label='Non-AMPs (6,015)')

plt.figure(figsize=(12, 6), dpi=600)
ax.set_xticks(x)
ax.set_xticklabels(['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])
ax.set_xlabel('Amino Acid', fontsize=20)
ax.set_ylabel('Mean Frequency (%)', fontsize=20)
#ax.set_title('Comparison of AAC Occurrence Frequency', fontsize=16)
ax.legend(fontsize=20)  # Increase the legend font size

plt.show()
