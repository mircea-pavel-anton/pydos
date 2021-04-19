import sys
import numpy as np
import matplotlib.pyplot as plot
import sounddevice as sd

from encode import encode, decode
from config import sample_rate
from plot import plot_bits, plot_T, plot_S
from modulate import modulate, demodulate

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

	# Convert the input data into an audio signal
	signal = np.array( encode(bits) )

	# Modulate the signal
	signal_mod = modulate ( signal )

	# Play the audio signal and record it back into @rec
	rec = sd.playrec(signal_mod, sample_rate, channels=1)

	# Wait for the audio signal to play out completely
	sd.wait()

	# Demodulate the recorded signal
	rec_demod = demodulate( rec )

	# Decode the recorded audio signal back into bits
	bits_back = decode(rec)

	# Print the bit array
	print("Output data: " + str(bits_back))

	# Finally, plot out all the signals (in time)

	# Plot the input side
	plot.figure()
	plot.subplot(3, 1, 1)
	plot_bits(bits, "Input bit signal")
	# Plot the generated sound wave
	plot.subplot(3, 1, 2)
	plot_T(1/sample_rate, signal, "Message signal")
	# Plot the modulated sound wave
	plot.subplot(3, 1, 3)
	plot_T(1/sample_rate, signal_mod, "Modulated signal")

	# Plot the output side
	plot.figure()
	plot.subplot(3, 1, 1)
	plot_T(1/sample_rate, rec, "Received signal")
	# Plot the recorded signal, demodulated
	plot.subplot(3, 1, 2)
	plot_T(1/sample_rate, rec_demod, "Demodulated signal")
	# Plot the decoded data bits
	plot.subplot(3, 1, 3)
	plot_bits(bits_back, "Decoded bit signal")
	plot.show()
	plot.tight_layout()