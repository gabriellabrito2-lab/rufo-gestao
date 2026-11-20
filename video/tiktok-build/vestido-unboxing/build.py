"""Render TikTok Shop cuts, each in its own editing look (see looks.py).
Usage: python3 build.py [plan-id ...]"""
import json, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
PROXY = os.path.join(PROJ, "proxy")
FONTS = os.path.join(PROJ, "fonts")
SFX = os.path.join(HERE, "sfx")
OUT = os.path.join(PROJ, "renders")
TMP = os.path.join(HERE, "tmp")
sys.path.insert(0, HERE)
from plans import PLANS  # noqa: E402
from looks import LOOKS, STYLE_LINES, YELLOW, WHITE  # noqa: E402

W, H, FPS = 1080, 1920, 30
HOLD_END = 1.3
from plans import FIX  # noqa: E402  {(src, start): word}
LAB_Y = {"fun": 1420, "meme": 1400, "news": 1360, "cine": 1350, "aes": 1480, "pov": 1400, "girly": 1400}

WORDS = {}
for _f in sorted(os.listdir(os.path.join(PROJ, "tr"))):
    if _f.endswith(".m.json"):
        _src = _f[:-7]; WORDS[_src] = json.load(open(os.path.join(PROJ, "tr", _f)))["words"]
        for w in WORDS[_src]:
            w["src"] = _src
            if (_src, w["start"], w["word"]) in FIX: w["word"] = FIX[(_src, w["start"], w["word"])]


def SRC(src):
    return os.path.join(PROXY, f"{src}.mp4")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); raise SystemExit(f"failed: {' '.join(cmd[:8])}")


def subclips(src, a, b, gap):
    words = WORDS[src]
    idx_at = lambda t: min(range(len(words)), key=lambda i: abs(words[i]["start"] - t))
    i, j = idx_at(a), idx_at(b)
    seg, out = [words[i]], []
    for k in range(i + 1, j + 1):
        if words[k]["start"] - words[k - 1]["end"] > gap:
            out.append(seg); seg = []
        seg.append(words[k])
    out.append(seg)
    res = []
    for s in out:
        kl = words.index(s[-1])
        nxt = words[kl + 1]["start"] if kl + 1 < len(words) else s[-1]["end"] + 0.3
        res.append((max(0.0, s[0]["start"] - 0.06), min(s[-1]["end"] + 0.14, nxt - 0.03), s))
    return res


def ts(t):
    cs = int(round(max(0, t) * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def ev(start, end, text, style, layer=0):
    return f"Dialogue: {layer},{ts(start)},{ts(end)},{style},,0,0,0,,{text}"


def rect(x0, y0, x1, y1):
    return f"m {x0} {y0} l {x1} {y0} l {x1} {y1} l {x0} {y1}"


POP_IN = r"\fscx30\fscy30\t(0,140,\fscx112\fscy112)\t(140,240,\fscx100\fscy100)"
ANIM = {
    "pop": POP_IN,
    "shake": POP_IN + "".join(r"\t(%d,%d,\frz%d)" % (240 + 90 * k, 330 + 90 * k, (5 if k % 2 else -5)) for k in range(30)),
    "slam": r"\fscx260\fscy260\alpha&HFF&\t(0,160,\fscx100\fscy100\alpha&H00&)",
    "fade": r"\fad(450,0)",
    "none": "",
}


def tempo_chain(sp):
    if 0.5 <= sp <= 2.0:
        return f"atempo={sp:.4f}"
    parts = []
    while sp > 2.0:
        parts.append("atempo=2.0"); sp /= 2.0
    return ",".join(parts + [f"atempo={sp:.4f}"])


def motion(look, n, hook, dur):
    m = look["motion"]
    if m == "punch":
        z = "1+0.28*max(0,1-t/0.35)" if hook else ("1.0" if n % 2 == 0 else "1.10")
        sh = "+if(lt(t,0.3),14*sin(t*95),0)" if hook else ""
    elif m == "chaos":
        z = f"{[1.0, 1.18, 1.3][n % 3]}+0.25*max(0,1-t/0.2)"
        sh = "+if(lt(t,0.22),20*sin(t*120),0)"
    elif m == "smooth":
        z = "1.14-0.14*min(1,t/0.9)" if hook else f"1+0.07*t/{dur:.3f}"
        sh = ""
    else:
        z, sh = "1.0", ""
    return z, sh


def vchain(z, sh, extra="", ypos=0.35):
    return (f"fps={FPS},scale=w='trunc({W}*({z})/2)*2':h='trunc({H}*({z})/2)*2':eval=frame,"
            f"crop={W}:{H}:x='(iw-{W})/2{sh}':y='(ih-{H})*{ypos}',{extra}setsar=1,format=yuv420p")


ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-r", str(FPS), "-c:a", "pcm_s16le", "-ac", "2"]


def is_antes(label):
    return bool(label) and label.lower() == "antes"


def is_depois(label):
    return bool(label) and (label.lower() == "depois" or label.startswith("#3"))


# ---------------- captions ----------------
def fmt_word(wd, case):
    if case == "upper": return wd.upper().strip(".,;:")
    if case == "lower": return wd.lower().strip(".,;:")
    return wd


def captions(timed, cap):
    mode, sty, y, n, case = cap["mode"], cap["style"], cap["y"], cap["n"], cap["case"]
    evs = []
    if mode == "word":
        rnd = random.Random(3); cols = [WHITE, YELLOW, "&H00FFFF00", WHITE]
        for k, (s, e, wd) in enumerate(timed):
            nxt = timed[k + 1][0] if k + 1 < len(timed) else e + 0.2
            tag = r"{\pos(540,%d)\frz%d\1c%s&\fscx150\fscy150\t(0,90,\fscx100\fscy100)}" % (y, rnd.randint(-7, 7), cols[k % 4])
            evs.append([s, max(nxt, s + 0.12), tag + fmt_word(wd, case)])
    else:
        groups, g = [], []
        for item in timed:
            if g and (len(g) >= n or item[0] - g[-1][1] > 0.35):
                groups.append(g); g = []
            g.append(item)
            if item[2][-1:] in ".,?!" and mode != "sentence":
                groups.append(g); g = []
            elif item[2][-1:] in ".?!":
                groups.append(g); g = []
        if g: groups.append(g)
        for g in groups:
            if mode == "karaoke":
                for k, (s, e, _) in enumerate(g):
                    nxt = g[k + 1][0] if k + 1 < len(g) else g[-1][1] + 0.12
                    parts = [(r"{\c%s&\fscx114\fscy114}" % cap["hi"] + fmt_word(wd, case) + r"{\c&HFFFFFF&\fscx100\fscy100}")
                             if m == k else fmt_word(wd, case) for m, (_, _, wd) in enumerate(g)]
                    intro = r"\fscx80\fscy80\t(0,90,\fscx100\fscy100)" if k == 0 else ""
                    evs.append([s, nxt, r"{\pos(540,%d)%s}" % (y, intro) + " ".join(parts)])
            else:
                txt = " ".join(fmt_word(wd, case) for _, _, wd in g)
                if mode == "sentence":
                    txt = txt[:1].upper() + txt[1:]
                fade = r"\fad(120,80)" if mode == "soft" else ""
                evs.append([g[0][0], g[-1][1] + 0.15, r"{\pos(540,%d)%s}" % (y, fade) + txt])
    evs.sort(key=lambda x: x[0])
    for k in range(len(evs) - 1):
        evs[k][1] = min(evs[k][1], evs[k + 1][0])
    return [ev(a, b, t, sty, 2) for a, b, t in evs if b > a]


ARROW = r"{\an7\bord4\3c&H000000&\1c&H00006AFF&\p1}m 60 0 l 120 60 l 75 105 l 115 145 l 0 145 l 0 30 l 40 70 l 60 0{\p0}"
CHECK = r"{\an7\bord3\3c&H000000&\1c&H0050D050&\p1}m 0 30 l 14 16 l 26 30 l 56 0 l 70 14 l 26 58 l 0 30{\p0}"
TICKER = "  FINALIZADOR QUE HIDRATA  •  PERFUMA  •  PROTEGE DO CALOR  •  TIRA O ASPECTO DE VASSOURA  •  NÃO PESA  •  TOCA NO CARRINHO LARANJA  •"


def src_to_out(segs, src, t):
    for s in segs:
        if s.get("speed", 1) == 1 and s.get("src") == src and s["src_start"] <= t < s["src_end"]:
            return s["off"] + (t - s["src_start"])
    return None


STYLE_INFO = {ln.split(",")[0][7:]: (ln.split(",")[1], float(ln.split(",")[2])) for ln in STYLE_LINES}


def fit(text, style, maxw=960):
    """Scale tag that keeps the widest line inside the safe width."""
    font, size = STYLE_INFO.get(style, ("", 80))
    k = 0.44 if font in ("Anton", "Bebas Neue") else 0.5 if font in ("Bangers", "Playfair Display", "Pacifico") else 0.6
    longest = max(len(x) for x in text.replace(r"\N", "|").split("|"))
    w = longest * size * k
    if w <= maxw: return ""
    sc = int(100 * maxw / w)
    return r"{\fscx%d\fscy%d}" % (sc, sc)


def build_ass(plan, look, lname, segs, total, cta_start, label_marks, extras_sfx):
    L = ["[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\nWrapStyle: 2\nScaledBorderAndShadow: yes\n" % (W, H),
         "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
         *STYLE_LINES, "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    if look.get("letterbox"):
        L.append(ev(0, total, r"{\pos(0,0)\1c&H000000&\bord0\p1}" + rect(0, 0, W, 130) + " " + rect(0, H - 130, W, H) + r"{\p0}", "Draw", 1))
    if look.get("progress"):
        L.append(ev(0, total, r"{\pos(0,0)\1c%s&\bord0\clip(0,0,0,16)\t(0,%d,\clip(0,0,1080,16))\p1}%s{\p0}" % (look["progress"], int(total * 1000), rect(0, 0, W, 16)), "Draw", 5))
    if look.get("news"):
        L.append(ev(0, total, r"{\pos(40,150)}URGENTE", "NewsBar", 6))
        blink = "".join(r"\t(%d,%d,\alpha&HFF&)\t(%d,%d,\alpha&H00&)" % (k * 1000 + 500, k * 1000 + 510, k * 1000 + 990, k * 1000 + 1000) for k in range(int(total) + 1))
        L.append(ev(0, total, r"{\pos(330,128)\1c&H2020FF&\bord3\3c&HFFFFFF&%s\p1}m 22 0 b 34 0 44 10 44 22 b 44 34 34 44 22 44 b 10 44 0 34 0 22 b 0 10 10 0 22 0{\p0}" % blink, "Draw", 6))
        L.append(ev(0, total, r"{\pos(0,0)\1c&H000000&\1a&H40&\bord0\p1}" + rect(0, 1450, W, 1512) + r"{\p0}", "Draw", 3))
        L.append(ev(0, total, r"{\move(1080,1481,-3400,1481)}" + plan.get("ticker", TICKER) * 2, "NewsTick", 4))
    if look.get("snow"):
        rnd = random.Random(11)
        k = 0; t0 = 0.0
        while t0 < total:
            for _ in range(6):
                x = rnd.randint(0, W); dur = rnd.uniform(4.5, 8.0); r = rnd.randint(5, 12); st = t0 + rnd.uniform(0, 1.0)
                L.append(ev(st, min(total, st + dur), r"{\move(%d,-30,%d,%d)\1c&HFFFFFF&\1a&H50&\bord0\blur2\p1}m 0 0 b %d 0 %d %d 0 %d b -%d %d -%d 0 0 0{\p0}" % (x, x + rnd.randint(-80, 80), H + 30, r, r, r, r, r, r, r), "Draw", 4))
            t0 += 1.0
    if look.get("frame"):
        L.append(ev(0, total, r"{\pos(0,0)\1c&HFFFFFF&\bord0\p1}" + " ".join([rect(0, 0, W, 28), rect(0, H - 28, W, H), rect(0, 0, 28, H), rect(W - 28, 0, W, H)]) + r"{\p0}", "Draw", 5))
    # hook
    hook_end = max(plan.get("hook_min", 2.8), segs[0]["clip_end"])
    anim = ANIM.get(look.get("hook_anim", "pop"), "")
    QUICK = r"\fscx90\fscy90\t(0,120,\fscx100\fscy100)"
    if plan.get("instant_hook"):
        anim = QUICK + (anim[len(POP_IN):] if anim.startswith(POP_IN) else "")
    for sty, y, delay, tags, li in look["hook"]:
        if plan.get("instant_hook"): delay = 0.0
        text = r"\N".join(plan["hook"]) if li == "both" else plan["hook"][li]
        if plan.get("hook_low") and not (li == "both" and lname == "split"):
            y = {0: 1330, 1: 1465, "both": 1400}[li]
        if look.get("hook_anim") == "slide" and not plan.get("instant_hook"):
            L.append(ev(delay, hook_end, r"{\move(-700,%d,540,%d,0,220)%s}" % (y, y, tags) + text, sty, 6))
        else:
            f_ = fit(text, sty)
            if f_:
                sc = f_[6:f_.index("\\", 6)]
                anim_f = anim.replace("fscx100", "fscx" + sc).replace("fscy100", "fscy" + sc).replace("fscx112", "fscx" + sc).replace("fscy112", "fscy" + sc)
                L.append(ev(delay, hook_end, r"{\pos(540,%d)\fscx%s\fscy%s%s%s}" % (y, sc, sc, anim_f, tags) + text, sty, 6))
            else:
                L.append(ev(delay, hook_end, r"{\pos(540,%d)%s%s}" % (y, anim, tags) + text, sty, 6))
    # transitions drawn in ASS
    tr = look["trans"]
    for s in segs[1:]:
        if not s["first_of_clip"]: continue
        o = s["off"]
        if tr == "flash":
            L.append(ev(o, o + 0.14, r"{\pos(0,0)\1c&HFFFFFF&\bord0\fad(0,130)\p1}" + rect(0, 0, W, H) + r"{\p0}", "Draw", 9))
        elif tr == "black":
            L.append(ev(o - 0.1, o + 0.2, r"{\pos(0,0)\1c&H000000&\bord0\fad(100,200)\p1}" + rect(0, 0, W, H) + r"{\p0}", "Draw", 9))
        elif tr == "softwhite":
            L.append(ev(o - 0.06, o + 0.3, r"{\pos(0,0)\1c&HFFFFFF&\1a&H50&\bord0\fad(60,240)\p1}" + rect(0, 0, W, H) + r"{\p0}", "Draw", 9))
        elif tr == "gold":
            L.append(ev(o, o + 0.24, r"{\pos(0,0)\1c&H37AFD4&\1a&H30&\bord0\fad(0,220)\p1}" + rect(0, 0, W, H) + r"{\p0}", "Draw", 9))
        elif tr == "pink":
            L.append(ev(o, o + 0.22, r"{\pos(0,0)\1c&HC9A0FF&\1a&H40&\bord0\fad(0,210)\p1}" + rect(0, 0, W, H) + r"{\p0}", "Draw", 9))
    # split-screen tags
    for s in segs:
        if s.get("split"):
            e = s["off"] + s["dur"]
            L.append(ev(s["off"], e, r"{\pos(0,0)\1c&HFFFFFF&\bord0\p1}" + rect(0, 954, W, 966) + r"{\p0}", "Draw", 5))
            t1, t2 = s.get("split_tags", ("ANTES", "DEPOIS"))
            L.append(ev(s["off"] + 0.1, e, r"{\pos(40,60)%s}%s" % (POP_IN, t1), "SplitTag", 6))
            L.append(ev(s["off"] + 0.4, e, r"{\pos(40,1000)%s}%s" % (POP_IN, t2), "SplitTagG", 6))
    # labels
    lab = look["lab"]; ly = LAB_Y.get(lname, lab["y"])
    for t0, t1, text in label_marks:
        if lab.get("numbers") and text.startswith("#"):
            num, rest = text[1], text[3:]
            L.append(ev(t0, min(t1, t0 + 2.6), r"{\pos(180,760)%s}%s" % (ANIM["slam"], num), "TopNum", 7))
            L.append(ev(t0 + 0.12, min(t1, t0 + 2.6), r"{\pos(540,%d)%s}%s" % (ly, POP_IN, rest), "TopLab", 7))
            continue
        sty = lab["ANTES"] if is_antes(text) else lab["DEPOIS"] if is_depois(text) else lab["other"]
        col = ""
        if is_depois(text) and lab.get("depois_color"): col = r"\3c%s&" % lab["depois_color"]
        if is_antes(text) and lab.get("antes_color"): col = r"\3c%s&" % lab["antes_color"]
        f_ = fit(text, sty); sc = f_[6:f_.index("\\", 6)] if f_ else "100"
        pin = POP_IN.replace("fscx100", "fscx" + sc).replace("fscy100", "fscy" + sc).replace("fscx112", "fscx" + str(int(int(sc) * 1.1))).replace("fscy112", "fscy" + str(int(int(sc) * 1.1)))
        L.append(ev(t0 + 0.05, min(t1, t0 + plan.get("beat_max", 2.4)), r"{\pos(540,%d)\frz%d%s%s}" % (ly, lab["rot"], col, pin) + text.replace("|", r"\N"), sty, 7))
    # checklist + stamp
    if look.get("checklist"):
        mapped = [(src_to_out(segs, plan["check"][0], a), txt) for a, txt in plan.get("check", (None, []))[1]]
        mapped = [(a, txt) for a, txt in mapped if a is not None]
        if mapped:
            end = mapped[-1][0] + 2.6
            for k, (a, txt) in enumerate(mapped):
                y = 1320 + k * 86
                L.append(ev(a, end, r"{\pos(36,%d)%s}" % (y - 30, POP_IN) + CHECK, "Draw", 7))
                L.append(ev(a, end, r"{\pos(118,%d)\fs64%s}%s" % (y, POP_IN, txt), "ChkItem", 7))
                extras_sfx.append(("tick", a, 0.8))
            extras_sfx.append(("ding", mapped[-1][0] + 0.25, 0.5))
        brolls = [s for s in segs if s.get("broll") and s["off"] < cta_start]
        if brolls:
            s = brolls[-1]
            L.append(ev(s["off"] + 0.1, cta_start, r"{\pos(540,430)\frz-8%s}APROVADO" % ANIM["slam"], "ChkStamp", 8))
            extras_sfx.append(("hit", s["off"] + 0.1, 0.9))
    # gossip chat bubble before the reveal
    if plan.get("bubble"):
        dep = [t0 for t0, _, tx in label_marks if is_depois(tx)]
        if dep:
            b0 = max(0.3, dep[0] - 1.7); b1 = dep[0] + 1.0
            L.append(ev(b0, b1, r"{\pos(70,205)\fad(120,150)}Amiga", "BubbleName", 8))
            L.append(ev(b0, b1, r"{\pos(70,268)\fad(120,150)\fscx60\fscy60\t(0,160,\fscx100\fscy100)}" + plan["bubble"], "Bubble", 8))
            extras_sfx.append(("notif", b0, 0.7))
            extras_sfx.append(("suspense", max(0, dep[0] - 0.05), 0.35))
    if plan.get("gossip"):
        extras_sfx.append(("shh", 0.0, 0.8))
    # captions
    timed = []
    for s in segs:
        for w in s["words"]:
            st = s["off"] + (w["start"] - s["src_start"]); en = s["off"] + (w["end"] - s["src_start"])
            if w["word"]: timed.append((max(st, s["off"]), en, w["word"]))
    if not plan.get("no_caps"):
        L += captions(timed, look["cap"])
    # CTA
    c1, c2 = plan["cta_text"]
    pulse = "".join(r"\t(%d,%d,\fscx108\fscy108)\t(%d,%d,\fscx100\fscy100)" % (300 + 600 * k, 600 + 600 * k, 600 + 600 * k, 900 + 600 * k) for k in range(8))
    L.append(ev(cta_start, total, r"{\pos(540,760)%s%s}" % (POP_IN, pulse) + c1, f"Cta_{lname}", 8))
    L.append(ev(cta_start + 0.3, total, r"{\pos(540,890)%s}" % POP_IN + c2, f"CtaS_{lname}", 8))
    bounce = "".join(r"\t(%d,%d,\fscx112\fscy112)\t(%d,%d,\fscx100\fscy100)" % (250 * k, 250 * k + 125, 250 * k + 125, 250 * k + 250) for k in range(20))
    L.append(ev(cta_start + 0.2, total, r"{\move(250,1420,190,1500,0,400)" + bounce + "}" + ARROW, "Draw", 8))
    L.append(ev(cta_start + 0.2, total, r"{\an4\pos(330,1580)}PRODUTO AQUI", f"CtaS_{lname}", 8))
    return "\n".join(L) + "\n"


def render(plan):
    os.makedirs(TMP, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    pid, lname = plan["id"], plan["look"]
    look = LOOKS[lname]; gap = look.get("gap", 0.45)
    clips = plan["clips"] + [plan["cta"]]
    segs, off, n, label_marks, cta_start = [], 0.0, 0, [], None

    def add_seg(f, dur, **kw):
        nonlocal off, n
        segs.append(dict(file=f, off=off, dur=dur, **kw)); off += dur; n += 1

    for ci, c in enumerate(clips):
        clip_off = off
        hook = ci == 0
        label = c.get("label")
        f = os.path.join(TMP, f"{pid}-{n:02d}.mp4")
        if c["kind"] == "broll":
            src = c["src"]; a, b = c["a"], c["b"]; sp = c.get("speed", 1.0)
            is_cta = ci == len(clips) - 1
            if is_cta: cta_start = off
            if look.get("slowmo") and c.get("slow_ok", True):
                b = min(b, a + 1.8); sp = 0.6
            dur = (b - a) / sp
            z, sh = motion(look, n, hook, dur)
            if look["motion"] in ("punch", "static"): z = f"1+0.10*t/{dur:.3f}"
            vf = f"setpts=(PTS-STARTPTS)/{sp}," + vchain(z, sh)
            vol = 0 if c.get("mute", True) else 0.45
            af = f"asetpts=PTS-STARTPTS,{tempo_chain(sp)},volume={vol},aresample=44100,afade=t=in:d=0.05,afade=t=out:st={max(0, dur - 0.08):.3f}:d=0.08"
            if is_cta:
                vf += f",tpad=stop_mode=clone:stop_duration={HOLD_END}"; af += f",apad=pad_dur={HOLD_END}"; dur += HOLD_END
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{b - a:.3f}", "-i", SRC(src), "-vf", vf, "-af", af, *ENC, "-t", f"{dur:.3f}", f])
            add_seg(f, dur, src=src, src_start=a, src_end=b, speed=sp, words=[], first_of_clip=True, broll=True)
        elif c["kind"] == "split":
            (tsrc, top), bot = c["top"], c["bot"]; src, a, b = bot["src"], bot["a"], bot["b"]
            st, en, ws = subclips(src, a, b, 99)[0]
            dur = en - st
            fc = (f"[0:v]setpts=PTS-STARTPTS,fps={FPS},crop={W}:960:0:(ih-960)*0.40{',hue=s=0' if c.get('bw', True) else ''}[t];"
                  f"[1:v]setpts=PTS-STARTPTS,fps={FPS},crop={W}:960:0:(ih-960)*0.40[b];[t][b]vstack,setsar=1,format=yuv420p[v];"
                  f"[1:a]asetpts=PTS-STARTPTS,aresample=44100,afade=t=in:d=0.015,afade=t=out:st={dur - 0.03:.3f}:d=0.03[a]")
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{top:.3f}", "-t", f"{dur:.3f}", "-i", SRC(tsrc), "-ss", f"{st:.3f}", "-t", f"{dur:.3f}", "-i", SRC(src),
                 "-filter_complex", fc, "-map", "[v]", "-map", "[a]", *ENC, "-t", f"{dur:.3f}", f])
            add_seg(f, dur, src=src, src_start=st, src_end=en, words=ws, first_of_clip=True, split=True,
                    split_tags=c.get("tags", ("ANTES", "DEPOIS")))
        else:
            src, a, b = c["src"], c["a"], c["b"]
            is_cta = ci == len(clips) - 1
            if is_cta: cta_start = off
            subs = subclips(src, a, b, gap)
            for si, (st, en, ws) in enumerate(subs):
                dur = en - st
                z, sh = motion(look, n, hook and si == 0, dur)
                extra = "hue=s=0," if (is_antes(label) and look.get("antes_bw")) else ""
                vf = "setpts=PTS-STARTPTS," + vchain(z, sh, extra)
                af = f"asetpts=PTS-STARTPTS,aresample=44100,afade=t=in:d=0.015,afade=t=out:st={max(0, dur - 0.03):.3f}:d=0.03"
                last = is_cta and si == len(subs) - 1
                if last:
                    vf += f",tpad=stop_mode=clone:stop_duration={HOLD_END}"; af += f",apad=pad_dur={HOLD_END}"
                f = os.path.join(TMP, f"{pid}-{n:02d}.mp4")
                run(["ffmpeg", "-v", "error", "-y", "-ss", f"{st:.3f}", "-t", f"{en - st:.3f}", "-i", SRC(src), "-vf", vf, "-af", af, *ENC,
                     "-t", f"{dur + (HOLD_END if last else 0):.3f}", f])
                add_seg(f, dur + (HOLD_END if last else 0), src=src, src_start=st, src_end=en, words=ws, first_of_clip=si == 0)
        if ci == 0:
            for s in segs: s["clip_end"] = off
        if label:
            label_marks.append((clip_off, off, label))
    total = off
    lst = os.path.join(TMP, f"{pid}.txt")
    open(lst, "w").write("".join(f"file '{s['file']}'\n" for s in segs))
    body = os.path.join(TMP, f"{pid}-body.mkv")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", body])

    extras_sfx = []
    ass = os.path.join(TMP, f"{pid}.ass")
    open(ass, "w", encoding="utf-8").write(build_ass(plan, look, lname, segs, total, cta_start, label_marks, extras_sfx))

    # ---- audio ----
    sx = look["sfx"]
    sfx = [(nm, 0.0, v) for nm, v in sx["hook"]]
    if sx.get("cut"):
        nm, v = sx["cut"]; pre = 0.18 if "whoosh" in nm or "swoosh" in nm else 0.0
        sfx += [(nm, max(0, s["off"] - pre), v) for s in segs[1:] if s["first_of_clip"]]
    for t0, _, text in label_marks:
        if is_depois(text) and sx.get("depois"):
            nm, v = sx["depois"]; sfx.append((nm, max(0, t0 - (0.3 if nm == "scratch" else 0) + 0.05), v))
        elif sx.get("label"):
            nm, v = sx["label"]; sfx.append((nm, t0 + 0.05, v))
        if look["lab"].get("numbers") and text.startswith("#"):
            sfx.append(("whoosh", max(0, t0 - 0.15), 0.5))
    sfx += [(nm, max(0, cta_start + o), v) for nm, o, v in sx["cta"]]
    sfx += extras_sfx
    if plan.get("silent"):
        sfx = []
    inputs = ["-i", body]
    fc = ["[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[v]"]
    mix = ["[v]"]; k0 = 1
    if look.get("music") and not plan.get("silent"):
        mname, mvol = look["music"]
        inputs += ["-stream_loop", "-1", "-i", os.path.join(SFX, mname + ".wav")]
        fc.append(f"[1:a]atrim=0:{total:.3f},volume={mvol},afade=t=out:st={total - 1.2:.3f}:d=1.2[m]"); mix.append("[m]"); k0 = 2
    for k, (nm, at, vol) in enumerate(sfx):
        inputs += ["-i", os.path.join(SFX, nm + ".wav")]
        d = int(at * 1000)
        fc.append(f"[{k + k0}:a]volume={vol},adelay={d}|{d}[s{k}]"); mix.append(f"[s{k}]")
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[a]")
    # ---- video: grade + ffmpeg-side transitions + graphics ----
    cuts = [s["off"] for s in segs[1:] if s["first_of_clip"]]
    win = "+".join(f"between(t,{c - 0.06:.3f},{c + 0.12:.3f})" for c in cuts) or "0"
    chain = [look["grade"]] if look["grade"] else []
    if look["trans"] == "glitch":
        chain.append(f"rgbashift=rh=-30:bh=30:rv=8:enable='{win}'"); chain.append(f"noise=alls=45:allf=t:enable='{win}'")
    if look["trans"] == "blur":
        bw = "+".join(f"between(t,{c - 0.08:.3f},{c + 0.08:.3f})" for c in cuts) or "0"
        chain.append(f"gblur=sigma=38:steps=2:enable='{bw}'")
    assf = ass.replace(":", r"\:")
    chain.append(f"subtitles=filename='{assf}':fontsdir='{FONTS}'")
    fc.append("[0:v]" + ",".join(chain) + "[vo]")
    out = os.path.join(OUT, f"tiktok-{pid}.mp4")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vo]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.3f}", out])
    print(f"{out}  {total:.1f}s  [{lname}]", flush=True)
    return out


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for p in PLANS:
        if not want or p["id"] in want:
            render(p)
