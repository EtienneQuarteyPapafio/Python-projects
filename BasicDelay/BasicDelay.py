import numpy as np  #imports the numpy library
import matplotlib.pyplot as plt #imports the matplot library
import librosa as lr #imports the Librosa library for reading audio
import soundfile as sf #imports soundfile library to write audio

y, fs = lr.load('AcGtr.wav',sr=None) #put sr as none to use native sample of file

N=int(len(y)) #length of signal


maxDelay=800 #max delay in ms

delayTime=600 #chosen delay time <--- Change

maxSamples=round(maxDelay*fs/1000) #converts ms to samples

msSample=round(delayTime*fs/1000)

#Buffers

delay1=np.zeros(N+maxSamples) #empty array buffer to hold delayed signal

output=np.zeros(N+maxSamples) #empty array buffer to hold original and delayed signal

delay1[msSample:msSample+N]=y

output[:N]+=y

output += delay1


sf.write('AcGtr_with_delay.wav', output, fs) #writes audio

# Plot signals
plt.figure(figsize=(14, 6))

plt.subplot(3,1,1)
lr.display.waveshow(y, sr=fs,color='blue')
plt.title("Original Signal")

plt.subplot(3,1,2)
lr.display.waveshow(delay1, sr=fs,color='red')
plt.title("Delayed Signal Only")

plt.subplot(3,1,3)
lr.display.waveshow(output, sr=fs,color='gold')
plt.title("Final Output (Original + Delayed)")

plt.tight_layout()
plt.show()