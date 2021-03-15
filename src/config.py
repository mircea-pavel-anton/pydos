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
