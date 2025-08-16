import numpy as np  #imports the numpy library
import matplotlib.pyplot as plt #imports the matplot library

#Librosa is a Python libray created for working with audio data

import librosa as lr

#filename = librosa.ex() #Loads sample audio file
y, fs = lr.load('AcGtr.wav',sr=None) #put sr as none to use native sample of file

plt.figure(figsize=(12, 4))
lr.display.waveshow(y, sr=fs) #This functions will dipslay audio file's waveform.
plt.show()
