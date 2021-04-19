import numpy as np
import matplotlib.pyplot as plot
from scipy.fftpack import fft, fftshift

from config import sample_rate

def plot_bits(bits, title=""):
	"""! This function plots a square-wave graph of the given data bits

	@param bits: a list of all of the data bits
	@param title: the title of the plot
	"""
	# The time vector, containing @sample_rate elements from
	# 0 to the number of bits
	t=np.arange(0, len(bits), 1/sample_rate)

	# The square wave signal we will plot
	u = []

	# For each bit in the @bits array, add elements to the output signal @u
	for bit in bits:
		u = u + sample_rate * [bit]

	# Finally, draw the signal
	plot.plot(t, u)
	plot.xlabel("t[s]")
	plot.ylabel("bit value")

def plot_T(Te, s, title=""):
	"""! This function plots the time response of the given signal
	
	@param Te: time duration of a single sample
	@param s: the given signal
	@param title: The title of the plot
	""" 
	time = np.arange(0, s.size*Te, Te)

	plot.plot(time[:s.size], s)
	plot.title(title)
	plot.xlabel("Time [s]")
	plot.ylabel("Amplitude")

def plot_S(Te, s, title=""):
	"""! This function plots the frequency response of the given signal

	@param Te: time duration of a single sample
	@param s: the given signal
	@param title: The title of the plot
	""" 
	N = s.size	# the number of samples
	fe = 1/Te	# the sample rate [Hz]

	delta_f = fe/N			# the distance between 2 adjacent samples
	f_max= N / 2 * delta_f	# The maximum frequency of the spectrum
	f_min = -f_max			# the minimum frequency of the spectrum
	
	# frequency array, from f_min to f_max with a step of delta_f
	f = np.arange(f_min, f_max, delta_f)
	
	S = fft(s) 
	S = fftshift(S) # shift the spectrum to center it on the axis origin
	S = np.abs(S)  # get the absolute value of each sample

	plot.plot(f[:S.size],S)
	plot.title(title)
	plot.xlabel("Freq [Hz]")
	plot.ylabel("Abs val")   