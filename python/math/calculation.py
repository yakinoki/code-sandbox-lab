# coding: utf-8

import numpy as np
from src import Gauss_Jordan

# ------------------------------
# Example: Solving a linear system using Gauss-Jordan elimination
# ------------------------------

# Coefficient matrix A (ensure all entries are floats)
A = np.array([
    [4.0, 2.0, 1.0],
    [2.0, -1.0, 2.0],
    [1.0, 4.0, 1.0]
])

# Right-hand side vector b
b = np.array([
    [10.0],
    [5.0],
    [12.0]
])

if __name__ == "__main__":
    print("Solving the system Ax = b using custom Gauss-Jordan method:\n")
    print("Matrix A:")
    print(A)
    print("\nVector b:")
    print(b)

    print("\nSolution (Gauss-Jordan):")
    Gauss_Jordan.Gauss_J(A, b)

    print("\nSolution (NumPy built-in):")
    print(np.linalg.solve(A, b))
