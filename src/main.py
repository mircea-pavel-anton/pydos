import sounddevice as sd
import matplotlib.pyplot as plot
import numpy as np

# The sample rate for the audio signal.
sample_rate = 44100 # [Hz]

# The duration of time one bit will be represented in the
# output signal
bit_duration = 1 # [s]

# The frequency our output signal will have when the
# corresponsing bit is '1'
freq_high = 1000 # [Hz]

# The frequency our output signal will have when the
# corresponsing bit is '0'
freq_low = 100 # [Hz]

# The time vector for a single bit representation
bit_time = np.linspace(0, bit_duration, bit_duration * sample_rate)

# The sine wave for the output signal when the
# corresponsing bit is '1'
signal_high = np.sin(2 * np.pi * freq_high * bit_time)

# The sine wave for the output signal when the
# corresponsing bit is '0'
signal_low = np.sin(2 * np.pi * freq_low * bit_time)

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

    # The time vector used to represent our signal:
    # @sample_count samples, evenly distributed from 0 to @signal_duration.
    time = np.linspace(0, signal_duration, sample_count)

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

# The input data, an array of bits
bits = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0];
signal = encode(bits)
rec = sd.playrec(signal, sample_rate, channels=2)
input("Press ENTER to continue")
