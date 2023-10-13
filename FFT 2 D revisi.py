# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:36:21 2023

@author: Ogi
"""

import cmath
import matplotlib.pyplot as plt

def fft2d(x):
    M, N = len(x), len(x[0])
    if M == 1 and N == 1:
        return [[x[0][0]]]
    
    M2, N2 = M // 2, N // 2
    x00 = [row[:N2] for row in x[:M2]]
    x01 = [row[N2:] for row in x[:M2]]
    x10 = [row[:N2] for row in x[M2:]]
    x11 = [row[N2:] for row in x[M2:]] 
    X00 = fft2d(x00)
    X01 = fft2d(x01)
    X10 = fft2d(x10)
    X11 = fft2d(x11)
    result = [[0] * N for _ in range(M)]
    for m in range(M2):
        for n in range(N2):
            e = cmath.exp(-2j * cmath.pi * (m + n) / M)
            X10[m][n] *= e
            X11[m][n] *= e
            result[m][n] = X00[m][n] + X10[m][n]
            result[m][n + N2] = X00[m][n] - X10[m][n]
            result[m + M2][n] = X01[m][n] + X11[m][n]
            result[m + M2][n + N2] = X01[m][n] - X11[m][n]
    return result
if __name__ == "__main__":
    signal = [[1, 2, 4, 4], [6, 6, 7, 8], [9, 11, 11, 12], [16, 14, 15, 16]]  # Contoh matriks 2D
    result = fft2d(signal)
    plt.imshow([[abs(val) for val in row] for row in result], cmap='viridis')
    plt.colorbar()
    plt.title("FFT 2D")
    plt.show()
