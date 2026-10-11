# Trening og kosthold – halvmaraton Madrid 25.4.2027

Privat prosjekt: 28 ukers program (styrke + halvmaraton) og kostholdsveileder.

- `dagbok.html` – offline treningsdagbok og kostholdsveileder med øvelsesbibliotek (32 øvelser med animasjon, teknikk og vanlige feil). Åpne filen i nettleseren (Mac eller mobil). Data lagres i nettleseren; bruk *Data → Eksporter* jevnlig.
- Kosthold: dagsmeny med klokkeslett per treningsdag, 27 enkle oppskrifter med nøyaktige mengder (g, skiver, dl), bytt-alternativer, handleliste per uke. Ingen fisk, tomat, squash eller sopp, og ingen uvanlige varer.
- Matlogger: søk opp mat eller oppskrift, oppgi mengde (g, skiver, stk, dl) og få protein/karbo/fett/kcal av det du faktisk har spist. Egne matvarer kan legges inn.
- Næringsverdier og porsjonsvekter er hentet fra Matvaretabellen.no (Mattilsynet) og kontrollert 11.10.2026; unntak er listet i Data-fanen.
- Ukentlig armdag (Styrke C): biceps curl, hammer curl, triceps over hodet, pushdown, sidehev, face pull.
- Øvelsene er kvalitetssikret mot åpne kilder (rapportene forskning/05–09); animasjonene er rettet etter funnene.
- `forskning/` – forskningsnotater med verifiserte kilder (styrke, halvmaraton, ernæring, motivasjon).

## Rammer
- Start søndag 11.10.2026, løp søndag 25.4.2027 (Zurich Rock 'n' Roll Running Series Madrid). Mål 2:15–2:30.
- 4 dager/uke i uke 1–8 (3 styrke + 1 gå/løp), deretter 5 dager (3 styrke + 2 løp + valgfri rolig økt).
- Energiunderskudd uke 1–12, vedlikehold etterpå. Mål 80–83 kg med mer muskel; vekt er sekundært.
- Kosthold uten fisk (laks/tunfisk), tomat og squash.

## Publisere til mobil
`python3 bygg.py` lager mappen `site/` (index.html, manifest, service worker, ikoner). Last mappen opp på Netlify-prosjektet `treningsdagbok-madrid-2027` (Deploys → dra og slipp `site`). På mobilen: åpne adressen og velg «Legg til på Hjem-skjerm».

## Oppdatere
Rediger `dagbok.html` (programdata ligger øverst i skriptet), commit og push.
