# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:57:36 2023

@author: Ogi
"""

import speaker_verification_toolkit.tools as svt
import librosa
data,sr= librosa.load('Audio.wav', sr=1600, mono='true')
data = svt.rms_silence_filter(data)
data=svt.extract_mfcc(data)
print("MFCC Values :\n", data)