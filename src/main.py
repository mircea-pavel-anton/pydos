from decode import decode
from encode import encode
from config import sample_rate
import sounddevice as sd

# The input data, an array of bits
bits = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0];

# Convert the input data into an audio signal
signal = encode(bits)

# Play the audio signal and record it back into @rec
rec = sd.playrec(signal, sample_rate, channels=2)

# Wait for the audio signal to play out completely
sd.wait()

# Decode the recorded audio signal back into bits
bits_back = decode(rec)

if (bits == bits_back):
	print("yay")
else:
	print("nay")
