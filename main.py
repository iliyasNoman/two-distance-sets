import numpy
import numpy as np
import sys

n = 6
number_of_matrices = 12346
file = "output8withspaces.txt"

m = n + 2
I = np.identity(m)
J = np.ones((m, m))
P = I - J / m
count = 0  # counter of the sets that have the first property
second_eigenval_set = [0]
one = 0

for i in range(number_of_matrices):
    matrix = np.loadtxt(file, skiprows=1 + i * (m + 1), max_rows=m, usecols=range(m))
    eigenvals = np.linalg.eigvalsh(matrix)
    second_eigenval = eigenvals[m - 2]
    if abs(second_eigenval) < 0.0001:
        continue
    projective_eigenvals = np.linalg.eigvalsh(np.matmul(np.matmul(P, matrix), P))
    if abs(second_eigenval - projective_eigenvals[m-1])<0.0001:
        count += 1
        k = m-2
        if second_eigenval < 1:
            one += 1
        # is_it_new = True
        # for j in range(len(second_eigenval_set)):
        #     if abs(second_eigenval_set[j] - second_eigenval) < 0.0001:
        #         is_it_new = False
        #         break
        # if is_it_new:
        #     second_eigenval_set.append(second_eigenval)
        while k >= 1 and abs(eigenvals[k-1] - second_eigenval)<0.00001:
            k -= 1
        if abs(second_eigenval - projective_eigenvals[k])<0.00001:  # the second condition fails

            # print(eigenvals, projective_eigenvals, "\n")
# print(second_eigenval_set)
# print(one)
# numpy.save