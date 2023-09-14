# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

# Membuat sinyal contoh (misalnya, sinyal sinus)
Fs = 1000  # Frekuensi sampel
T = 1.0   # Durasi sinyal dalam detik
N = int(Fs * T)  # Jumlah titik data
t = np.linspace(0.0, T, N, endpoint=False)  # Waktu dalam detik
f = 5.0  # Frekuensi sinyal sinus (Hz)
x = np.sin(2 * np.pi * f * t)  # Sinyal sinus dengan frekuensi 5 Hz

# Melakukan FFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, 1/Fs)  # Menghasilkan array frekuensi

# Plot hasil FFT
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Sinyal Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(X))
plt.title('Sinyal Frekuensi (FFT)')
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Amplitudo')
plt.xlim(0, Fs/2)  # Menampilkan hanya separuh spektrum (frekuensi positif)
plt.grid()

plt.tight_layout()
plt.show()

