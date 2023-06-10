import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the matrices from files
matrix1 = np.loadtxt('AMP.txt')
matrix2 = np.loadtxt('non_AMP.txt')

# Concatenate the matrices vertically
combined_matrix = np.vstack((matrix1, matrix2))

# Perform PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(combined_matrix)

# Split the PCA result back into the individual matrices
pca_result_matrix1 = pca_result[:matrix1.shape[0]]
pca_result_matrix2 = pca_result[matrix1.shape[0]:]

# Plot the PCA results
plt.scatter(pca_result_matrix1[:, 0], pca_result_matrix1[:, 1], label='AMPs', s=1)
plt.scatter(pca_result_matrix2[:, 0], pca_result_matrix2[:, 1], label='Non-AMPs', s=1)
plt.xlabel('PC 1 ({:.2f}%)'.format(pca.explained_variance_ratio_[0]))
plt.ylabel('PC 2 ({:.2f}%)'.format(pca.explained_variance_ratio_[1]))
plt.legend()
plt.show()
