"""Synthesize royalty-free SFX and a light background beat (44.1 kHz stereo WAV)."""
import os, wave
import numpy as np

SR = 44100
OUT = os.path.join(os.path.dirname(__file__), "sfx")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)


def save(name, x, gain=0.9):
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    peak = np.abs(x).max() or 1
    x = (x / peak * gain * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name + ".wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(x.tobytes())


def t(d):
    return np.arange(int(SR * d)) / SR


def lowpass(x, a):
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x):
        acc += a[i] * (v - acc) if np.ndim(a) else a * (v - acc); y[i] = acc
    return y


# whoosh: noise swept through a moving low-pass, bell envelope
d = t(0.45); n = rng.standard_normal(d.size)
cut = 0.02 + 0.35 * np.sin(np.pi * d / d[-1]) ** 2
save("whoosh", lowpass(n, cut) * np.sin(np.pi * d / d[-1]) ** 1.5)

# pop: short pitched-down sine blip
d = t(0.09)
save("pop", np.sin(2 * np.pi * (900 - 5000 * d) * d) * np.exp(-d * 45), 0.8)

# ding: bright bell
d = t(0.9)
save("ding", (np.sin(2 * np.pi * 1318 * d) + 0.5 * np.sin(2 * np.pi * 2637 * d) + 0.25 * np.sin(2 * np.pi * 3951 * d)) * np.exp(-d * 5), 0.7)

# cha-ching: two metallic hits + coin shimmer
def metal(f, dd):
    return sum(np.sin(2 * np.pi * f * k * dd) / k for k in (1, 2.76, 5.4)) * np.exp(-dd * 9)
d = t(1.0); x = np.zeros(d.size)
x += metal(2200, d)
off = int(0.12 * SR); x[off:] += 1.2 * metal(2950, d[: d.size - off])
x += 0.25 * rng.standard_normal(d.size) * np.exp(-d * 6) * (np.sin(2 * np.pi * 37 * d) > 0)
save("chaching", x, 0.75)

# riser: rising tone + noise, 1.2 s
d = t(1.2)
f = 200 + 1400 * (d / d[-1]) ** 2
save("riser", (np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.6 + 0.4 * rng.standard_normal(d.size) * (d / d[-1])) * (d / d[-1]) ** 2, 0.6)

# boom/impact for the hook
d = t(0.7)
save("boom", np.sin(2 * np.pi * (110 - 60 * d) * d) * np.exp(-d * 6) + 0.3 * rng.standard_normal(d.size) * np.exp(-d * 30), 0.95)

# background beat: 100 BPM, kick / clap / hats / soft chord pad, 48 s loop
bpm = 100; beat = 60 / bpm; L = 48.0
mix = np.zeros(int(SR * L))
def add(sig, at, g=1.0):
    i = int(at * SR); j = min(mix.size, i + sig.size); mix[i:j] += g * sig[: j - i]
k_t = t(0.35); kick = np.sin(2 * np.pi * (55 + 120 * np.exp(-k_t * 30)) * k_t) * np.exp(-k_t * 9)
c_t = t(0.2); clap = rng.standard_normal(c_t.size) * np.exp(-c_t * 25)
h_t = t(0.05); hat = rng.standard_normal(h_t.size) * np.exp(-h_t * 90)
hat = hat - lowpass(hat, 0.2)
chords = [(261.6, 329.6, 392.0), (220.0, 261.6, 329.6), (174.6, 220.0, 261.6), (196.0, 246.9, 293.7)]
p_t = t(beat * 4)
for bar in range(int(L / (beat * 4)) + 1):
    b0 = bar * beat * 4
    ch = chords[bar % 4]
    pad = sum(np.sin(2 * np.pi * f * p_t) for f in ch) * (1 - np.exp(-p_t * 4)) * np.exp(-p_t * 0.4)
    add(pad, b0, 0.12)
    add(np.sin(2 * np.pi * ch[0] / 2 * p_t) * np.exp(-p_t * 1.2), b0, 0.35)
    for s in range(4):
        add(kick, b0 + s * beat, 0.9 if s in (0, 2) else 0.0)
        if s in (1, 3): add(clap, b0 + s * beat, 0.35)
    for s in range(8):
        add(hat, b0 + s * beat / 2, 0.18)
save("beat", mix, 0.8)
print("ok", sorted(os.listdir(OUT)))
