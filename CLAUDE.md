# rufo-gestao

App web (index.html, app.js, sw.js) + kit de edição de vídeo com HyperFrames.

## Edição de vídeo

- Skills em `.claude/skills/`:
  - Oficiais HeyGen HyperFrames (Apache-2.0): `hyperframes` (ler primeiro), `hyperframes-cli`,
    `hyperframes-registry`, `media-use`, `slideshow`, `figma`, `reverse-any-video`,
    `remotion-to-hyperframes`, `style-sampling`.
  - Herk Edit Kit (MIT): `edit-video` (pipeline completo), `cut-silences`, `cut-mistakes`,
    `short-form-edit`, `short-form-video`, `video-storytelling`, `hyperframes-video-beats`,
    `gsap`, `style-library`, `make-a-video`, `motion-showreel`, `website-to-hyperframes`.
- Workspace de edição: `video/` (scripts, docs, style-library, MOTION_PHILOSOPHY.md).
  As skills do Herk citam `scripts/...`, `docs/...` e `style-library/...` relativos a `video/`.
  Guia original: `video/WORKSPACE-GUIDE.md`.
- Projetos ficam em `video/video-projects/<slug>/` (ignorado pelo git, junto com mídias e renders).
- Setup: `cd video && npm install` (instala hyperframes, gsap, playwright). ffmpeg já existe no ambiente.
- Chaves de API (ElevenLabs etc.) nunca no repo; ver `video/docs/TOOLS-AND-API-KEYS.md`.
