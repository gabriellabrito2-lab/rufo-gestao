"""Christmas music bed + sleigh bells + runway/editorial bed (synthesized)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sfx import save, t, lowpass, SR, rng  # noqa: E402

def env(d, a=0.005, r=8.0):
    e = np.exp(-d * r); n = int(a * SR); e[:n] *= np.linspace(0, 1, n); return e

def bell(f, dd=0.9, r=4.0):
    d = t(dd); return sum(np.sin(2*np.pi*f*h*d) * g for h, g in ((1, 1), (2.76, 0.4), (5.4, 0.2))) * env(d, 0.002, r)

def jingle(dd=0.12):
    d = t(dd); n = rng.standard_normal(d.size); return (n - lowpass(n, 0.5)) * np.exp(-d * 40)

save("sleigh", np.concatenate([jingle(0.12) * (1 - 0.15 * k) for k in range(6)]), 0.6)
save("bells", bell(1568) + 0.7 * np.pad(bell(2093), (int(0.12 * SR), 0))[: int(0.9 * SR)], 0.6)

def bed(name, bpm, bars, fn, gain=0.8):
    beat = 60 / bpm; mix = np.zeros(int(SR * bars * 4 * beat))
    def add(sig, at, g=1.0):
        i = int(at * SR); j = min(mix.size, i + sig.size)
        if i < mix.size: mix[i:j] += g * sig[: j - i]
    fn(add, beat, bars); save(name, mix, gain)

def tone(f, dd, r=3.0, harm=(1,), a=0.01):
    d = t(dd); return sum(np.sin(2*np.pi*f*h*d)/h for h in harm) * env(d, a, r)

kick = lambda: (lambda d: np.sin(2*np.pi*(50+110*np.exp(-d*28))*d)*np.exp(-d*8))(t(0.4))

def xmas(add, b, bars):  # 120 bpm, swung sleigh bells, celesta-like melody, bass
    prog = [(261.6, 329.6, 392), (220, 261.6, 329.6), (174.6, 220, 261.6), (196, 246.9, 293.7)]
    mel = [784, 659, 698, 784, 880, 784, 659, 587]
    for bar in range(bars):
        b0 = bar * 4 * b; ch = prog[bar % 4]
        for f in ch: add(tone(f, 4 * b, 0.9, (1, 2), 0.03), b0, 0.07)
        add(tone(ch[0] / 2, 2 * b, 1.5, (1, 2)), b0, 0.35); add(tone(ch[0] / 2, 2 * b, 1.5, (1, 2)), b0 + 2 * b, 0.3)
        for s in range(8): add(jingle(), b0 + s * b / 2 + (0.03 if s % 2 else 0), 0.25)
        for s in range(4): add(kick(), b0 + s * b, 0.35 if s % 2 == 0 else 0)
        if bar % 2 == 0:
            for k, f in enumerate(mel[:4] if bar % 4 == 0 else mel[4:]): add(bell(f, 0.6, 5), b0 + k * b, 0.18)
bed("music_xmas", 120, 16, xmas)

def runway(add, b, bars):  # 124 bpm minimal house for editorial
    for bar in range(bars):
        b0 = bar * 4 * b
        add(tone(55, 4 * b, 0.4, (1, 2, 3), 0.02), b0, 0.18)
        for s in range(4):
            add(kick(), b0 + s * b, 0.8)
            d = t(0.05); h = rng.standard_normal(d.size) * np.exp(-d * 90); add(h - lowpass(h, 0.3), b0 + s * b + b / 2, 0.2)
        for s in (1, 3):
            d = t(0.15); add(rng.standard_normal(d.size) * np.exp(-d * 30), b0 + s * b, 0.18)
        if bar % 2: add(tone(440, 0.25, 9, (1, 2)), b0 + 3.5 * b, 0.12)
bed("music_runway", 124, 16, runway)
print("ok")
