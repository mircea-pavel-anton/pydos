from config import sample_rate, signal_high, signal_low
import numpy as np
import matplotlib.pyplot as plot

def truncate(n):
	return (int) ((n * 1000) / 1000)

def encode(bits):
	# The length of time per sample.
	sample_time = 1 / sample_rate # [s]

	# The duration of the audio signal produced.
	# We assume each bit represents 1s in the audio signal.
	signal_duration = len(bits) # [s]

	# The number of samples in the audio signal.
	sample_count = signal_duration * sample_rate


	# To begin with, @signal is just a flat line.
	signal = []
	signal_index = 0

	for i in range(0, len(bits)):
		if (bits[i] == 1):
			for sample in signal_high:
				signal.append(sample)
		else:
			for sample in signal_low:
				signal.append(sample)

	return signal;
