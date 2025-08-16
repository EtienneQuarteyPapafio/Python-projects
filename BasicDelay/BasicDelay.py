import numpy as np  #imports the numpy library
import matplotlib.pyplot as plt #imports the matplot library
import librosa as lr #imports the Librosa library

y, fs = lr.load('AcGtr.wav',sr=None) #put sr as none to use native sample of file



maxDelay=800 #max delay in ms

maxSamples=maxDelay*fs/1000 #converts to samples

buffer=fs+maxSamples

plt.figure(figsize=(12, 4))
lr.display.waveshow(y, sr=fs) #This functions will dipslay audio file's waveform.
plt.show()