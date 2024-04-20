import numpy as np

n = 5
number_of_matrices = 1044
file = "output7.txt"
outputfile = "7vertexFail.npy"

m = n + 2
I = np.identity(m)
J = np.ones((m, m))
P = I - J / m

matrices = []


def findK(eigenvals, second_eigenval):
    k = m - 2
    while k >= 1 and abs(eigenvals[k - 1] - second_eigenval) < 0.00001:
        k -= 1
    return k


for i in range(number_of_matrices):
    matrix = np.loadtxt(file, skiprows=1 + i * (m + 1), max_rows=m, usecols=range(m))
    eigenvals = np.linalg.eigvalsh(matrix)
    second_eigenval = eigenvals[m - 2]  # uses a separate variable for the second eigenvalue
    if second_eigenval < 0.0001:  # removes the graphs that are complete multipartite
        continue
    projective_eigenvals = np.linalg.eigvalsh(np.matmul(np.matmul(P, matrix), P))
    if abs(second_eigenval - projective_eigenvals[m - 1]) < 0.0001:
        k = findK(eigenvals, second_eigenval)
        if abs(second_eigenval - projective_eigenvals[k]) < 0.00001:  # the second condition fails
            matrices.append(matrix)
np.save(outputfile, matrices)
