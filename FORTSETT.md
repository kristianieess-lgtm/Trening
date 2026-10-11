# Fortsett her: overlevering og gjenoppretting

Dette dokumentet gjør at du (eller en ny Claude-økt) kan ta opp arbeidet uten den opprinnelige samtalen.
Sist oppdatert 11.10.2026. Repo: https://github.com/kristianieess-lgtm/Trening (privat).

## 1. Hva dette er
Et personlig treningsprosjekt for en mann på 50 år (175 cm, 90 kg, tidligere godt trent, motivasjonen på lavpunkt):

- **Mål:** definert, atletisk kropp med mer muskel (80–83 kg; vekt er sekundært, følg midje, styrke og bilder) og fullføre **halvmaraton i Madrid søndag 25. april 2027** (Zurich Rock 'n' Roll Running Series). Mål 2:15–2:30 og god opplevelse. Liker ikke å løpe.
- **Oppstart:** søndag 11. oktober 2026 (med gå/løp), styrke fra mandag 12.10.
- **Ikke ekstremt:** bærekraftig over tid, fagfellevurdert evidens. Reiser mye (1–2 netter, hotellgym).
- **Mat:** ikke fisk (laks/tunfisk), tomat, squash, sopp. Kun vanlige varer. Lunsj må være pakkbar brødmat/salat uten tilberedning.
- **Leveranser:** treningsprogram, kostholdsprogram og en offline HTML-treningsdagbok/kostholdsveileder (`dagbok.html`).
- Brukeren vil ha **delmål med avsjekk**, og at du **kvalitetssikrer mot kilder før publisering** (de har flere ganger vært kritisk til tall fra hukommelsen).

## 2. Filer
| Fil | Innhold |
|---|---|
| `dagbok.html` | Hele appen (én fil, ingen eksterne avhengigheter). Dette er masterkilden. |
| `bygg.py` | Bygger `site/` (index.html, manifest, service worker, ikoner) fra `dagbok.html`. Krever Python + Pillow. |
| `site/` | Publiserbar mobilversjon (genereres, kan bygges på nytt). |
| `forskning/01–04` | Første forskningsrunde: styrke, halvmaraton, ernæring, motivasjon/dagbokdesign. |
| `forskning/05–09` | Kvalitetssikring av øvelsene mot åpne kilder (press, trekk, ben, hofte/kjerne, armer). |
| `verktoy/sok_matvaretabellen.py` | Slå opp matvarer i Matvaretabellen for å kontrollere matbasen. |
| `minne/` | Kopi av Claude-minnenotater om prosjektet. |

## 3. Arkitektur i `dagbok.html`
Én `<script>`-blokk. Viktigste objekter (søk på navnene):

- **Program:** `START/RACE/WEEKS`, `PHASES`, `EX` (økter A/B/C/R1/R2/MIN med øvelser og sett×reps), `SESS`, `RUN1` (gå/løp uke 1–8), `RUN2` (uke 9–27), `W28` (taper/løpsuke), `planFor(k)` (én sannhet for hva som står på en dato), `effPlan(k)` (tar hensyn til reisedag).
- **Øvelsesbibliotek:** `LIB` (teknikk-tekst), `RIG` (animasjonsposer, vinkler fra rett opp, med klokka), `CUES`, `HL`, `TRK`, `CF`, og blokken «KVALITETSSIKRING» med rettelser lagt over `LIB`/`RIG`. Tegning: `rigSvg`, `frontSvg`, `faceSvg`, `topSvg`, `openEx`.
- **Mat:** `ING` (næringsverdier per 100 g, fra Matvaretabellen), `RECIPES` (27 oppskrifter med mengder og tillegg for tyngre dager), `TEMPL` (dagsmal med klokkeslett per treningstid), `dayLevel`, `dayMacros`, `energy`, `shoppingList`.
- **Matlogger:** `LG*`-funksjoner, `intake(k)`, `intakeCard`.
- **Kvalitetssikring i appen:** `selfTest()` (knapp «Kjør egentest» i Data-fanen).
- **Data:** lagres i nettleserens `localStorage` (nøkkel `treningsdagbok.v1`). Ingenting av brukerens logg ligger i repoet. Eksport/import som JSON under Data-fanen.

### Plan i korte trekk
- Uke 1–8: søn gå/løp, man styrke A, ons B, fre C (armdag). 4 dager.
- Uke 9–20: søn langtur, tir kvalitetsløp, ons A, tor valgfri rolig, fre B, lør C (armdag). 3 styrke + 2 løp.
- Uke 21–25 topp, 26–28 taper, uke 29 = løpsdag (søndag 25.4.).
- Kosthold: underskudd til og med uke 12 (`DEFICIT_TO`), vedlikehold etterpå. Nivåer: basisdag ~2 350 kcal, mer-dag ~2 700, stor dag (langtur) ~3 000. Protein 1,8 g/kg.

## 4. Slik jobber du videre
1. Endre `dagbok.html`.
2. Kjør egentesten (Data → Kjør egentest). **Alle punkter skal være grønne** før du committer.
3. Test visuelt: åpne filen i nettleser (eller en lokal server: `python3 -m http.server`).
4. `python3 bygg.py` for å bygge `site/`, og publiser den (se under).
5. Commit og push.

Nye matvarer/oppskrifter: legg til i `ING`/`RECIPES`, og verifiser mot Matvaretabellen:
```bash
curl -sL -o foods.json https://www.matvaretabellen.no/api/nb/foods.json
python3 -I verktoy/sok_matvaretabellen.py foods.json "Cottage cheese"
```

## 5. Publisering til mobil
- Netlify-prosjekt: `treningsdagbok-madrid-2027` (site-id `486358bc-1b48-42b4-8525-3b94aa0dc554`), adresse `https://treningsdagbok-madrid-2027.netlify.app`.
- Første deploy ble **dra-og-slipp av `site/`** på https://app.netlify.com/projects/treningsdagbok-madrid-2027/deploys (Mac-en hadde ikke Node/npx).
- Prosjektet er satt til at besøkende må logge inn med Netlify-konto (SSO). Alternativ: passord eller uoppdagelig åpen adresse.
- På mobil: åpne adressen, «Legg til på Hjem-skjerm». Loggen ligger i telefonens nettleser; Mac og mobil har hver sin logg (bruk eksport/import).
- Offline-funksjonen (service worker) er **ikke verifisert** i en ekte nettleser ennå.

## 6. Kjente svakheter og åpne punkter
- **Næringsverdier** er fra Matvaretabellen, men: skyr naturell er fra Tine-pakning, myseprotein/proteinbar fra produsent, kyllingpålegg satt lik kalkunfilet, og vekt per potet/løk er veiledende.
- **Øvelsesvinkler** er utledet fra kildene, ikke målt; ingen studie har testet 50-åringer med belastning. Mange kilder var kun sammendrag fordi PubMed, StatPearls og Physiopedia blokkerte agentene. Se hver rapport i `forskning/05–09`.
- **Animasjonene** er stilfigurer fra siden. De kan ikke vise albueflare, rotasjon eller bekkentilt (face pull, sidehev og pallof har egne visninger).
- **Anbefalt:** be en trener se på knebøy og markløft første gang.
- **Løpsdato:** antatt søndag 25.4.2027 (bekreftet av bruker). Sjekk offisiell dato og starttid når påmeldingen foreligger.
- **Ikke gjort:** ukentlig kroppsfettmåling er bare en påminnelse (uke 1, 13, 26). Ingen import fra klokke/Strava. Progresjon per øvelse beregnes ikke automatisk (kun «sist»-verdi).
- **Mulige neste steg:** automatisk forslag til neste vekt (dobbel progresjon), ukesoppsummering som kan deles, påminnelser, bilde-logg, bytte til 5 løp/uke dersom styrketrening og form tillater det.

## 7. Prosess som har fungert (gjenta)
- Spør om delmål før neste fase. Presenter funn kort, og vær ærlig om hva som er verifisert.
- Bruk agenter parallelt for kildesøk, og selv integrer og visuelt kontroller resultatene.
- Skriv aldri næringsverdier eller vinkler «fra hukommelsen» uten kilde.
- Hold maten enkel og pakkbar; spør før nye matvarer legges inn.
