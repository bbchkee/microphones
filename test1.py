#!/usr/bin/python3


import wave
import struct
import numpy as np
from matplotlib import pyplot as plt

wav = wave.open("claps50cm16bit.wav")

print("channels", wav.getnchannels())
print("frame rate", wav.getframerate())
print("frame number", wav.getnframes())
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
print(wav.getparams())
content = wav.readframes(nframes)
samples = np.fromstring(content, dtype=np.int16)
data = struct.unpack("<" + str(nframes * 2) + "h", content)



new_wav = wave.open("new.wav", mode="wb")
new_wav.setparams(wav.getparams())
new_wav.writeframes(content)
wav.close()
new_wav.close()
