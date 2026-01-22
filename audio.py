import pygame
import math
import array

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

def make_beep(freq=440, duration_ms=200, volume=0.4, sample_rate=44100):
    n_samples = int(sample_rate * duration_ms / 1000)
    buf = array.array("h")

    amplitude = int(32767 * volume)
    for i in range(n_samples):
        t = i / sample_rate
        sample = int(amplitude * math.sin(2 * math.pi * freq * t))
        buf.append(sample)

    return pygame.mixer.Sound(buffer=buf)

beep = make_beep(freq=240, duration_ms=200)
beep.play()
pygame.time.delay(500)