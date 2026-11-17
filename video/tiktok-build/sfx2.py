"""Extra SFX and one background track per style (all synthesized, royalty-free)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sfx import save, t, lowpass, SR, rng  # noqa: E402  (also regenerates base set)


def env(d, a=0.005, r=8.0):
    e = np.exp(-d * r); n = int(a * SR); e[:n] *= np.linspace(0, 1, n); return e


# --- one-shots ---
d = t(1.1); save("vineboom", (np.sin(2*np.pi*(70+90*np.exp(-d*14))*d) + 0.5*np.sin(2*np.pi*(140+180*np.exp(-d*14))*d)) * env(d, r=3.2), 1.0)
d = t(0.55); f = 300 + 900*np.sin(np.pi*d/d[-1]*2.2); save("scratch", lowpass(rng.standard_normal(d.size)*np.sin(2*np.pi*np.cumsum(f)/SR), 0.35) * env(d, r=4), 0.85)
d = t(0.25); g = rng.standard_normal(d.size); g = np.round(g*3)/3 * (np.sin(2*np.pi*55*d) > -0.2); save("glitch", g*env(d, r=10) + 0.4*np.sign(np.sin(2*np.pi*180*d))*env(d, r=14), 0.7)
d = t(1.2); x = np.zeros(d.size)
for k, fr in enumerate((2093, 2637, 3136, 4186)):
    o = int(k*0.07*SR); x[o:] += np.sin(2*np.pi*fr*d[:d.size-o]) * np.exp(-d[:d.size-o]*6)
save("sparkle", x, 0.55)
d = t(0.04); save("tick", rng.standard_normal(d.size)*np.exp(-d*160) + np.sin(2*np.pi*3000*d)*np.exp(-d*120), 0.6)
d = t(0.9); save("alarm", np.sign(np.sin(2*np.pi*np.where((d*6).astype(int) % 2 == 0, 880, 660)*d)) * 0.5 * (d < 0.85), 0.45)
d = t(0.18); save("shutter", rng.standard_normal(d.size) * (np.exp(-d*60) + 0.6*np.exp(-np.maximum(d-0.07, 0)*80)*(d > 0.07)), 0.7)
d = t(0.16); save("bubble", np.sin(2*np.pi*np.cumsum(400 + 2400*d/d[-1])/SR) * env(d, r=18), 0.7)
d = t(0.6); n = rng.standard_normal(d.size); save("swoosh_soft", lowpass(n, 0.04 + 0.12*np.sin(np.pi*d/d[-1])**2) * np.sin(np.pi*d/d[-1])**2, 0.5)
d = t(0.5); save("hit", np.sin(2*np.pi*(60+140*np.exp(-d*40))*d)*env(d, r=7) + 0.5*rng.standard_normal(d.size)*np.exp(-d*35), 0.95)
d = t(0.6); save("heart", sum(np.sin(2*np.pi*55*(d-o))*np.exp(-(d-o)*18)*(d >= o) for o in (0, 0.22)), 0.9)
# gossip extras
d = t(0.9); n = rng.standard_normal(d.size); shh = n - lowpass(n, 0.35)
save("shh", lowpass(shh, 0.6) * np.minimum(1, d / 0.08) * np.exp(-np.maximum(d - 0.55, 0) * 12), 0.55)
save("notif", np.concatenate([np.sin(2*np.pi*1568*t(0.12))*np.exp(-t(0.12)*18), np.zeros(int(0.03*SR)),
                              np.sin(2*np.pi*2093*t(0.3))*np.exp(-t(0.3)*9)]), 0.6)
d = t(0.7); save("suspense", sum(np.sin(2*np.pi*f*d) for f in (233.1, 277.2, 329.6)) * np.minimum(1, d/0.05) * np.exp(-d*3.5), 0.6)


# --- music beds ---
def bed(name, bpm, bars, fn, gain=0.8):
    beat = 60/bpm; L = bars*4*beat; mix = np.zeros(int(SR*L))
    def add(sig, at, g=1.0):
        i = int(at*SR); j = min(mix.size, i+sig.size)
        if i < mix.size: mix[i:j] += g*sig[:j-i]
    fn(add, beat, bars)
    save(name, mix, gain)

kick = lambda: (lambda d: np.sin(2*np.pi*(50+110*np.exp(-d*28))*d)*np.exp(-d*8))(t(0.4))
hat = lambda dd=0.04: (lambda d: (lambda h: h-lowpass(h, 0.25))(rng.standard_normal(d.size)*np.exp(-d*100)))(t(dd))
snare = lambda: (lambda d: rng.standard_normal(d.size)*np.exp(-d*22) + 0.4*np.sin(2*np.pi*190*d)*np.exp(-d*30))(t(0.22))
def tone(f, dd, r=3.0, harm=(1,), a=0.01):
    d = t(dd); return sum(np.sin(2*np.pi*f*h*d)/h for h in harm) * env(d, a, r)

def lofi(add, b, bars):
    ch = [(220, 277.2, 329.6, 415.3), (185, 233.1, 277.2, 349.2), (196, 246.9, 293.7, 370), (174.6, 220, 261.6, 329.6)]
    for bar in range(bars):
        b0 = bar*4*b
        for f in ch[bar % 4]: add(tone(f, 4*b, 0.6, (1, 2), 0.05), b0, 0.10)
        for s in range(4):
            if s in (0, 2): add(kick(), b0+s*b, 0.45)
            if s in (1, 3): add(snare(), b0+s*b, 0.12)
        for s in range(8): add(hat(), b0+s*b/2 + (0.04 if s % 2 else 0), 0.08)
bed("music_lofi", 78, 14, lofi)

def trap(add, b, bars):
    roots = [55, 55, 49, 41.2]
    for bar in range(bars):
        b0 = bar*4*b; r = roots[bar % 4]
        add(tone(r, 2*b, 1.2, (1, 2)), b0, 0.6); add(tone(r, 2*b, 1.2, (1, 2)), b0+2.5*b, 0.5)
        add(kick(), b0, 0.8); add(kick(), b0+2.5*b, 0.6); add(snare(), b0+2*b, 0.45)
        for s in range(16 if bar % 2 else 8):
            add(hat(0.03), b0 + s*(4*b/(16 if bar % 2 else 8)), 0.12)
bed("music_trap", 140, 28, trap)

def cine(add, b, bars):
    for bar in range(bars):
        b0 = bar*4*b
        for f in (73.4, 110, 146.8, 220): add(tone(f, 4*b+0.5, 0.25, (1, 2, 3), 0.8), b0, 0.10)
        add(tone(55, 0.8, 4), b0, 0.5)
        for s in range(4): add(tone(880 if bar % 2 else 659.3, 0.3, 10), b0+s*b, 0.05)
bed("music_cine", 70, 10, cine)

def news(add, b, bars):
    seq = [220, 220, 261.6, 220, 246.9, 220, 293.7, 261.6]
    for bar in range(bars):
        b0 = bar*4*b
        for s in range(8): add(tone(seq[s] * (1 if bar % 4 < 2 else 0.89), 0.18, 14, (1, 3, 5)), b0+s*b/2, 0.22)
        add(kick(), b0, 0.6); add(kick(), b0+2*b, 0.6)
        for s in range(4): add(tone(55, 0.3, 8, (1, 2)), b0+s*b, 0.25)
bed("music_news", 120, 16, news)

def happy(add, b, bars):
    ch = [(261.6, 329.6, 392), (196, 246.9, 293.7), (220, 261.6, 329.6), (174.6, 220, 261.6)]
    for bar in range(bars):
        b0 = bar*4*b
        for s in range(8):
            for k, f in enumerate(ch[bar % 4]): add(tone(f*2, 0.35, 9, (1, 2, 3)), b0+s*b/2 + k*0.012, 0.09)
        for s in range(4):
            add(kick(), b0+s*b, 0.5 if s % 2 == 0 else 0)
            if s % 2: add(snare(), b0+s*b, 0.3)
bed("music_happy", 118, 16, happy)

def pop(add, b, bars):
    ch = [(293.7, 370, 440), (246.9, 293.7, 370), (196, 246.9, 293.7), (220, 277.2, 329.6)]
    for bar in range(bars):
        b0 = bar*4*b
        for f in ch[bar % 4]: add(tone(f, 4*b, 0.8, (1, 2), 0.02), b0, 0.08)
        for s in range(4):
            add(kick(), b0+s*b, 0.7)
            if s % 2: add(snare(), b0+s*b, 0.3)
        for s in range(8): add(hat(), b0+s*b/2+b/4, 0.12)
bed("music_pop", 105, 16, pop)
print("ok", len(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx"))))
