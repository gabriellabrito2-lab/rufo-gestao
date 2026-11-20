"""Vestido vermelho (12 cortes) + unboxing divertido. Times are word START times in tr/<src>.m.json."""


def sp(src, a, b, label=None):
    return dict(kind="speech", src=src, a=a, b=b, label=label)


def br(src, a, b, speed=1.0, label=None, slow_ok=True):
    return dict(kind="broll", src=src, a=a, b=b, speed=speed, label=label, mute=True, slow_ok=slow_ok)


def L(c, label):
    return dict(c, label=label)


FIX = {
    ("9508", 31.08, "R"): "R$20,", ("9508", 31.38, "$20"): "", ("9508", 31.38, ",00,"): "",
    ("9508", 32.84, "R"): "R$20!", ("9508", 33.28, "$20"): "", ("9508", 33.28, ",00."): "",
    ("9515", 48.76, "1"): "1,63,", ("9515", 49.02, ",63,"): "",
    ("9509", 7.30, "1"): "1,70m.", ("9509", 7.52, ",70m."): "",
    ("9516", 6.84, "acentura."): "acintura.", ("9517", 14.46, "recote"): "recorte",
    ("9514", 2.62, "Reveillon."): "Réveillon.", ("9511", 6.22, "My"): "MyMate,", ("9511", 6.44, "Mate,"): "",
}

# ---- spoken hooks (she recorded several takes) ----
H_ENCONTREI = sp("9516", 0.00, 3.00)    # "Encontrei o vestido mais lindo de Natal aqui no TikTok."
H_COMPREI = sp("9517", 0.00, 4.30)      # "Comprei o vestido princesa mais lindo do TikTok, vou mostrar agora pra vocês."
H_MEU = sp("9515", 24.26, 26.04)        # "Acho que encontrei o meu vestido de natal."
H_VERMELHO = sp("9513", 18.50, 20.12)   # "Gente, comprei um vestido vermelho pro Natal."
H_DEVOLVI = sp("9513", 56.86, 59.26)    # "Eu devolvi um essa semana porque o tecido era transparente."
H_VERDE = sp("9513", 23.16, 27.16)      # "Se ele ficar bom também eu vou comprar o verde... Natal de verde ou de vermelho."
H_MARIDO = sp("9513", 49.00, 50.48)     # "Vou vestir e ver se meu marido aprova."

# ---- development ----
D_TECIDO = sp("9515", 33.06, 36.94)     # "Gente, ele é maravilhoso, o tecido dele é suplex, não ficou transparente,"
D_CINTURA = sp("9515", 37.82, 41.20)    # "olha a cintura que ele deu, modelou o corpo,"
D_NAO_TRANSP = sp("9515", 42.22, 43.44) # "não fica nada transparente,"
D_RODADISSIMO = sp("9515", 45.20, 48.36)  # "rodadíssimo embaixo, tamanho é midi, tá?"
D_ALTURA = sp("9515", 48.46, 49.02)     # "Eu tenho 1,63,"
D_CORES = sp("9515", 50.02, 52.34)      # "tem várias cores e eu escolhi esse vermelho para o natal,"
D_ACHARAM = sp("9515", 52.66, 53.16)    # "o que vocês acharam?"
D_LONGO = sp("9515", 33.06, 48.36)      # whole review run (for checklist)
D_ACINTURA = sp("9516", 4.48, 6.84)     # "Olha que maravilhoso, o quanto ele acintura."
D_RODADO_PRINC = sp("9516", 7.86, 10.04)  # "E o melhor, ele é rodado e estilo princesa."
D_RECORTE = sp("9516", 10.58, 13.76)    # "Esse recorte princesa, gente, deu todo o toque especial do vestido."
D_AMEI = sp("9516", 22.74, 23.24)       # "Eu amei."
D_PERFEICAO = sp("9517", 5.02, 6.98)    # "Olha que perfeição de vestido,"
D_SUPER_RODADO = sp("9517", 8.34, 10.06)  # "super rodado, tamanho midi,"
D_CORES2 = sp("9517", 11.52, 13.38)     # "tem várias cores, eu escolhi a vermelha pro natal."
D_MODELAGEM = sp("9517", 14.04, 18.64)  # "Tem esse recorte princesa que dá toda uma modelagem no corpo, gente, eu amei."
U_SUPLEX = sp("9513", 42.82, 44.66)     # "é bom, é suplex. Ele é no suplex."
U_NAO_TRANSP = sp("9513", 51.74, 53.96) # "Gente, mas assim, o tecido é bom, tá? Não é transparente."
U_PRINCESA = sp("9513", 60.68, 62.40)   # "Ele é rodado, estilo princesa, de manguinha."
U_APROVADO = sp("9513", 72.54, 73.52)   # "Estou sentindo que ele está aprovado."

# ---- silent B-roll ----
B_GIRO = br("9516", 16.0, 21.5, 1.3)          # spin, skirt flares
B_TRANSICAO = br("9518", 1.0, 13.0, 2.6, slow_ok=False)  # walks out of frame and comes back
B_VOLTA = br("9518", 8.5, 13.0, 1.4)          # walking back toward camera
B_POSE_CORPO = br("9515", 1.0, 5.0, 1.2)      # full body walk
B_POSE_CINTURA = br("9515", 5.0, 11.5, 1.6)   # closer poses, waist
B_POSE_INTEIRO = br("9515", 12.0, 18.0, 1.6)  # full-body poses
B_POSE_FINAL = br("9518", 13.0, 19.5, 1.6)
B_EMBALAGEM = br("9513", 29.8, 33.5, 1.3)     # pulling the red dress out of the bag

# ---- CTAs (her own voice) ----
CTA_BLACK = sp("9515", 54.52, 60.50)    # "Gente, ele tem oferta de black, corre aqui no carrinho laranja e já garante o seu, que vestido lindo!"

TICKER_VESTIDO = "  VESTIDO PRINCESA  •  TECIDO SUPLEX  •  NÃO É TRANSPARENTE  •  SUPER RODADO  •  TAMANHO MIDI  •  VÁRIAS CORES  •  OFERTA DE BLACK NO CARRINHO LARANJA  •"
CHECK_9515 = ("9515", [(35.32, "TECIDO SUPLEX"), (36.94, "NÃO É TRANSPARENTE"), (39.18, "MARCA A CINTURA"), (45.20, "RODADÍSSIMO"), (47.76, "TAMANHO MIDI")])

PLANS = [
    dict(id="v01-achei", look="classic", hook=["ACHEI O VESTIDO DE NATAL", "MAIS LINDO DO TIKTOK"],
         clips=[H_ENCONTREI, L(B_POSE_CINTURA, "OLHA ISSO"), D_ACINTURA, D_RODADO_PRINC, L(B_GIRO, "RODADO"), D_RECORTE, D_CORES],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "OFERTA DE BLACK"]),
    dict(id="v02-natal", look="natal", hook=["Natal de vermelho?", "ACHEI O VESTIDO PERFEITO"],
         clips=[H_MEU, B_POSE_CORPO, D_TECIDO, D_CINTURA, D_RODADISSIMO, L(B_GIRO, "RODADÍSSIMO"), D_CORES],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "E BRILHA NO NATAL"]),
    dict(id="v03-devolvi", look="pov", hook=["POV: você devolveu um vestido transparente", "e achou esse aqui"],
         clips=[H_DEVOLVI, L(B_TRANSICAO, "depois"), D_TECIDO, D_NAO_TRANSP, D_CINTURA, B_GIRO, D_RODADISSIMO],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "e não conta pra ninguém"],
         gossip=True, bubble="amiga, esse não é transparente..."),
    dict(id="v04-embalagem", look="split", hook=["DA EMBALAGEM", "PRO CORPO"],
         clips=[dict(kind="split", top=("9513", 30.6), bot=H_ENCONTREI, bw=False, tags=("NA EMBALAGEM", "NO CORPO")),
                U_PRINCESA, L(B_TRANSICAO, "NO CORPO"), D_ACINTURA, D_RECORTE, B_GIRO],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "E GARANTE O SEU"]),
    dict(id="v05-editorial", look="editorial", hook=["O vestido princesa", "EDIÇÃO DE NATAL"],
         clips=[H_COMPREI, B_POSE_INTEIRO, D_PERFEICAO, D_SUPER_RODADO, D_MODELAGEM, B_GIRO],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "LINK NO CARRINHO"]),
    dict(id="v06-cinema", look="cine", hook=["Achei o meu", "VESTIDO DE NATAL"],
         clips=[H_MEU, B_POSE_CORPO, D_CINTURA, D_RODADISSIMO, B_GIRO, D_CORES, B_POSE_FINAL],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "OFERTA DE BLACK"]),
    dict(id="v07-checklist", look="check", hook=["CHECKLIST DO VESTIDO", "DE NATAL PERFEITO"], check=CHECK_9515,
         clips=[H_ENCONTREI, D_LONGO, B_GIRO],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "E GARANTE O SEU"]),
    dict(id="v08-3-motivos", look="top3", hook=["3 MOTIVOS PRA USAR", "ESSE VESTIDO NO NATAL"],
         clips=[H_VERMELHO, L(D_TECIDO, "#1 TECIDO"), L(D_ACINTURA, "#2 CINTURA"), B_POSE_CINTURA, L(D_SUPER_RODADO, "#3 RODADO"), B_GIRO],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "OFERTA DE BLACK"]),
    dict(id="v09-verde-ou-vermelho", look="girly", hook=["Natal de verde", "ou de vermelho?"],
         clips=[H_VERDE, L(B_TRANSICAO, "vermelho!"), D_PERFEICAO, D_RECORTE, B_GIRO, D_CORES2, D_ACHARAM],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "e escolhe a sua cor"]),
    dict(id="v10-alerta", look="news", hook=["ALERTA DE ACHADINHO", "VESTIDO DE NATAL NO TIKTOK"], ticker=TICKER_VESTIDO,
         clips=[H_ENCONTREI, D_TECIDO, D_NAO_TRANSP, D_RODADISSIMO, D_ALTURA, D_CORES, B_GIRO],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "ANTES QUE A OFERTA ACABE"]),
    dict(id="v11-aesthetic", look="aes", hook=["o vestido mais lindo", "QUE EU JÁ COMPREI NO TIKTOK"],
         clips=[H_COMPREI, B_VOLTA, D_ACINTURA, D_PERFEICAO, B_POSE_FINAL, D_MODELAGEM],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "E SE APAIXONA TAMBÉM"]),
    dict(id="v12-marido-aprovou", look="meme", hook=["SERÁ QUE O MARIDO", "APROVOU O VESTIDO?"],
         clips=[H_MARIDO, U_APROVADO, L(B_TRANSICAO, "DEPOIS"), D_TECIDO, D_CINTURA, L(B_GIRO, "APROVADO"), D_ACHARAM],
         cta=CTA_BLACK, cta_text=["TOCA NO CARRINHO LARANJA", "E MANDA PRO SEU MARIDO"],
         gossip=True, bubble="amiga, ele aprovou..."),
    # ---- unboxing divertido ----
    dict(id="u01-unboxing-black", look="fun", hook=["TUDO QUE EU COMPREI", "NA BLACK DO TIKTOK"],
         clips=[sp("9507", 0.76, 4.14), sp("9507", 10.96, 13.24),
                L(sp("9508", 18.54, 23.08), "1. TRIPÉ"), sp("9508", 23.70, 28.20), sp("9508", 28.42, 33.28),
                sp("9508", 39.06, 43.12), sp("9509", 2.78, 7.52), sp("9510", 5.66, 8.50), L(sp("9510", 13.68, 14.54), "APROVADO"),
                L(sp("9511", 4.18, 7.86), "2. BABYLISS"), sp("9511", 12.20, 14.28), sp("9511", 26.64, 28.32), sp("9511", 32.38, 34.72),
                L(sp("9512", 18.16, 24.64), "3. FERRO A VAPOR"), sp("9512", 8.82, 10.90),
                L(H_VERMELHO, "4. VESTIDO DE NATAL"), H_DEVOLVI, L(B_TRANSICAO, "NO CORPO"), D_ACINTURA,
                L(sp("9514", 0.96, 2.62), "5. VESTIDO BRANCO"), sp("9514", 18.80, 24.64), sp("9514", 26.16, 27.78), sp("9514", 47.86, 50.42)],
         cta=sp("9511", 29.54, 31.28), cta_text=["TOCA NO CARRINHO LARANJA", "TEM TUDO NO MEU CARRINHO"]),
]

for _p in PLANS:
    _p["hook_low"] = True
