import numpy as np
import sys as sys

sys.path.insert(1, 'src')
from encode import encode, decode
from config import sample_rate
from modulate import modulate, demodulate
from utils import get_data_bits

if __name__ == "__main__":
	# Get the input data, an array of bits from CLI arguments
	bits = get_data_bits()

	# Convert the input data into an audio signal
	signal = np.array( encode(bits) )

	# Modulate the signal
	signal_mod = modulate ( signal )

	# simulate the playing and recording functionality in a perfect scenario by
    # passing the signal directly
	rec = signal_mod

	# Demodulate the recorded signal
	rec_demod = demodulate( rec )

	# Decode the recorded audio signal back into bits
	bits_back = decode(rec_demod)

	if (bits == bits_back):
		exit(0)
	else:
		exit(1)
