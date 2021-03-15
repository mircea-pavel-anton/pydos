# PyDoS

PyDoS (Python Data-over-Sound) is a simple python script that simulates a modem.

## What it does and how it works?

### The "what"

This program takes an array on bit values, such as:

``` python
bits = [1, 0, 1, 1]
```

And it generates a sine wave that can be then played by the sound card. The sound produced by the speakers is then captured by the microphone, and another method converts the sound wave back into the original bit array.  
This emulates the process of converting digital data into an analog signal, sending and receiving it over an analog medium and then converting back into digital, much like a modem.

### The "how"

By taking a look at `config.py` under `src/`, we can notice some key components that help us build the sine wave:

1. `sample_rate = 44100 # [Hz]`: the sample rate of the wave
2. `bit_duration = 1 # [s]`: the time duration allocated for each bit into the output signal
3. `freq_high = 1000 # [Hz]`: the frequency of the sine-wave used to represent a `1` bit
4. `freq_low = 100 # [Hz]`: the frequency of the sine-wave used to represent a `0` bit

As such, we can deduce that the way this program builds the soundwave is by concatenating together 1 second long sine waves, of alternating frequencies in order to represent each bit.

| Bit value | Wave frequency | Waveform |
| :-: | :-: | :-: |
| 0 | 100 Hz | <img src="res/signal_low.png" alt="drawing" width="350"/> |
| 1 | 1 kHz | <img src="res/signal_high.png" alt="drawing" width="350"/> |

## Example

For example, assuming the already mentioned bits for input:

``` python
bits = [1, 0, 1, 1]
```
<p align="center">
  <img src="res/bit_input.png" alt="drawing" width="450"/>
</p>

The program will generate the following sine wave:

<p align="center">
  <img src="res/encoded_signal.png" alt="drawing" width="650" height="250"/>
</p>

We can easily observe the original bit array within our signal, since the 2 used frequencies are far apart enough for it to be noticeable.

Next, this signal is played by the sound card and recorded back via the microphone. The previous wave, recorded by a my microphone looks like this:

<p align="center">
  <img src="res/recorded_signal.png" alt="drawing" width="650" height="250"/>
</p>

We can notice quite a bit of noise and variance, but it is still easily recognizable.

Next, a the `decode` method will reconstruct the bit array by analyzing the frequencies of each section of our signal, producing the following signal:

<p align="center">
  <img src="res/decoded_signal.png" alt="drawing" width="450"/>
</p>

---

_a project by Mircea-Pavel Anton (Mike Anthony)_
