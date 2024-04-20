import numpy as np

# change the following three lines if you want to use it for other dimensions n (n+2 vertex graphs)
n = 5
number_of_matrices = 1044
file = "output7.txt"

m = n + 2
I = np.identity(m)
J = np.ones((m, m))
P = I - J / m
counter = np.zeros(m)
count = 0  # counter of the sets that have the first property
matrices = []

for i in range(number_of_matrices):
    matrix = np.loadtxt(file, skiprows=1 + i * (m + 1), max_rows=m, usecols=range(m))
    eigenvals = np.linalg.eigvalsh(matrix)
    second_eigenval = eigenvals[m - 2]
    if second_eigenval < 0.0001:
        continue
    projective_eigenvals = np.linalg.eigvalsh(np.matmul(np.matmul(P, matrix), P))
    if abs(eigenvals[m - 2] - projective_eigenvals[m - 1]) < 0.0001:
        # print(matrix)
        # if count % 50 == 0:  # prints the counter so that we can keep track of how fast we are at the moment
        #     print(count, i)
        k = m - 2
        while k >= 1 and abs(eigenvals[k - 1] - second_eigenval) < 0.0001:
            k -= 1
        print(k, end=" ")

        if second_eigenval > projective_eigenvals[k]:  # the second condition fails
            # matrices.append(matrix)
            count += 1
            counter[k] += 1
# np.save("spherical8.npy", matrices)
print("Number of small spherical:", count)
i = n
while counter[i] != 0:
    print("Number of spherical graphs that embed in", i, end="")
    print("-dimensional space: ", counter[i])
    i -= 1
