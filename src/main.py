from decode import decode
from encode import encode
from config import sample_rate
import sys
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plot

def draw_bits(bits):
	# The time vector, containing @sample_rate elements from
	# 0 to the number of bits
	t=np.arange(0, len(bits), 1/sample_rate)

	# The square wave signal we will plot
	u = []

	# For each bit in the @bits array, add elements to the output signal @u
	for bit in bits:
		u = u + sample_rate * [bit]

	# Finally, draw the signal
	plot.figure()
	plot.plot(t, u)
	plot.xlabel("t[s]")
	plot.ylabel("bit value")
	plot.show()

def draw_wave(signal):
	# The duration of our signal, in seconds
	signal_duration = (int)(len(signal) / sample_rate) # [s]

	# The number of samples within our signal
	sample_count = sample_rate * signal_duration

	# The time vector used to represent our signal:
	# @sample_count samples, evenly distributed from 0 to @signal_duration.
	time = np.linspace(0, signal_duration, sample_count)

	# Finally, draw the graph
	plot.figure()
	plot.plot(time, signal)
	plot.show()

def get_input_data():
	# Get the input data, an array of bits from CLI arguments
	bits = []
	for i in range(1, len(sys.argv)):
		if (sys.argv[i].isdigit()):
			bit = (int)(sys.argv[i])
			if (bit == 1 or bit == 0):
				bits.append(bit)
			else:
				print("Invalid input data. ABORT")
				sys.exit()
	return bits

if __name__ == "__main__":
	# Get the input data, an array of bits from CLI arguments
	bits = get_input_data()
	print("Input data: " + str(bits))

	# Plot the given bits
	draw_bits(bits)

	# Convert the input data into an audio signal
	signal = encode(bits)

	# Draw the generated signal
	draw_wave(signal)

	# Play the audio signal and record it back into @rec
	rec = sd.playrec(signal, sample_rate, channels=2)

	# Wait for the audio signal to play out completely
	sd.wait()

	# Draw the recorded signal
	draw_wave(rec)

	# Decode the recorded audio signal back into bits
	bits_back = decode(rec)

	# Draw the decoded bit array
	draw_bits(bits_back)

	# Print the bit array
	print("Output data: " + str(bits_back))

	if (bits == bits_back):
		print("yay")
	else:
		print("nay")
