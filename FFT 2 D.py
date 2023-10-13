# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:41:20 2023

@author: Ogi
"""

import numpy as np
import matplotlib.pyplot as plt

def fft2D(x):
    N, M = x.shape

    if N == 1 and M == 1:
        return x

    X = np.zeros((N, M), dtype=complex)

    for u in range(N):
        for v in range(M):
            X[u, v] = 0
            for m in range(M):
                for n in range(N):
                    X[u, v] += x[n, m] * np.exp(-2j * np.pi * ((u * n / N) + (v * m / M)))

    return X


def ifft2D(X):
    N, M = X.shape
    x = np.zeros((N, M), dtype=complex)

    for m in range(M):
        for n in range(N):
            x[n, m] = 0
            for v in range(M):
                for u in range(N):
                    x[n, m] += X[u, v] * np.exp(2j * np.pi * ((u * n / N) + (v * m / M)))

    return x / (N * M)


matrix = np.array([[1, 3, 3, 5], [5, 6, 7, 9], [9, 10, 14, 12], [13, 14, 15, 17]], dtype=complex)


DFT_result = fft2D(matrix)
print("Hasil DFT:")
print(DFT_result)


iDFT_result = ifft2D(DFT_result)
print("Hasil IFFT:")
print(iDFT_result)


plt.figure(figsize=(8, 8))
plt.subplot(121)
plt.imshow(np.abs(DFT_result), cmap='gray')
plt.title('Magnitude of DFT')
plt.subplot(122)
plt.imshow(np.angle(DFT_result), cmap='hsv')
plt.title('Phase of DFT')

plt.show()
