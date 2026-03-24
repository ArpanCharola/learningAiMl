#Using the NumPy library, create a 3x3 matrix (2D array) filled with random values
# and find the mean of the entire matrix.
import numpy as np

matrix = np.random.rand(3,3)
print("3x3 matrix")
print(matrix)

mean_value = np.mean(matrix)
print(f"Mean of matrix is :{mean_value}")

#AI models rely on NumPy for efficient numerical
# computations and data representation