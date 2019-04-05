# Audio
import time
import board
import array
import math
import audioio
import digitalio

FREQUENCY = 440  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!

class cpAudioPlayer:
    def __init__(self, sampleRate = SAMPLERATE, enableInternalSpeaker = True):
        self.sampleRate = sampleRate
        if enableInternalSpeaker:
            self.speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
            self.speaker_enable.direction = digitalio.Direction.OUTPUT
            self.speaker_enable.value = True
            self.audio = audioio.AudioOut(board.A0)

    def playTone(self, frequencies = [FREQUENCY], duration = .5):
        for frequency in frequencies:
            length = self.sampleRate // frequency
            sine_wave = array.array("H", [0] * length)
            for i in range(length): # Generate one period of sine wav.
                sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)
            sine_wave_sample = audioio.RawSample(sine_wave)
            self.audio.play(sine_wave_sample, loop=True)  # keep playing the sample over and over
            time.sleep(duration)
            self.audio.stop()
        return self

    def playFile(self, filename):
        print("Playing file: " + filename)
        wave_file = open(filename, "rb")
        with audioio.WaveFile(wave_file) as wave:
            self.audio.play(wave)
            while self.audio.playing:
                pass
        return self
