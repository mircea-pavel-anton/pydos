from config import sample_rate, signal_high, signal_low, bit_duration, freq_high
import numpy as np
import matplotlib.pyplot as plot

def truncate(n):
	return (int) ((n * 1000) / 1000)

# Returns the absolute value of @n.
def absolute(n):
	return n if n >= 0 else -n

# Returns true if the signs of a and b are different.
def signs_differ(a, b):
	if (a > 0 and b < 0):
		return True
	if (a < 0 and b > 0):
		return True
	return False

# Extracts a sub-signal from the original signal.
def extract_bit_signal(signal, i):
	return signal[i * sample_rate * bit_duration : (i+1) * sample_rate * bit_duration]

def decode(signal):
	bits = []
	freqs = []
	avg_freq = 0
	signal_duration = (int)(len(signal) / sample_rate) # [s]

	# For each sample in the recorded signal, check if it represents a pass through
	# Ox.
	# Basically, check if the previous sample is above Ox and the current one below
	# or the other way around
	# The number of passes through Ox represents our frequency
	# If the frequency is closer to @freq_high, it is safe to assume we have a '1'
	# otherwise, we have a '0'
	for i in range(0, signal_duration):
		# Extract a sub-signal from @signal, 1s long
		# We can do this since we know the @bit_duration and @sample_rate
		bit_signal = extract_bit_signal(signal, i)

		# Initially, we don't know the frequency, but we know that it represents
		# the number of passes through Ox. So we initialize it to 0 so that we
		# can start counting
		freq = 0

		# For each sample in our sub-signal, check if 2 consecutive samples
		# pass through Ox. If they do, increment @freq
		for j in range(1, len(bit_signal)):
			if (signs_differ(bit_signal[j-1], bit_signal[j])):
				freq = freq + 1

		print("Section " + str(i) + " frequency: " + str(freq) + " Hz")

		# If the calculated frequency is closer to @freq_high, assume
		# the bit was 1, otherwise, it was 0
		# NOTE: the frequencies are extremely unlikely to match, i.e. @freq will
		# almost never be equal to either @freq_high or @freq_low, so we
		# compare the distances between them
		freqs.append(freq)
		avg_freq += freq

	avg_freq = avg_freq / len(freqs)
	for i in range(0, len(freqs)):
		if (freqs[i] > avg_freq):
			bits.append(1)
		else:
			bits.append(0)

	return bits

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
