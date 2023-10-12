# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:49:18 2023

@author: Ogi
"""

def convolv(signal, kernel):     # Define
    # Sinyal dan Kernelnya
    signal_length = len(signal)
    kernel_length = len(kernel)
    
    # Sinyal yang udah di konvolusi
    result_Con_length = signal_length + kernel_length - 1
    
    # Inisialisasi hasil konvolusi dengan nilai nol
    result = [0] * result_Con_length
    
    # Hasil Konvolusi dari Padding
    kernel = list(reversed(kernel))
    
    for i in range(result_Con_length):
        for j in range(kernel_length):
            if i - j >= 0 and i - j < signal_length:
                result[i] += signal[i - j] * kernel[j]
    
    return result

# Hasilnya
signal = [1, 2, 3, 4, 5]
kernel = [0, 1, 2, 3]
print("Muhammad Harry Therzaghy")
print("5009211114")
result = convolv(signal, kernel)
print("Konvolusi:", result)