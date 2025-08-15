import numpy as np #imports the numpy library
import matplotlib.pyplot as plt #imports the matplot library

#Define signal parameters

T=1 #period in seconds
fs=44100 #sampling frequency (Hz)
ts=1/fs
time=np.arange(0,T,ts) #creates an array of time in steps of ts

#sinewave = A*cos*((2*pi*freq)*time+phase)

amp=1; #0-1
freq=20; #in hz
phase=0; #initial phase

y=amp*np.cos(2*np.pi*freq*time+phase)

# Plot the sine wave
plt.plot(time, y)

# Add title and labels
plt.title("Sine Wave")
plt.xlabel("Time(sec)")
plt.ylabel("Amplitude")

# Show grid and the plot
plt.grid(True)
plt.show()
