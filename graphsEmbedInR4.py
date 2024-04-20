import numpy as np

n = 6
arr = np.load("8vertexFail.npy")

m = n + 2
I = np.identity(m)
J = np.ones((m, m))
P = I - J / m


def FindDefect(projective_eigenvals):
    defect = 0
    for i in projective_eigenvals:
        if abs(i) < 0.0001:
            defect += 1
    return defect

counter = 0
for matrix in arr:
    projective_eigenvals = np.linalg.eigvalsh(np.matmul(np.matmul(P, matrix), P))
    defect = FindDefect(projective_eigenvals)
    if defect == 1:
        print(matrix, defect)
        counter += 1
print(counter)

