from encode import encode
from config import sample_rate
import sounddevice as sd

# The input data, an array of bits
bits = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0];

# Convert the input data into an audio signal
signal = encode(bits)

# Play the audio signal and record it back into @rec
rec = sd.playrec(signal, sample_rate, channels=2)

# Prompt the user for keyboard input as otherwise the
# signal won't play out
input("Press ENTER to continue")
