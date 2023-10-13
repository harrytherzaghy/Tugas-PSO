# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:33:33 2023

@author: Ogi
"""

import cmath


def fft(x):                  #  FFT dari sinyal
    N = len(x)
    if N <= 1:
        return x

    
    even = fft(x[0::2]) #  Genap dan ganjil
    odd = fft(x[1::2])

   
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]


    result = [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]
    return result

if __name__ == "__main__":

    signal = [0, 1, 2, 3, 4, 5, 6, 7]

    # Padding sinyal hingga panjang menjadi pangkat dua (jika diperlukan)
    def next_power_of_2(x):
        return 1 << (x - 1).bit_length()
    padded_signal = signal + [0] * (next_power_of_2(len(signal)) - len(signal))

    # Menghitung FFT sinyal
    result = fft(padded_signal)

    # Skala hasil dengan panjang sinyal
    result = [x / len(signal) for x in result]

    # Import Matplotlib untuk plotting
    import matplotlib.pyplot as plt

    # Plot sinyal asli
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.title("Sinyal Asli")
    plt.plot(signal)
    plt.xlabel("t")
    plt.ylabel("A")

    # Plot hasil FFT
    plt.subplot(122)
    plt.title("FFT")
    plt.plot([abs(x) for x in result])
    plt.xlabel("F")
    plt.ylabel("A")
    plt.show()