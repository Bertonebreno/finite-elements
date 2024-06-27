import numpy as np

def calculate_a_ij(i, j):
    # Calcula a_ij conforme a fórmula dada
    return (i * j / (i + j - 1) 
            - ((1 + i) * j + (1 + j) * i) / (i + j) 
            + (1 + (1 + i) * (1 + j)) / (i + j + 1) 
            - 2 / (i + j + 2) 
            + 1 / (i + j + 3))

def calculate_f_i(i):
    # Calcula f_i conforme a fórmula dada
    return 1 / (i + 3) - 1 / (i + 2)

def build_matrix_and_vector(n):
    # Constrói a matriz A e o vetor f para um dado n
    A = np.zeros((n, n))
    f = np.zeros(n)
    for i in range(1, n + 1):
        f[i-1] = calculate_f_i(i)
        for j in range(1, n + 1):
            A[i-1, j-1] = calculate_a_ij(i, j)
    return A, f

def solve_galerkin_method(n):
    # Constrói a matriz e o vetor, resolve o sistema linear e retorna w
    A, f = build_matrix_and_vector(n)
    w = np.linalg.solve(A, f)
    return w