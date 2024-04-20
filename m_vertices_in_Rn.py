import numpy as np

N = 5  # this is the dimension of the adjacency matrix
sample = int(1e4)  # this is the size of the sample that we are going to take

precision = 1e-6  # this is the precision with which two numbers are compared

I = np.identity(N)
J = np.ones((N, N))
P = I - J / N


def findK(eigenvals, second_eigenval):
    k = N - 2
    while k >= 1 and abs(eigenvals[k - 1] - second_eigenval) < 0.00001:
        k -= 1
    return k


def are_equal(a, b):
    if abs(a-b) < precision:
        return True
    return False


for t in range(sample):
    matrix = np.random.rand(N, N)
    for i in range(N):
        for j in range(i):
            if matrix[i, j] < 0.5:
                matrix[i, j] = 0
                matrix[j, i] = 0
            else:
                matrix[i, j] = 1
                matrix[j, i] = 1
        matrix[i, i] = 0
    eigenvals = np.linalg.eigvalsh(matrix)
    second_eigenval = eigenvals[N - 2]  # uses a separate variable for the second eigenvalue
    if second_eigenval < precision:  # removes the graphs that are complete multipartite
        continue
    projective_eigenvals = np.linalg.eigvalsh(np.matmul(np.matmul(P, matrix), P))
    if are_equal(second_eigenval, projective_eigenvals[N - 1]):
        k = findK(eigenvals, second_eigenval)
        if not are_equal(second_eigenval, projective_eigenvals[k]):  # the second condition fails
            counter = 0
            for eigen in projective_eigenvals:
                if are_equal(eigen, second_eigenval):
                    counter += 1
            if counter > 1:
                print(counter)
                print("Eigenvals: ", eigenvals)
                print("Projective eigenvals: ", projective_eigenvals)

