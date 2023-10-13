# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:13:24 2023

@author: Ogi
"""

from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav


sample_rate, signal = wav.read("Gelaas 3.wav")

mfcc_features = mfcc(signal, sample_rate)
fbank_features = logfbank(signal, sample_rate)

print("MFCC Features:")
print(mfcc_features)

print("Filter Bank Features:")
print(fbank_features)
