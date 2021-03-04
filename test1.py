#!/usr/bin/python3


import wave
import struct
import numpy as np
from matplotlib import pyplot as plt

wav = wave.open("samples/voices.wav")

print("channels", wav.getnchannels())
print("frame rate", wav.getframerate())
print("frame number", wav.getnframes())
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
print(wav.getparams())
content = wav.readframes(nframes)
samples = np.fromstring(content, dtype=np.int16)
#print(content)
data = []
for i in range(0, nframes * sampwidth * nchannels, sampwidth):
    #for ch_num in range(nchannels):
    s = 0
    for b in range(sampwidth):
        s += content[i+b] << b*8
    #print(hex(s&0x800000))
    if (s & 1 << (8*sampwidth)-1) > 0:
        s = s - np.sum([0xff << 8*i for i in range(sampwidth)])
    data.append(s)

plt.clf()
plt.plot(data[0::2])
plt.plot(data[1::2])
plt.show()

#exit()
#data = struct.unpack("<" + str(nframes * 2) + "h", content)


#for i in range(0,600, 2):
#    plt.clf()
#    plt.plot(data[0::2])
#    plt.plot(data[i+1::2])
#    plt.show()


new_data = list(data)
ch1 = np.array(data[0::2])
ch2 = np.array(data[1::2])
print(np.std(ch1), np.std(ch2), np.std(ch1)/np.std(ch2))
resp = []
for i in range(800):
    mono = ch1[1000:-1000] - ch2[1000+i:-1000+i] 
    if 0 < i < 30:
        print(i)
        plt.clf()
        plt.plot(mono)
        plt.show()
    m = np.std(mono)
    
    resp.append(m)

plt.clf()
plt.plot(resp)
plt.show()

for i in range(0,len(data),2):
    new_data[i] = 0 
#new_data = new_data[59122:104352]


new_content = struct.pack("<" + str(len(new_data)) + "h", *new_data)
new_wav = wave.open("new.wav", mode="wb")
new_wav.setparams(wav.getparams())
new_wav.writeframes(new_content)
wav.close()
new_wav.close()
