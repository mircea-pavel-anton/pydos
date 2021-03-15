# Sample code that simply pllays and records a sine wave
# and plots out the input and output signals
import sounddevice as sd
import matplotlib.pyplot as plot
import numpy as np

signal_freq = 1000              # Hz
signal_duration = 2             # sec
sample_rate = 44100             # Hz
sample_time = 1 / sample_rate   # sec
sample_count = sample_rate * signal_duration

# Generate the time vector, containing @sample_count items
# in the interval of (0, @signal_duration), all equally distanced
# from each other
time = np.linspace(0, signal_duration, sample_count)

sine_wave = np.sin(2 * np.pi * signal_freq * time)  # sin(2*pi*f*t)

rec = sd.playrec(sine_wave, sample_rate, channels=2)
sd.wait()

plot.figure()
plot.subplot(311)
plot.plot(time, sine_wave)
plot.subplot(312)
plot.plot(time, rec[:,0])
plot.subplot(313)
plot.plot(time, rec[:,1])
plot.show()