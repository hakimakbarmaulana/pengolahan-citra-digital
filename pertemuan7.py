import numpy as np
import math


# Transformasi Fourier 1 D
# X = np.array([13, 3, 10, 15, 10, 13, 0, 2, 13, 6])
# print(X)
# F1 = np.zeros(len(X))
# F = []
# for i in range(len(X)):
#     F.append(complex(F1[i]))
# for u in range(len(X)):
#     F[u] = 0
#     for k in range(len(X)):
#         F[u] = F[u] + X[k] * np.exp(-complex(0, 1) * 2 * math.pi * u * k / 10)
# print(F)
# G1 = np.zeros(len(X))
# G = []
# for i in range(len(X)):
#     G.append(complex(G1[i]))
# for k in range(len(X)):
#     G[k] = 0
#     for u in range(len(X)):
#         G[k] = G[k] + F[u] * np.exp(complex(0, 1) * 2 * math.pi * u * k / 10)
#     G[k] = int(np.real(G[k]) / 10)
# print(np.array(G))


# Transformasi Fourier 2 D
X = np.array([[20, 25], [50, 22]])
print(X)
[m, n] = [len(X), len(X[0])]
F = []
for i in range(m):
    A = []
    for j in range(n):
        A.append(complex(0))
    F.append(A)
F = np.array(F)
for u in range(m):
    for v in range(n):
        F[u, v] = 0
        for j in range(m):
            for k in range(n):
                F[u, v] = F[u, v] + X[j, k] * np.exp(-complex(0, 1) * 2 * math.pi * (u * j / m + v * k / n))
print(F)
G = []
for i in range(m):
    B = []
    for j in range(n):
        B.append(complex(0))
    G.append(B)
G = np.array(G)
G2 = np.zeros([m, n])
for u in range(m):
    for v in range(n):
        G[u, v] = 0
        for j in range(m):
            for k in range(n):
                G[u, v] = G[u, v] + F[j, k] * np.exp(complex(0, 1) * 2 * math.pi * (u * j / m + v * k / n))
        G2[u, v] = np.real(G[u, v])/(m*n)
print(G2)
