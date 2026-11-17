"""TikTok Shop cuts of the same source. Times are word START times from transcript.json:
each clip runs from the word starting at `a` to the end of the word starting at `b`."""

CTA_FUNCIONA = (160.96, 163.74)   # "Realmente ele funciona, ele hidrata e dá brilho."
CTA_APROVADO = (152.70, 154.24)   # "esse produto está aprovadíssimo."

ANTES = (47.00, 52.70)            # "Essa é a realidade de um cabelo longo liso, sem finalização, sem óleo, só batendo secador."
VASSOURA = (53.20, 55.88)         # "Gente, aqui tem um corte reto, fica parecendo uma vassoura."
DIFERENCA = (75.62, 77.10)        # "Nossa gente, que diferença, hein?"
OLHA = (83.30, 84.84)             # "olha isso aqui. Que diferença."
BENEFICIOS = (16.10, 19.66)       # "Hidrata, perfuma, previne pontas duplas, tem proteção térmica"
NAO_PESA = (114.26, 116.06)       # "Não pesou nada o cabelo, tá?"
BRILHOSO = (140.86, 146.14)       # "Mas olha só, o cabelo brilhoso não está pesado, não pesou nada."
SEM_TEMPO = (66.26, 69.10)        # "Não estou com tempo pra finalizar, não tenho como escovar o meu cabelo"
APLICA = (29.38, 32.94)           # "Passar nas pontas, né, passando três de cada lado."
POUCOS_PUMPS = (24.68, 28.14)     # "passar poucos pumps, porque o cheiro já me agradou."
TIROU_VASSOURA = (156.12, 159.92) # "Tirou todo aspecto de vassoura do meu cabelo, tá gente?"
ALINHANDO = (92.06, 93.28)        # "Gente, o cabelo tá alinhando."
VOCES_VENDO = (164.12, 168.76)    # "Vocês estão vendo aqui o brilho desse cabelo. Se eu tivesse escovado..."
ANTES_DE_SECAR = (20.34, 22.22)   # "então eu vou passar ele antes de secar o meu cabelo."

# Silent B-roll (no speech): drying, product hero shot, applying
SECADOR = dict(broll=(41.5, 46.8), speed=1.8, label="SÓ SECADOR")
FRASCO = dict(broll=(38.3, 41.3), speed=1.4, mute=True)
APLICANDO = dict(broll=(86.0, 89.05), speed=1.5, label="SÓ 3 PUMPS")

PLANS = [
    dict(id="01-vassoura", look="meme", hook=["MEU CABELO PARECIA", "UMA VASSOURA"],
         clips=[VASSOURA, (ANTES, "ANTES"), (60.34, 61.74), SECADOR, (DIFERENCA, "DEPOIS"), OLHA, TIROU_VASSOURA, FRASCO],
         cta=CTA_FUNCIONA, cta_text=["TOCA NO CARRINHO LARANJA", "E GARANTE O SEU"]),
    dict(id="02-sem-tempo", look="news", hook=["SEM TEMPO PRA ESCOVA?", "FAZ ISSO AQUI"],
         clips=[SEM_TEMPO, (69.74, 71.00), (BENEFICIOS, "4 EM 1"), SECADOR, (DIFERENCA, "DEPOIS"), (97.88, 101.70), BRILHOSO, FRASCO],
         cta=CTA_APROVADO, cta_text=["TOCA NO CARRINHO LARANJA", "E TESTA VOCÊ TAMBÉM"]),
    dict(id="03-10-minutos", look="cine", hook=["Resultado em", "MENOS DE 10 MINUTOS"],
         clips=[(134.10, 136.90), (ANTES, "antes"), POUCOS_PUMPS, SECADOR, (DIFERENCA, "depois"), BRILHOSO, VOCES_VENDO, FRASCO],
         cta=CTA_FUNCIONA, cta_text=["TOCA NO CARRINHO LARANJA", "PRA TER ESSE RESULTADO"]),
    dict(id="04-4-em-1", look="check", hook=["4 EM 1 PRO SEU CABELO", "HIDRATA E PROTEGE"],
         clips=[BENEFICIOS, ANTES_DE_SECAR, (APLICA, "SÓ 3 PUMPS"), (34.90, 36.34), SECADOR, (DIFERENCA, "DEPOIS"), NAO_PESA, FRASCO],
         cta=CTA_FUNCIONA, cta_text=["TOCA NO CARRINHO LARANJA", "E GARANTE O SEU"]),
    dict(id="05-bom-e-barato", look="top3", hook=["3 MOTIVOS", "PRA TER ESSE FINALIZADOR"],
         clips=[(5.94, 6.96), ((11.36, 14.72), "#1 PREÇO"), (7.40, 10.10), (BENEFICIOS, "#2 4 EM 1"), (ANTES, "ANTES"), SECADOR, (DIFERENCA, "#3 RESULTADO"), TIROU_VASSOURA, FRASCO],
         cta=CTA_APROVADO, cta_text=["TOCA NO CARRINHO LARANJA", "CABE NO SEU BOLSO"]),
    dict(id="06-cheiro", look="aes", hook=["o cheiro desse finalizador", "É SURREAL"],
         clips=[(1.92, 5.22), POUCOS_PUMPS, APLICA, (ANTES, "antes"), SECADOR, (DIFERENCA, "depois"), BRILHOSO, FRASCO],
         cta=CTA_FUNCIONA, cta_text=["TOCA NO CARRINHO LARANJA", "E SENTE ESSE CHEIRO"]),
    dict(id="07-review-sincero", look="pov", hook=["POV: você achou um finalizador", "que funciona de verdade"],
         clips=[(160.96, 161.84), (137.18, 140.02), (ANTES, "antes"), VASSOURA, SECADOR, (DIFERENCA, "depois"), NAO_PESA, FRASCO],
         cta=CTA_APROVADO, cta_text=["TOCA NO CARRINHO LARANJA", "E comprova você mesma"]),
    dict(id="08-nao-pesa", look="girly", hook=["Finalizador que", "não pesa nada"],
         clips=[NAO_PESA, (BENEFICIOS, "4 em 1"), APLICANDO, (ANTES, "antes"), ALINHANDO, SECADOR, (BRILHOSO, "depois"), FRASCO],
         cta=CTA_FUNCIONA, cta_text=["TOCA NO CARRINHO LARANJA", "e garante o seu"]),
    dict(id="09-antes-e-depois", look="split", hook=["ANTES x DEPOIS", "SEM ESCOVA"],
         clips=[dict(split=(47.6, DIFERENCA)), (ANTES, "ANTES"), VASSOURA, SECADOR, (OLHA, "DEPOIS"), ALINHANDO, VOCES_VENDO, FRASCO],
         cta=CTA_APROVADO, cta_text=["TOCA NO CARRINHO LARANJA", "PRA TER ESSE RESULTADO"]),
    dict(id="10-sem-escova", look="classic", hook=["NEM PRECISEI", "DE ESCOVA"],
         clips=[(166.48, 168.76), SEM_TEMPO, ANTES_DE_SECAR, (ANTES, "ANTES"), SECADOR, (DIFERENCA, "DEPOIS"), (164.12, 166.04), FRASCO],
         cta=CTA_FUNCIONA, cta_text=["TOCA NO CARRINHO LARANJA", "E GARANTE O SEU"]),
]

# ---- "fofoca" versions: same cuts and looks, gossip-tone writing ----
GOSSIP = {
    "01-vassoura": (["AMIGA, DESCOBRI POR QUE", "MEU CABELO PARECIA VASSOURA"], "amiga, olha como ficou...", ["CORRE NO CARRINHO LARANJA", "E NÃO CONTA PRA NINGUÉM"]),
    "02-sem-tempo": (["O SEGREDO QUE NINGUÉM", "TE CONTA SOBRE ESCOVA"], "gente, olha isso sem escova", ["TOCA NO CARRINHO LARANJA", "ANTES QUE TODO MUNDO DESCUBRA"]),
    "03-10-minutos": (["Ninguém te conta isso...", "MAS EM 10 MINUTOS EU RESOLVI"], "nem acredito nisso amiga", ["TOCA NO CARRINHO LARANJA", "DEPOIS ME CONTA"]),
    "04-4-em-1": (["O SEGREDINHO DO MEU CABELO", "QUE EU NÃO CONTAVA PRA NINGUÉM"], "mulher, olha o depois", ["TOCA NO CARRINHO LARANJA", "E NÃO CONTA PRA NINGUÉM"]),
    "05-bom-e-barato": (["3 FOFOCAS SOBRE", "ESSE FINALIZADOR BARATINHO"], "a melhor parte vem agora", ["TOCA NO CARRINHO LARANJA", "MANDA PRA SUA AMIGA"]),
    "06-cheiro": (["psiu... vem cá", "VOU TE CONTAR UM SEGREDO"], "o resultado amiga...", ["TOCA NO CARRINHO LARANJA", "E DEPOIS ME CONTA"]),
    "07-review-sincero": (["POV: sua amiga te contando o segredo", "do cabelo dela sem escova"], "olha o depois...", ["TOCA NO CARRINHO LARANJA", "e manda pra sua amiga"]),
    "08-nao-pesa": (["Amiga, senta que", "LÁ VEM FOFOCA"], "gente, olha isso", ["TOCA NO CARRINHO LARANJA", "e não conta pra ninguém"]),
    "09-antes-e-depois": (["VOCÊS ACHAM QUE", "EU FIZ ESCOVA?"], "conta a verdade...", ["TOCA NO CARRINHO LARANJA", "MANDA PRA SUA AMIGA"]),
    "10-sem-escova": (["NINGUÉM ACREDITA QUE", "EU NÃO FIZ ESCOVA"], "amiga, olha isso...", ["TOCA NO CARRINHO LARANJA", "E NÃO CONTA PRA NINGUÉM"]),
}
for _p in list(PLANS):
    _h, _b, _c = GOSSIP[_p["id"]]
    PLANS.append(dict(_p, id=_p["id"] + "-fofoca", hook=_h, bubble=_b, cta_text=_c, gossip=True))
