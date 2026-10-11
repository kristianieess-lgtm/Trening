---
name: trening-halvmaraton-2027
description: "Personlig trenings-/kostholdsprosjekt (mann 50, halvmaraton Madrid 25.4.2027); mappe ~/Desktop/Trening, eget repo, rammer og status"
metadata:
  node_type: memory
  type: project
  originSessionId: 77a5ad7c-b2df-424b-b597-172d618c2be3
  modified: 2026-10-11T11:43:54.787Z
---

Privat prosjekt (ikke Ocab) i `~/Desktop/Trening` (eget lokalt git-repo, commit c1021fc). GitHub-repo https://github.com/kristianieess-lgtm/Trening (opprettet av brukeren, pushet 2026-10-11, branch main). Innhold: `dagbok.html` (offline dagbok + kostholdsveileder, localStorage, JSON-eksport), `forskning/01–04-*.md` (agentrapporter med verifiserte kilder).

Rammer: mann 50 år, 175 cm, 90 kg. Start søndag 11.10.2026. Halvmaraton søndag 25.4.2027 (Zurich Rock 'n' Roll Running Series Madrid), mål 2:15–2:30, liker ikke å løpe. Ikke fisk (laks/tunfisk), tomat, squash. Reiser ofte 1–2 netter med hotellgym.

Tidligere vekt 75–78 kg (kickboksing 3x/uke) så «tynn» ut; ønsker større muskler, «fitness»-kropp, ikke stor. Mål nå 80–83 kg med mer muskel, vekt sekundært (midje, styrke, bilder, BIA/DEXA uke 1/13/26). Vil ha dagbok som fil på Mac, mobil er en fordel.

Mobil: Netlify-prosjekt `treningsdagbok-madrid-2027` (id 486358bc-1b48-42b4-8525-3b94aa0dc554) er opprettet, men ikke deployet: Mac har ikke node/npx, så deploy må gjøres ved dra-og-slipp av `~/Desktop/Trening/site` eller ved at node installeres. Prosjektet har SSO-teamlogin på besøkende (må avklares: passord/offentlig). `python3 bygg.py` lager site/. Service worker kunne ikke testes i in-app-nettleseren. Øvelsene (32+2) kvalitetssikret mot åpne kilder via 5 agenter (forskning/05–09); animasjoner rettet. Brukeren vil ha en ukentlig armdag: Styrke C = armdag (biceps, hammer, triceps over hodet, pushdown, sidehev, face pull, kjerne). Svakhet: PubMed/StatPearls/Physiopedia blokkerte agentene; mange vinkler er avledet, ikke målt. Kosthold v2 (oktober 2026): dagsmeny med klokkeslett per treningsdag (treningstid morgen/lunsj/kveld), 36 oppskrifter med eksakte mengder (g + skiver/dl), bytt-alternativer, handleliste, egentest i Data-fanen. Plan-fanen viser nå alle 7 dager per uke (tidligere viste den bare løp og ga mismatch mot I dag). Brukeren vil «imponere», kvalitetssikre før publisering; publisering på Netlify/mobil (alternativ A + offline-pakke) venter på ja. Delmål 3 (godkjent): underskudd kortet til 12 uker; 3 styrkeøkter (A/B/C, C = overkropp) gjennom hele perioden + 2 løp (kvalitet, langtur) + valgfri rolig økt. Dagbok har øvelsesbibliotek (32 øvelser, SVG-animasjon med muskelmarkering, bevegelsessti, tempo-tidslinje). Brukeren ba om «bedre animasjoner» – stilfigur-rig i dagbok.html (RIG/LIB/CUES). Preview av lokale filer fungerer bare via lokal http-server fra scratchpad. Avklart/godkjent 11.10.2026: 4 dager/uke økt til 5 etter 8 uker; nesten null løpebase; ingen helsehensyn. Faser: 1–8 komme i gang (3 styrke + 1 gå/løp), 9–20 bygg (2 styrke + 3 kondisjon), 21–25 topp, 26–28 taper, uke 29 løpsdag. Kosthold: underskudd uke 1–16, vedlikehold etterpå.

**Why:** Brukeren vil ha delmål med avsjekk underveis, ikke ekstremversjoner; fagfellevurdert evidens.
**How to apply:** Presenter delmål og spør før neste fase. Hold adskilt fra Ocab. Ingen gh-CLI; auto-modus nektet å hente git-credential for API-kall, så brukeren oppretter tomt privat repo selv og jeg pusher via vanlig git. Se [[lenke-til-siste-oppdatering]].
