import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Load the matrices from files
amp_matrix = np.loadtxt('AMP.txt')
nonamp_matrix = np.loadtxt('non_AMP.txt')

# Combine the matrices
combined_matrix = np.vstack((amp_matrix, nonamp_matrix))

# Perform t-SNE
tsne = TSNE(n_components=2)
tsne_result = tsne.fit_transform(combined_matrix)

# Split the t-SNE result
tsne_amp_result = tsne_result[:amp_matrix.shape[0]]
tsne_nonamp_result = tsne_result[amp_matrix.shape[0]:]

# Plot the t-SNE results
plt.scatter(tsne_amp_result[:, 0], tsne_amp_result[:, 1], label='AMPs',s=1)
plt.scatter(tsne_nonamp_result[:, 0], tsne_nonamp_result[:, 1], label='Non-AMPs',s=1, alpha=0.4)
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.legend()

#plt.tight_layout()
plt.show()
