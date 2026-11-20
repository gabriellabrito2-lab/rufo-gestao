"""Ten distinct editing looks. Colours are ASS &HAABBGGRR."""

WHITE, BLACK = "&H00FFFFFF", "&H00000000"
YELLOW, RED, GREEN, ORANGE = "&H0000E5FF", "&H00552CFE", "&H0050B000", "&H00006AFF"
GOLD, PINK, HOTPINK, NEWSRED = "&H0037AFD4", "&H00C9A0FF", "&H009314FF", "&H002020D0"


def S(name, font, size, prim=WHITE, outl=BLACK, back=BLACK, bold=0, italic=0, bs=1, ol=6, sh=0, align=5, sp=0):
    return (f"Style: {name},{font},{size},{prim},{prim},{outl},{back},{bold},{italic},0,0,100,100,{sp},0,"
            f"{bs},{ol},{sh},{align},40,40,0,1")


MONT, BANG, ARCH, PLAY, POP, ANTON, BEBAS, PACI, MARK = (
    "Montserrat Thin Black", "Bangers", "Archivo Black", "Playfair Display", "Poppins SemiBold",
    "Anton", "Bebas Neue", "Pacifico", "Permanent Marker")

STYLE_LINES = [
    # classic
    S("Cap", MONT, 86, ol=7, sh=4, back="&H64000000"),
    S("HookW", MONT, 88, "&H00111111", WHITE, WHITE, bs=3, ol=22, align=8),
    S("HookR", MONT, 98, WHITE, RED, RED, bs=3, ol=22, align=8),
    S("LabR", MONT, 96, WHITE, "&H003030E0", "&H003030E0", bs=3, ol=20),
    S("LabG", MONT, 96, WHITE, GREEN, GREEN, bs=3, ol=20),
    S("LabY", MONT, 84, "&H00111111", "&H0000D8FF", "&H0000D8FF", bs=3, ol=20),
    # meme
    S("MemeCap", BANG, 150, ol=9, sh=5),
    S("MemeHook", BANG, 175, YELLOW, BLACK, BLACK, ol=11, sh=6, align=8),
    S("MemeHook2", BANG, 160, WHITE, BLACK, BLACK, ol=10, sh=6, align=8),
    S("MemeLab", BANG, 150, WHITE, RED, RED, ol=10, sh=4),
    # news
    S("NewsBar", ARCH, 54, WHITE, NEWSRED, NEWSRED, bs=3, ol=16, align=7),
    S("NewsHead", ARCH, 70, BLACK, WHITE, WHITE, bs=3, ol=18, align=8),
    S("NewsHead2", ARCH, 70, WHITE, NEWSRED, NEWSRED, bs=3, ol=18, align=8),
    S("NewsCap", ARCH, 72, ol=6, sh=3),
    S("NewsTick", ARCH, 44, WHITE, BLACK, BLACK, bs=3, ol=14, align=4),
    S("NewsLab", ARCH, 74, WHITE, NEWSRED, NEWSRED, bs=3, ol=16),
    # cinematic
    S("CineHook", PLAY, 112, GOLD, BLACK, "&H80000000", bold=-1, italic=-1, ol=0, sh=3, align=8),
    S("CineSub", POP, 58, WHITE, BLACK, "&H80000000", ol=0, sh=2, align=8, sp=8),
    S("CineCap", POP, 74, WHITE, BLACK, "&H90000000", ol=0, sh=3),
    S("CineLab", PLAY, 104, GOLD, BLACK, "&H80000000", bold=-1, italic=-1, ol=0, sh=3),
    # checklist
    S("ChkHook", ANTON, 150, WHITE, BLACK, BLACK, ol=7, sh=4, align=8),
    S("ChkHook2", ANTON, 118, WHITE, GREEN, GREEN, bs=3, ol=18, align=8),
    S("ChkCap", ANTON, 112, ol=7, sh=4),
    S("ChkItem", ANTON, 70, WHITE, "&H50000000", "&H50000000", bs=3, ol=14, align=4),
    S("ChkStamp", ANTON, 130, WHITE, "&H002020E8", "&H002020E8", bs=3, ol=20),
    S("ChkLab", ANTON, 112, WHITE, BLACK, BLACK, bs=3, ol=18),
    # top 3
    S("TopHook", BEBAS, 168, YELLOW, BLACK, BLACK, ol=9, sh=5, align=8),
    S("TopHook2", BEBAS, 140, WHITE, BLACK, BLACK, ol=7, sh=4, align=8),
    S("TopNum", BEBAS, 400, YELLOW, BLACK, BLACK, ol=14, sh=8),
    S("TopLab", BEBAS, 136, BLACK, YELLOW, YELLOW, bs=3, ol=18),
    S("TopCap", BEBAS, 140, ol=7, sh=4),
    # aesthetic
    S("AesHook", PLAY, 124, WHITE, BLACK, "&H60000000", bold=-1, italic=-1, ol=0, sh=3, align=8),
    S("AesHook2", POP, 62, WHITE, BLACK, "&H60000000", ol=0, sh=2, align=8, sp=6),
    S("AesCap", POP, 82, WHITE, BLACK, "&H70000000", ol=0, sh=3),
    S("AesLab", POP, 92, "&H00333333", WHITE, WHITE, bs=3, ol=16),
    # pov / native
    S("PovText", POP, 76, WHITE, "&H00101010", "&H00101010", bs=3, ol=16, align=8),
    S("PovCap", POP, 74, WHITE, "&H00101010", "&H00101010", bs=3, ol=14),
    S("PovLab", POP, 80, "&H00101010", WHITE, WHITE, bs=3, ol=14),
    # girly
    S("GirlHook", PACI, 108, WHITE, HOTPINK, HOTPINK, ol=8, sh=4, align=8),
    S("GirlHook2", MARK, 92, HOTPINK, WHITE, WHITE, ol=7, sh=3, align=8),
    S("GirlCap", MARK, 88, WHITE, HOTPINK, HOTPINK, ol=7, sh=3),
    S("GirlLab", MARK, 96, WHITE, HOTPINK, HOTPINK, bs=3, ol=18),
    # split
    S("SplitHook", MONT, 110, WHITE, BLACK, BLACK, ol=8, sh=4, align=5),
    S("SplitTag", MONT, 76, WHITE, "&H003030E0", "&H003030E0", bs=3, ol=16, align=7),
    S("SplitTagG", MONT, 76, WHITE, GREEN, GREEN, bs=3, ol=16, align=7),
    S("Draw", "Arial", 20, ol=0, align=7),
    # natal
    S("NatalHook", PLAY, 122, GOLD, "&H001010A0", BLACK, bold=-1, italic=-1, ol=4, sh=4, align=8),
    S("NatalHook2", MONT, 84, WHITE, "&H002020C8", "&H002020C8", bs=3, ol=20, align=8),
    S("NatalCap", MONT, 84, ol=7, sh=4),
    S("NatalLab", MONT, 90, WHITE, "&H002020C8", "&H002020C8", bs=3, ol=20),
    # editorial
    S("EdHook", PLAY, 160, WHITE, BLACK, "&H70000000", bold=-1, italic=-1, ol=0, sh=4, align=8),
    S("EdKick", POP, 58, WHITE, BLACK, "&H70000000", ol=0, sh=2, align=8, sp=14),
    S("EdCap", POP, 66, WHITE, BLACK, "&H80000000", ol=0, sh=3, sp=3),
    S("EdLab", POP, 86, BLACK, WHITE, WHITE, bs=3, ol=16, sp=6),
    # fun (unboxing)
    S("FunLab", BANG, 130, BLACK, YELLOW, YELLOW, bs=3, ol=20),
    S("FunHook", BANG, 150, WHITE, "&H00FF7F00", BLACK, ol=10, sh=6, align=8),
    S("FunHook2", BANG, 135, YELLOW, BLACK, BLACK, ol=10, sh=6, align=8),
    # gossip chat bubble
    S("Bubble", POP, 64, "&H00202020", WHITE, "&H50000000", bs=3, ol=20, sh=0, align=7),
    S("BubbleName", POP, 46, "&H0040A000", WHITE, WHITE, bs=1, ol=0, align=7),
]
for nm, font, sz in (("classic", MONT, 82), ("meme", BANG, 104), ("news", ARCH, 70), ("cine", PLAY, 78),
                     ("check", ANTON, 92), ("top3", BEBAS, 120), ("aes", POP, 66), ("pov", POP, 64),
                     ("girly", MARK, 84), ("split", MONT, 82), ("natal", MONT, 80), ("editorial", POP, 66), ("fun", BANG, 104)):
    it = -1 if font == PLAY else 0
    STYLE_LINES.append(S(f"Cta_{nm}", font, sz, WHITE, ORANGE, ORANGE, bold=it, italic=it, bs=3, ol=24))
    STYLE_LINES.append(S(f"CtaS_{nm}", font if font not in (BEBAS, ANTON) else POP, int(sz * 0.75), WHITE, BLACK, BLACK,
                         bold=it, italic=it, bs=3, ol=16))

LOOKS = {
    "classic": dict(
        motion="punch", trans="flash", grade="eq=contrast=1.05:saturation=1.1", progress=RED,
        hook=[("HookW", 250, 0.0, "", 0), ("HookR", 400, 0.25, "", 1)], hook_anim="pop",
        cap=dict(mode="karaoke", style="Cap", y=1190, hi=YELLOW, n=3, case="upper"),
        lab=dict(ANTES="LabR", DEPOIS="LabG", other="LabY", y=1350, rot=-4),
        sfx=dict(hook=[("boom", 0.9)], cut=("whoosh", 0.55), label=("pop", 0.6), depois=("ding", 0.6),
                 cta=[("riser", -1.2, 0.35), ("chaching", 0.05, 0.75), ("pop", 0.35, 0.5)]),
        music=("beat", 0.11)),
    "meme": dict(
        motion="chaos", trans="glitch", grade="eq=contrast=1.15:saturation=1.45", progress=YELLOW,
        hook=[("MemeHook", 210, 0.0, r"\frz4", 0), ("MemeHook2", 400, 0.2, r"\frz-3", 1)], hook_anim="shake",
        cap=dict(mode="word", style="MemeCap", y=1150, n=1, case="upper"),
        lab=dict(ANTES="MemeLab", DEPOIS="MemeLab", other="MemeLab", y=560, rot=8, depois_color=GREEN),
        sfx=dict(hook=[("vineboom", 1.0)], cut=("glitch", 0.5), label=("vineboom", 0.7), depois=("scratch", 0.7),
                 cta=[("vineboom", 0.0, 0.6), ("chaching", 0.15, 0.8)]),
        music=("music_trap", 0.10)),
    "news": dict(
        motion="punch", trans="black", grade="eq=contrast=1.1:saturation=0.95", news=True,
        hook=[("NewsHead", 250, 0.1, "", 0), ("NewsHead2", 370, 0.35, "", 1)], hook_anim="slide",
        cap=dict(mode="karaoke", style="NewsCap", y=1180, hi=YELLOW, n=3, case="upper"),
        lab=dict(ANTES="NewsLab", DEPOIS="NewsLab", other="NewsLab", y=600, rot=0, depois_color=GREEN),
        sfx=dict(hook=[("alarm", 0.45), ("hit", 0.7)], cut=("hit", 0.35), label=("tick", 0.8), depois=("ding", 0.6),
                 cta=[("alarm", 0.0, 0.3), ("chaching", 0.2, 0.7)]),
        music=("music_news", 0.13)),
    "cine": dict(
        motion="smooth", trans="black", slowmo=True, letterbox=True,
        grade="colorbalance=rs=0.06:gs=0.01:bs=-0.06:rh=0.04:bh=-0.05,eq=contrast=1.08:saturation=0.85,noise=alls=9:allf=t,vignette=PI/4.5",
        hook=[("CineHook", 260, 0.0, "", 0), ("CineSub", 410, 0.5, "", 1)], hook_anim="fade",
        cap=dict(mode="soft", style="CineCap", y=1500, n=4, case="lower"),
        lab=dict(ANTES="CineLab", DEPOIS="CineLab", other="CineLab", y=600, rot=0),
        sfx=dict(hook=[("hit", 0.8), ("riser", 0.3)], cut=("swoosh_soft", 0.45), label=None, depois=("sparkle", 0.5),
                 cta=[("hit", 0.0, 0.6), ("chaching", 0.25, 0.5)]),
        music=("music_cine", 0.16)),
    "check": dict(
        motion="punch", trans="blur", grade="eq=contrast=1.1:saturation=1.05,unsharp=5:5:0.6", progress=GREEN,
        antes_bw=True, checklist=True,
        hook=[("ChkHook", 230, 0.0, "", 0), ("ChkHook2", 410, 0.25, "", 1)], hook_anim="pop",
        cap=dict(mode="karaoke", style="ChkCap", y=1230, hi="&H0050FF50", n=2, case="upper"),
        lab=dict(ANTES="ChkLab", DEPOIS="ChkLab", other="ChkLab", y=1390, rot=0, depois_color=GREEN, antes_color="&H003030E0"),
        sfx=dict(hook=[("hit", 0.9)], cut=("whoosh", 0.5), label=("tick", 0.8), depois=("ding", 0.6),
                 cta=[("riser", -1.2, 0.3), ("chaching", 0.05, 0.75)]),
        music=("music_pop", 0.10)),
    "top3": dict(
        motion="punch", trans="flash", grade="eq=contrast=1.12:saturation=1.2", progress=YELLOW,
        hook=[("TopHook", 200, 0.0, "", 0), ("TopHook2", 390, 0.25, "", 1)], hook_anim="slam",
        cap=dict(mode="karaoke", style="TopCap", y=1210, hi=YELLOW, n=2, case="upper"),
        lab=dict(ANTES="TopLab", DEPOIS="TopLab", other="TopLab", y=1390, rot=0, numbers=True),
        sfx=dict(hook=[("hit", 1.0)], cut=("whoosh", 0.5), label=("hit", 0.9), depois=("hit", 0.9),
                 cta=[("riser", -1.2, 0.35), ("chaching", 0.05, 0.75)]),
        music=("music_trap", 0.09)),
    "aes": dict(
        motion="smooth", trans="softwhite",
        grade="eq=brightness=0.03:contrast=0.96:saturation=0.88,colorbalance=rs=0.05:gs=0.01:bs=-0.03",
        hook=[("AesHook", 270, 0.0, "", 0), ("AesHook2", 430, 0.5, "", 1)], hook_anim="fade",
        cap=dict(mode="soft", style="AesCap", y=1330, n=4, case="lower"),
        lab=dict(ANTES="AesLab", DEPOIS="AesLab", other="AesLab", y=620, rot=0),
        sfx=dict(hook=[("sparkle", 0.6)], cut=("swoosh_soft", 0.45), label=("bubble", 0.5), depois=("sparkle", 0.55),
                 cta=[("sparkle", 0.0, 0.5), ("chaching", 0.2, 0.55)]),
        music=("music_lofi", 0.15)),
    "pov": dict(
        motion="static", trans="none", grade="", gap=0.6,
        hook=[("PovText", 300, 0.0, "", "both")], hook_anim="none",
        cap=dict(mode="sentence", style="PovCap", y=1220, n=6, case="keep"),
        lab=dict(ANTES="PovLab", DEPOIS="PovLab", other="PovLab", y=640, rot=0),
        sfx=dict(hook=[("tick", 0.7)], cut=None, label=("tick", 0.7), depois=("tick", 0.7),
                 cta=[("tick", 0.0, 0.7), ("chaching", 0.2, 0.45)]),
        music=None),
    "girly": dict(
        motion="smooth", trans="pink",
        grade="colorbalance=rs=0.08:gs=-0.02:bs=0.05,eq=saturation=1.1:brightness=0.02", progress=HOTPINK,
        hook=[("GirlHook", 230, 0.0, r"\frz3", 0), ("GirlHook2", 400, 0.3, r"\frz-3", 1)], hook_anim="pop",
        cap=dict(mode="karaoke", style="GirlCap", y=1200, hi="&H00FFE0FF", n=2, case="lower"),
        lab=dict(ANTES="GirlLab", DEPOIS="GirlLab", other="GirlLab", y=600, rot=-7),
        sfx=dict(hook=[("bubble", 0.7), ("sparkle", 0.5)], cut=("bubble", 0.5), label=("bubble", 0.6), depois=("sparkle", 0.6),
                 cta=[("sparkle", 0.0, 0.5), ("chaching", 0.15, 0.7)]),
        music=("music_happy", 0.10)),
    "split": dict(
        motion="punch", trans="flash", grade="eq=contrast=1.06:saturation=1.08", progress=WHITE, antes_bw=True,
        hook=[("SplitHook", 960, 0.0, "", "both")], hook_anim="pop",
        cap=dict(mode="karaoke", style="Cap", y=1190, hi=YELLOW, n=3, case="upper"),
        lab=dict(ANTES="LabR", DEPOIS="LabG", other="LabY", y=1350, rot=-4),
        sfx=dict(hook=[("shutter", 0.8), ("boom", 0.7)], cut=("shutter", 0.5), label=("pop", 0.6), depois=("ding", 0.6),
                 cta=[("riser", -1.2, 0.35), ("chaching", 0.05, 0.75)]),
        music=("music_pop", 0.10)),
}

LOOKS["natal"] = dict(
    motion="smooth", trans="gold", grade="colorbalance=rs=0.05:bs=-0.04,eq=saturation=1.12:contrast=1.05", snow=True, progress=GOLD,
    hook=[("NatalHook", 220, 0.0, "", 0), ("NatalHook2", 400, 0.35, "", 1)], hook_anim="pop",
    cap=dict(mode="karaoke", style="NatalCap", y=1200, hi=GOLD, n=3, case="upper"),
    lab=dict(ANTES="NatalLab", DEPOIS="NatalLab", other="NatalLab", y=1380, rot=-3),
    sfx=dict(hook=[("sleigh", 0.7), ("bells", 0.6)], cut=("sleigh", 0.35), label=("bells", 0.5), depois=("bells", 0.6),
             cta=[("bells", 0.0, 0.6), ("chaching", 0.2, 0.7)]),
    music=("music_xmas", 0.13))
LOOKS["editorial"] = dict(
    motion="smooth", trans="none", grade="eq=contrast=1.1:saturation=0.92", frame=True,
    hook=[("EdKick", 150, 0.0, "", 1), ("EdHook", 210, 0.15, "", 0)], hook_anim="fade",
    cap=dict(mode="soft", style="EdCap", y=1440, n=3, case="upper"),
    lab=dict(ANTES="EdLab", DEPOIS="EdLab", other="EdLab", y=1300, rot=0),
    sfx=dict(hook=[("shutter", 0.9)], cut=("shutter", 0.6), label=("tick", 0.6), depois=("shutter", 0.7),
             cta=[("shutter", 0.0, 0.7), ("chaching", 0.2, 0.6)]),
    music=("music_runway", 0.12))
LOOKS["fun"] = dict(
    motion="chaos", trans="flash", grade="eq=contrast=1.1:saturation=1.35", progress=YELLOW,
    hook=[("FunHook", 200, 0.0, r"\frz-3", 0), ("FunHook2", 370, 0.25, r"\frz3", 1)], hook_anim="shake",
    cap=dict(mode="word", style="MemeCap", y=1180, n=1, case="upper"),
    lab=dict(ANTES="FunLab", DEPOIS="FunLab", other="FunLab", y=560, rot=-6),
    sfx=dict(hook=[("vineboom", 0.9)], cut=("whoosh", 0.5), label=("bubble", 0.8), depois=("chaching", 0.6),
             cta=[("riser", -1.2, 0.35), ("chaching", 0.05, 0.8)]),
    music=("music_happy", 0.11))
