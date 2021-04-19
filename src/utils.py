import numpy as np
import sys

from config import bit_duration, sample_rate

def get_data_bits():
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
