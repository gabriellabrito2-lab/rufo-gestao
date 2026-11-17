# TikTok Shop build (projeto tiktok-1)

Gera 10 cortes em 10 estilos de edição (+10 versões "fofoca") a partir de um vídeo bruto.

1. Copie esta pasta para `video/video-projects/<slug>/build/`.
2. Coloque o vídeo em `../raw/source.mov`, a transcrição (faster-whisper, word timestamps) em `../transcript.json` e as fontes TTF em `../fonts/`.
3. `python3 sfx2.py` (gera efeitos e trilhas) e depois `python3 build.py [ids...]`.

Estilos em `looks.py`, roteiros de corte em `plans.py`.
