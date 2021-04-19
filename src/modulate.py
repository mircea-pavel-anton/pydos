import numpy as np
from scipy import signal

from config import sample_rate

def modulate(s):
	Te = 1 / sample_rate
	T = s.size * Te # signal duration [s]
	time = np.arange(0, T, Te)

	# Carrier signal
	fc = 2500 # carrier signal frequency [Hz]
	sc = 2 * np.cos(2 * np.pi * fc * time) # carrier signal

	# Modulated signal
	sm = sc * s + sc

	return sm

def demodulate(s):
	filter_freq = [0, 2000, 3000, sample_rate/2] # cutoff frequencies for the filter
	filter_amp = [1, 0] # The amplitudes for the filter
	filter_size = 100 # filter size

	filter = signal.remez(filter_size - 1, filter_freq, filter_amp, Hz=sample_rate)
	return signal.lfilter(filter, 1, np.abs(s))