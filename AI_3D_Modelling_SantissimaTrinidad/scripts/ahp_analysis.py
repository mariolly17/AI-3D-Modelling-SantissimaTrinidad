# ahp_analysis.py
import numpy as np

def ahp_weights(matrix):
    eigvals, eigvecs = np.linalg.eig(matrix)
    max_index = np.argmax(eigvals)
    weights = np.real(eigvecs[:, max_index])
    weights /= np.sum(weights)
    return weights

if __name__ == "__main__":
    A = np.array([[1, 3, 0.5],
                  [1/3, 1, 0.25],
                  [2, 4, 1]])
    print("Weights:", ahp_weights(A))
