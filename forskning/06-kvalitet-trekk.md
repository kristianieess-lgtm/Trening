# Kvalitetssikring: trekk- og roingsøvelser (teknikk og animasjonsgeometri)

Gjelder: manualroing, kabelroing, nedtrekk, strikknedtrekk, pull-ups, TRX-/strikkroing, face pull, biceps curl.
Målgruppe: mann 50 år, hobbyutøver. Fokus: skuldre, albuer, nakke, korsrygg.
Kontrollert mot `dagbok.html` (LIB- og RIG-objektene). Filen er ikke endret.

## 0. Hovedkonklusjon og ærlig forbehold

| Øvelse | Verdict | Kort begrunnelse |
|---|---|---|
| Manualroing | OK (små tekstgrep) | Sidegeometrien er riktig. Mangler at albuen skal holdes nær kroppen og når en skal stoppe. |
| Kabelroing | MÅ ENDRES | Animasjonen svinger overkroppen 15° og ender 5° bak loddlinjen, noe teksten selv forbyr. Albuen går ca. 25° bak overkroppen. |
| Nedtrekk | MÅ ENDRES | Sluttposisjon har albuen ca. 30° bak overkroppen (20° bak lodd), mot kildenes «stopp når albuene går bakover». |
| Strikknedtrekk | MÅ ENDRES | Samme rigg som nedtrekk, samme feil. Teksten sier «står på kne», figuren sitter. |
| Pull-ups | MÅ ENDRES | Albuen 23° bak overkroppen i toppen, grepsbredden «litt bredere» bør strammes inn. |
| TRX-/strikkroing | MÅ ENDRES (verst) | Sluttposen har overarmen ca. 105° bak overkroppen og albuen helt sammenfoldet (180°). Anatomisk umulig/uønsket. |
| Face pull | MÅ ENDRES | Sideriggen kan ikke vise albue-ut. Overarm ca. 85° bak kroppen i slutt, kabel i brysthøyde mens teksten sier øyehøyde. |
| Biceps curl | OK | Geometrien stemmer. Legg til sikkerhetsnote om strak arm under tung last (distal bicepssene). |

Viktige forbehold om kildegrunnlaget:

- Jeg fant ingen studie som isolerer «albuevinkel 45° mot 90°» alene. Tallene under er avledet av studier som varierer skulderabduksjon, av ACE-instruksjoner og av klinisk resonnement. De er merket som slutning der de ikke står eksplisitt i en kilde.
- Ingen av EMG-studiene måler skade. «Skadelig» er i hovedsak biomekanisk resonnement, ikke påvist skaderate.
- Jeg fant ingen EMG-studie av selve kabel-face-pull. Kildene for face pull er derfor indirekte (bånd-pull-apart, eksternrotasjonsstudier, ACE «high row») pluss trenerkilder av lavere kvalitet.
- NCBI Bookshelf/StatPearls og Physiopedia ga 403 eller bot-sjekk fra verktøyene mine. PMC-artikler ble lest via Europe PMC (åpen fulltekst-XML) og NCBI E-utilities.

## 1. Rigg-konvensjon og beregningsmetode

Rig-vinkler er verdensvinkler (0 = opp, 90 = frem, 180 = ned). For å sammenligne med anatomi regnet jeg om til vinkler relativt til overkroppen:

- Overarmens vinkel mot overkroppen, S = (to + 180) − ua. Positiv S = arm foran overkroppslinjen (fleksjon), negativ S = bak overkroppslinjen (ekstensjon). S = 0 betyr at overarmen ligger langs overkroppen.
- Albuefleksjon E = |fa − ua|. 0 = strak arm.
- Overkroppslean = `to` (0 = oppreist, negativ = bakover).

Normal aktiv skulderekstensjon (arm bak kroppen) oppgis til ca. 45–60° (Healthline, forbrukerkilde). Rigg-siden viser bare sagittalplanet, så den kan ikke vise at albuene går ut til siden (abduksjon). Dette er sentralt for roing og face pull, se punkt 8.

Nåværende RIG, omregnet:

| Øvelse | Pose | Overkropp | Overarm mot overkropp (S) | Albuefleksjon |
|---|---|---|---|---|
| manualroing | 0 → 1 | 70° (nesten horisontal) | 70° fleksjon → 5° fleksjon | 0° → 65° |
| kabelroing | 0 → 1 | +10° → −5° | 110° fleksjon → 25° ekstensjon | 5° → 120° |
| nedtrekk/strikk | 0 → 1 | −10° | 165° fleksjon → 30° ekstensjon | 0° → 170° |
| pullups | 0 → 1 | 0° → −8° | 180° → 23° ekstensjon | 0° → 180° |
| trx | 0 → 1 | −50° → −35° | 75° fleksjon → 105° ekstensjon | 0° → 180° |
| facepull | 0 → 1 | −5° | 85° fleksjon → 85° ekstensjon | 0° → 170° |
| biceps | 0 → 1 | 0° | ca. 5° → 10° fleksjon | 5° → 155° |

Merknad: i pullups er albuefleksjon 180° i tallet over et artefakt av at underarmen peker opp og overarmen ned. I virkeligheten er albuen i toppen bøyd ca. 130–150°, ikke «foldet ihop». Flere sluttposer (nedtrekk 170°, trx 180°) viser et for sammenfoldet ledd.

## 2. Direkte svar på de tre spørsmålene

### (a) Roing: albuer langs kroppen (45°) eller ut til siden (90°)?

Kort svar: begge er legitime varianter med ulikt mål. For en hobbyutøver på 50 år er standardvarianten med albuer nær kroppen (ca. 30–45° fra overkroppen) riktig utgangspunkt.

| Variant | Albue fra overkropp (frontalplan) | Slutt (sagittalt) | Dominerende muskler | Kilde |
|---|---|---|---|---|
| Lat-roing («albuer i baklomma») | ca. 30–45° | Albue ved eller opptil 20° bak overkroppslinjen | Latissimus, i tillegg til mellomtrapezius/romboideer | ACE seated row, single-arm row. Narrativ review (lavere abduksjon ga mer LD-EMG). |
| Mellomrygg/bakre skulder («high row») | ca. 70–90° (albue i bryst- til skulderhøyde) | Overarm ikke lenger bak enn frontalplanet, maks ca. 20–30° bak | Mellomtrapezius, nedre/øvre trapezius, bakre deltoid | ACE high row, ACE TRX-high-back-row, suspensjons-roing (PMC7734360) |

Hva kildene faktisk sier:

- ACE seated row: albuene glir bakover og holdes nær ribbena til håndtaket er foran magen, ikke flaret ut til siden.
- ACE single-arm row: albuen holdes nær kroppen og overarmen trekkes bakover og opp.
- ACE TRX single-arm row: albuen holdes i brysthøyde og beveger seg mot siden av kroppen; «high-back row»-variant hever albuen til skulderhøyde for å treffe bakre deltoid og øvre rygg.
- Narrativ review (PMC13510307) oppsummerer at lavere skulderabduksjon i roing er koblet til mer latissimus-EMG, mens høyere abduksjon flytter aktiviteten mot trapezius og bakre deltoid. Forfatterne kaller humerus-til-overkropp-posisjon en kandidat til hovedforklaring, men presiserer at dette er en slutning på tvers av studier.
- Suspensjons-roing (PMC7734360, n = 28): «high row» og «horisontal abduksjons-roing» ga over 60 % MVIC i trapezius (alle tre deler) og bakre deltoid. «Low row» nådde bare 40–60 % i mellomtrapezius, lats og bakre deltoid.
- Ledesma-presentasjon (flywheel-roing): sammenlignet 90° skulderabduksjon med maksimal adduksjon og anbefalte adduksjon for lats-vekt. Dette er et konferanse-/lysbildedokument uten full effektstørrelse, svak evidens.

Hvor langt bak torso-linjen kan albuen gå uten å overstrekke skulderen?

- Ingen kilde gir et eksakt tall for roing. Normal aktiv ekstensjon er ca. 45–60° (Healthline).
- Klinisk resonnement (Eric Cressey, trener, ikke fagfellevurdert): smerte fremme i skulderen i sluttposisjon oppstår når overarmen fortsetter i ekstensjon etter at skulderbladet har sluttet å trekkes bakover. Humerushodet skyves da fremover i leddkapselen, og over tid kan fremre slakkhet utvikles.
- ACE single-arm row: gå ikke lenger enn at vekten kan løftes uten å rotere overkroppen.
- Praktisk, konservativ anbefaling (min slutning): albuen skal slutte ved eller høyst ca. 10–20° bak overkroppslinjen, godt innenfor 45–60°-grensen. Stopp bevegelsen når skulderbladet slutter å gå bakover, eller når skulderen ruller fremover.

Hvilken variant passer når:

- Lat-variant (albuer nære): standardvalget. Passer bredest, minst krevende for skulderleddet, god for «generell ryggstyrke».
- Mellomrygg/bakre skulder (albuer ut): bra supplement for øvre rygg og bakre skulder, spesielt hvis du sitter mye foran skjerm. Kjør lettere, kontrollert, uten å gå langt bak frontalplanet. Ved eksisterende skulderproblem: start lett og stopp ved stikkende smerte.
- Uenighet: Lehman 2004 (PMC449729) fant høyest lat- og mellomtrapezius/romboideaktivitet i seated row med protrahert skulderblad (30,1 mot 26,2 % MVC for nedtrekk), men forfatterne konkluderer likevel at retrahert posisjon «synes å gi bedre skulderstabilitet», basert på annen litteratur om skulderbladstilling og ligamentbelastning. Aktiv retraksjon endret ikke lat-EMG signifikant. Dette er en kjent faglig avveining, ikke et avklart svar.

### (b) Nedtrekk og pull-ups: stangen foran eller bak hodet, albuebane, lean, bak nakken?

- Stangen går foran hodet, til øvre bryst/kragebein. ACE seated lat pulldown: stangen ned til øvre eller midtre bryst, albuene rett ned mot gulvet og mot siden av overkroppen.
- Albuebane: ned, ikke bak. ACE: «Stopp når stangen nærmer seg brystet eller når albuene slutter å gå ned og begynner å gå bakover. Ikke trekk lenger, det gir ekstra belastning på skulderleddet.» Rigg-sluttposen bryter dette (albue 20° bak vertikal).
- Fremover i skapulaplanet: kildene gir ikke en tydelig regel. ACE-ekspert (Rubenstein): tenk «albuer mot ribbena og bakover mens brystbeinet løftes mot stangen». Prinold & Bull målte at overarmen i pull-ups avviker opptil 28° (frontgrep) og 42° (reverse grip) fra skulderbladets plan. Min praktiske slutning: albuene beveger seg ned i et plan mellom frontalplanet og skapulaplanet (inntil ca. 30° foran frontalplanet), og ender rett under skulderleddet. Ikke aktivt «frem».
- Lean bakover: ACE sier maks ca. 30° og ikke øk lean under trekket. Teksten i dagbok.html («10–15°») er innenfor og forsvarlig, rigg viser konstant −10°, som er bra. Studie (Buonsenso 2025, referert i PMC13510307): 30° lean økte bakre deltoid men ikke lat-EMG, altså ingen lat-gevinst.
- Bak nakken: ikke anbefalt for deg, men «skadelig» er ikke påvist i en skadestudie.
  - Padovan et al. 2024 (PMC11057623, n = 14): fronten ga høyere 8RM (70,0 mot 59,3 kg), mer lat- og brystaktivitet i nedfasen. Bakre variant ga mer lat i oppfasen. Forfatterne skriver at bakre variant «krever mer glenohumeral bevegelighet for å utføres trygt og effektivt», og at personer med begrenset bevegelighet kan måtte bøye nakken for at stangen skal komme forbi hodet.
  - Samme artikkel nevner tidligere studie som kobler «high-five»-posisjon til mer skulderustabilitet, men at studien kan ha hatt falske positive. Forfatterne foreslår gradvis tilvenning, ikke forbud.
  - Narrativ review (PMC13510307): bekymringen hviler på biomekanikk (ekstrem ekstern rotasjon og abduksjon), ingen EMG-studie målte skade. Fremre variant er «rimelig standardvalg».
  - Vurdering: ingen fordel som oppveier kravet til mobilitet. For en 50-åring med trolig redusert skulder- og brystryggmobilitet er foran-varianten klart å foretrekke. Ordlyden «Aldri bak nakken» i `sikker` bør være «Ikke bak nakken: ingen fordel, krever mer skulderbevegelighet og nakkebøy».

### (c) Face pull: albuehøyde, utover/over hodet, utadrotasjon, «over hodet»-risiko

- Albuehøyde: i skulderhøyde, ikke over. Kildene som beskriver det (trener-/utøverkilder, ikke fagfellevurdert) sier albuer minst i flukt med skuldrene, helst rett over, mens en annen advarer mot å føre albuen høyt og langt bak kroppen fordi det kaster leddet inn i innadrotasjon. ACE «high row» (taukabel i skulderhøyde): albuene trekkes bakover til hendene er foran skuldrene. Ingen kilder gir et tall utover dette.
- Utover: ja. Taugrepet brukes slik at albuene går ut til siden og hendene ender ved hver side av ansiktet. Sett ovenfra betyr det overarmen ca. 80–100° fra rett frem (rundt frontalplanet), maks ca. 20–30° bak frontalplanet. Dette er min praktiske anbefaling, ikke et kildetall.
- Utadrotasjon: underarmene roteres opp og ut slik at hendene havner over albuehøyde («L» eller «målstolpe»-posisjon, Human Kinetics-utdrag «Cuban-style»). Eksternrotasjon er hovedstimuli for infraspinatus/teres minor. Bånd-pull-apart-studien (PMC8975561) fant at håndflate opp (utadrotert grep) ga høyest infraspinatus- og nedre-trapezius-aktivitet, og at håndflate ned (innadrotert) kan gi lavere subakromialt rom og er forbundet med mer impingement-risiko. Face pull bør derfor gjøres med tommel bak/utover, ikke innadrotert.
- «Over hodet»: risikoen er høyere når albuene løftes over skulderhøyde i kombinasjon med innadrotasjon og tung last. Prinold & Bull: høy armelevasjon reduserer subakromialt rom og øker trykket. Kabelen skal være i øye- til skulderhøyde, ikke over pannen. Albuer høyt (skulderhøyde) med utadrotasjon er den beskyttede posisjonen. Albuer langt over skulderen med hendene ned og innadrotert er den uheldige.
- Uenighet/mangel: ingen EMG-studie av selve face pull funnet. Reinold-type studier (rapportert via sekundærkilder) viser høy bakre-deltoid- og infraspinatusaktivitet i prone horisontal abduksjon ved ca. 100° med full utadrotasjon, men det er ikke face pull.

## 3. Øvelsene enkeltvis

### 3.1 Enarms manualroing (`manualroing`)

Verdict: OK. Legg til presisering av albuebane og stoppkriterium.

Kilder:
- ACE Single Arm Row: https://www.acefitness.org/resources/everyone/exercise-library/126/single-arm-row/ — hånd under skulder, kne under hofte, skulderblad ned og bakover og holdt, albuen nær kroppen og overarmen trekkes bakover til vekten ikke kan gå høyere uten overkroppsrotasjon.
- Narrativ review lat-EMG: https://pmc.ncbi.nlm.nih.gov/articles/PMC13510307/ — lavere abduksjon favoriserer lats, høyere trapezius/bakre deltoid. Benkstøttet roing ga lavere erektor-EMG enn stående, men ikke signifikant.
- Sekundært: ACE «Dynamite Delts» https://www.acefitness.org/continuing-education/prosource/september-2014/4972/dynamite-delts-ace-research-identifies-top-shoulder-exercises/ — for bakre deltoid i hellende roing holdes overarmene vinkelrett på kroppen. Dette er altså «albuer ut»-varianten, ikke lat-varianten.

Rettelser (tekst):
- ut[0]: behold «albuen opp og bakover mot hoften». Legg til «albuen holdes nær kroppen, ca. 30–45° fra siden».
- ut[2]: «Senk til strak arm, la skulderbladet få følge litt frem nederst, trekk så skulderblad ned og bak før albuen». (ACE: ikke forhånds-trekk skulderbladet for tidlig, ekspertene er uenige om timing, se punkt 7.)
- feil: legg til «albuen går langt bak ryggen og skulderen ruller frem».
- sikker: «Stopp trekket når overkroppen vil rotere. Stopp ved stikkende smerte i skulder eller korsrygg.»

RIG (sagitt): geometrien er riktig. Start: overarm lodd (S 70° fleksjon relativt til en nesten horisontal rygg), slutt: overarm parallell med overkroppen (S ≈ +5°). Albuefleksjon 65° med underarm vertikal er naturlig (manualen henger). Anbefalt: S i slutt 0 til −15° (ua 250–265). Nåværende 245 er i orden. Ryggen er 20° over horisontalen, ok. Hode i flukt med ryggen (`nk` = `to`), korrekt.

Skaderisiko og stopp: skulder fremme (albue bak kroppen), korsrygg (hyperekstensjon eller rotasjon), nakke (hodet løftes). I brukerundersøkelsen PMC10821116 (1387 mosjonister) hadde enarms manualroing 24 smerterapporter blant 440 som utfører den (ca. 5 %), lavere enn de fleste andre øvelsene. Dette er deskriptivt og uten skadebegrep.

### 3.2 Sittende kabelroing (`kabelroing`)

Verdict: MÅ ENDRES (animasjon og tekst).

Kilder:
- ACE Seated Row: https://www.acefitness.org/resources/everyone/exercise-library/48/seated-row/ — albuene glir bakover nær ribbena til håndtaket er foran magen, ryggen rett, brystet løftet. Ikke flaret ut.
- Padovan 2025 seated row (PMC12821611): https://pmc.ncbi.nlm.nih.gov/articles/PMC12821611/ — sammenligner fast retrahert mot fri skulderbladsposisjon. Fast skulderblad ga mer lat (eksentrisk), mellomtrapezius og bakre deltoid. Trunk ble holdt stabilt.
- Lehman 2004: https://pmc.ncbi.nlm.nih.gov/articles/PMC449729/ — seated row med protrahert skulderblad ga høyest lat/mellomtrapezius-aktivitet, forfatterne mener retrahert er mer stabil for skulderen. Ingen signifikant forskjell med aktiv retraksjon.
- ACE-artikkel om skulderbladscues: https://www.acefitness.org/certifiednewsarticle/2384/correct-cues-for-scapular-motion/ — «bak og ned», men unngå å trekke skulderbladene sammen før armen beveger seg. Kaselj: ikke slapp av/trekk opp skuldrene.

Rettelser:
- opp[2]: «Armene strake. Skuldrene kan få gli litt frem uten å runde ryggen.» Teksten er ok.
- ut[0]: ok («mot navlen, albuer bakover langs kroppen»). Legg til «albuer nær ribbena, ikke ut til siden».
- ut[1]: «Klem skulderbladene lett sammen» er ok, men legg til «trekk først med albuene, ikke ‘klem før du drar’».
- sikker: erstatt «Ikke lene deg bakover over loddlinjen» med «Hold overkroppen oppreist og stille gjennom hele settet, ikke slå deg bakover for å få vekten opp».
- Legg inn variantvalg: «Ønsker du mer mellomrygg/bakre skulder: bruk bredere håndtak og la albuene gå ut til skulderhøyde (lettere vekt), men ikke bak ryggen» (se 2a).

RIG (nåværende → anbefalt):

| | Nå | Anbefalt |
|---|---|---|
| Overkropp start/slutt | +10° → −5° (svinger 15°, passerer lodd) | +5° begge (maks ±3° variasjon) |
| Overarm start | ua 80, S 110° fleksjon | ua 90–100 (S ≈ 90–95°): arm horisontal eller litt under |
| Overarm slutt | ua 200, S −25° | ua 200 med to = +5 gir S ≈ −15°. Holdes ≤ −20°. |
| Albuefleksjon slutt | 120° | 110–125° (håndtaket foran magen), ok |

Skaderisiko og stopp: korsrygg (rygg rundes ved start, eller hyperekstensjon i slutt), skulder (albuen langt bak overkroppen, skulder ruller frem), nakke (skuldre mot ørene). Stopp ved stikkende smerte i fremre skulder eller korsrygg.

### 3.3 Nedtrekk (`nedtrekk`) og strikknedtrekk (`strikknedtrekk`)

Verdict: begge MÅ ENDRES (samme rigg).

Kilder:
- ACE Seated Lat Pulldown: https://www.acefitness.org/resources/everyone/exercise-library/158/seated-lat-pulldown/ — skulderblad ned og bakover, lean maks ca. 30° og ikke øk, hode i flukt med ryggraden, albuer rett ned mot gulvet og mot siden, stopp når albuene slutter å gå ned og begynner å gå bakover.
- Padovan 2024 front mot bak: https://pmc.ncbi.nlm.nih.gov/articles/PMC11057623/ — se (b).
- Pulldown grep- og underarmsorientering (PMC12452428): https://pmc.ncbi.nlm.nih.gov/articles/PMC12452428/ — 40 menn, sju varianter, ingen signifikante lat-forskjeller mellom grep. Bakre deltoid høyere med 30° lean og vid pronert grep. Forfatterne nevner at innadrotasjon i den varianten kan svekke skulderbladstabiliteten.
- ACE-artikkel skulderblad: https://www.acefitness.org/certifiednewsarticle/2384/correct-cues-for-scapular-motion/ — uenighet om hva skulderbladene bør gjøre i toppen og om cuing «stang til bryst».

Rettelser (tekst):
- opp[2]: ok (10–15°). Legg til «ikke øk lean under trekket».
- ut[0]: «Start med å trekke skuldrene ned og bak» er litt for bestemt. ACE-eksperter (Rubenstein, Kaselj) advarer mot sterk retraksjon/depresjon før armen beveger seg. Foreslått: «Sett skuldrene ned (ikke i ørene), trekk så albuene ned mot sidene».
- ut[1]: «ned mot øvre bryst, ikke bak hodet». Legg til: «stopp når albuene er ved ribbena, ikke la dem gå bak kroppen».
- feil: legg til «albuene går bak kroppen og brystet skyves frem».
- sikker: «Ikke bak nakken: ingen fordel og krever mer skulderbevegelighet og nakkebøy. Stopp ved stikkende skulder- eller albuesmerte.»
- strikknedtrekk: `opp[1]` sier «sitter eller står på kne», men figuren sitter på benk. Enten tegne knestående eller rette teksten til «sitter». Legg til: «Strikken festes loddrett over hodet (slik at trekkretningen blir nedover) og slippes sakte opp. La den aldri smelle tilbake.»

RIG (nåværende → anbefalt):

| | Nå | Anbefalt |
|---|---|---|
| Overkropp | −10° begge | −10 til −15°, konstant (ok) |
| Start: overarm | ua 5, fa 5 (S 165° fleksjon) | ua 5–15, fa 5–15 (bar foran ansikt, armer 5–15° foran lodd) |
| Slutt: overarm | ua 200 (20° bak lodd, S −30°) | ua 170–180 (vertikal eller litt foran), S ≈ 0 til −10° |
| Slutt: underarm | fa 30 | fa 35–45 (hendene ca. 8–12 cm under skulder, 15 cm foran) |
| Slutt: albuefleksjon | 170° | ca. 130–140° |
| Hode | `nk` = `to` (flukt) | behold, hakeretrasjon er ikke nødvendig |

Hva mangler i sidebildet: at albuene i frontalplanet ender ca. 30–45° fra siden ved bred grep. Kan ikke vises uten frontvisning.

Skaderisiko og stopp: fremre skulder (albuer bak overkropp, stang trekkes ned bak hodet), nakke (stang bak, hodet skyves frem), albuer (tung last i bred grep: ACE nevner jukse/kipping i pull-ups; i pulldown tilsvarer det kroppsvekt-sving). Stopp ved stikkende skulder- eller albuesmerte. Pulldown er maskinøvelse; i PMC10821116 var maskin-/kabelbaserte øvelser forbundet med mindre smerte enn frivekt og kroppsvekt (maskiner 11,5 % mot frivekt 19,9 %), men de tre øvelsene ble ikke analysert enkeltvis.

### 3.4 Pull-ups (`pullups`)

Verdict: MÅ ENDRES (albuen bak overkroppen, grepsbredde, nyanser i skulderblad-cue).

Kilder:
- ACE Pull-ups: https://www.acefitness.org/resources/everyone/exercise-library/191/pull-ups/ — full grep, tommel rundt, skulderblad ned og bak og holdt, kryss ben, hode i flukt med overkroppen, albuene ned mot gulvet nær siden, omtrent i linje med overkroppen, kroppen vertikal, ingen sving.
- Prinold & Bull 2016: https://pmc.ncbi.nlm.nih.gov/articles/PMC4916995/ — 11 trente menn, tre grep. Bred grep: skulderbladet beveget seg bare 10° i pro-/retraksjon mot 22° med skulderbredde, og overarmen nådde 90° abduksjon og 45° utadrotasjon. Reverse grep: ekstrem utadrotasjon ved start og opptil 42° avvik fra skulderbladsplanet. Forfatterne slutter at disse mønstrene kan øke impingement-risiko og foreslår assistert frontgrep som mulig lavrisikovalg. Skade ikke målt.
- Narrativ review: https://pmc.ncbi.nlm.nih.gov/articles/PMC13510307/ — lat-EMG er omtrent lik mellom grep. Grep endrer mest biceps, pectoralis major og nedre trapezius.
- ACE «A back-to-school program»: https://www.acefitness.org/resources/pros/expert-articles/8944/a-back-to-school-program-an-evidence-based-approach-to-training-the-back/ — pull-ups/chin-ups er best for lats og infraspinatus, svakest for mellom-/nedre trapezius.

Rettelser (tekst):
- opp[0]: «litt bredere enn skuldrene» bør bli «skulderbredde, evt. marginalt bredere. Unngå vid grep (på den skrå delen av stangen)». Støttet av Prinold & Bull og Padovan (ekstreme posisjoner med vid grep).
- ut[0]: «Start med å dra skuldrene ned, deretter albuene» er ACE-konform. Legg til «uten å låse skulderbladene fast (de skal få bevege seg fritt)», jf. ACE-ekspertene.
- ut[1]: «Før haken over stangen» er greit, men «uten å strekke nakken» bør presiseres: «hodet i flukt med overkroppen (ACE), ikke stikk haken frem eller bak».
- sikker: legg til «Unngå helt passivt hengende ‘dead hang’ ved skulderproblemer. Slipp ikke ned ukontrollert i bunn, albuene tåler det dårlig.»
- tips: assistanse er riktig valg for deg (50 år) til 6–8 rene reps.

RIG (nåværende → anbefalt):

| | Nå | Anbefalt |
|---|---|---|
| Start | ua 0, fa 0, to 0 (S 180°) | ok. Evt. vis lett skulder ned (skulder ca. 1–2 cm lavere) |
| Slutt: overarm | ua 195 (15° bak lodd, S −23° bak overkropp) | ua 175–180 (albuer ved siden av overkroppen, S ≈ 0 til −10°) |
| Slutt: underarm | fa 15 | fa 10–15 (håndledd over albue, stang litt foran skulder) |
| Slutt: overkropp | −8° | −5° |
| Hode | `nk` = `to` | `nk` ca. 0 til +10 for at haken kommer foran stangen uten nakkestrekk |
| Knær | sn 90 (90° knebøy bak) | sn 70–80, «lett bøyde knær» som teksten sier |

Skaderisiko og stopp: impingement/skulder (vid eller reverse grep, albuen bak overkropp, kipping), albuer (tendinopati ved høyt volum og ukontrollert nedsenking), nakke (haken stikkes frem). Stopp ved stikkende smerte i skulder eller albue.

### 3.5 TRX-/strikkroing liggende (`trx`)

Verdict: MÅ ENDRES. Den verste feilen i denne gruppen.

Kilder:
- ACE TRX Single-arm Row: https://www.acefitness.org/resources/everyone/exercise-library/92/trx-reg-single-arm-row/ — albuen holdes i brysthøyde og beveges mot siden av kroppen, ikke la skulderen rulle frem, ikke sag i korsrygg/hofter, ikke rotere. High-back-variant hever albuen til skulderhøyde for bakre deltoid og øvre rygg. ACE klassifiserer enarms som avansert.
- Suspensjons-roing (PMC7734360): https://pmc.ncbi.nlm.nih.gov/articles/PMC7734360/ — high row og horisontal abduksjons-roing >60 % MVIC i trapezius og bakre deltoid. Foreslås å kunne passe ved skulderbladsdysfunksjon eller subakromial impingement. Armposisjon ikke gjengitt i det jeg fikk lese.
- Snarr & Esco 2013: https://www.asep.org/asep/asep/JEPonlineDecember2013_Snarr_Esco.pdf — suspensjon mot Smith-maskin ga ikke signifikant forskjell i lat, mellomtrapezius, bakre deltoid. Biceps lavere med suspensjon. (Kun sett via søkeresultatets sammendrag.)
- Narrativ review: https://pmc.ncbi.nlm.nih.gov/articles/PMC13510307/ — inverted row hadde høyest lat/øvre rygg og lavest estimert korsryggbelastning i Fenwick 2009 (n = 7, må replikeres).

Rettelser (tekst):
- ut[0]: «Trekk albuene bakover og brystet mot håndtakene» er ok. Legg til «albuene nær kroppen ved lat-fokus, eller ut til skulderhøyde med lett belastning for bakre skulder (ikke lenger bak enn kroppslinjen)».
- feil: legg til «albuene går langt bak ryggen og skulderen ruller frem».
- opp: legg til at kroppen er rett fra ankel til skulder, «sag i korsrygg = stopp».
- sikker: ok. Legg til «Vær sikker på at festet tåler kroppsvekten».

RIG (nåværende → anbefalt):

| | Nå | Anbefalt |
|---|---|---|
| Start: kropp | −50° (40° over horisontalt) | ok |
| Start: arm | ua 55, fa 55 (strake, i linje med stropp) | ok |
| Slutt: kropp | −35° | −35°, ok |
| Slutt: overarm | ua −110 (S −105°, albuen 20 enheter bak skulder) | ua ca. 160 (S ≈ −15°, albue ved/litt bak overkroppen) |
| Slutt: underarm | fa 70 (albuefleksjon 180°) | fa 10–20 (hendene ved bryst/nedre ribbein), fleksjon 130–150° |

Følger man anbefalt tabell ender håndleddet ca. 12 enheter foran skulderleddet og 3 under, altså håndtak ved brystet. Strikk/stropp-linjen vil da gå ca. 50° fra loddrett mot festet. Det er realistisk.

Skaderisiko og stopp: fremre skulder (albue bak overkropp), korsrygg (sag), nakke (hode foran). Stopp ved stikkende smerte i skulder eller korsrygg. ACE advarer mot å prøve enarmsvarianten før korsryggen kan stabiliseres av kjernen.

### 3.6 Face pull (`facepull`)

Verdict: MÅ ENDRES (kabelhøyde, sluttposisjon og manglende utadrotasjonsvisning).

Kilder:
- ACE High Row: https://www.acefitness.org/resources/everyone/exercise-library/336/high-row/ — kabel i skulderhøyde med tau, albuene trekkes bakover til hendene er foran skuldrene, ingen sikkerhetsmerknader.
- Bånd pull-apart (PMC8975561): https://pmc.ncbi.nlm.nih.gov/articles/PMC8975561/ — 10 menn. Håndflate opp (utadrotert) ga høyest infraspinatus og nedre trapezius, håndflate ned høyest bakre deltoid og øvre trapezius. Forfatterne advarer om at håndflate ned med diagonal opp-bevegelse kan gi glenohumeral innadrotasjon forbundet med redusert subakromialt rom.
- Human Kinetics-utdrag (Chad Landers): https://us.humankinetics.com/blogs/excerpt/cuban-style-face-pull — når albuene er i skulderhøyde roteres armene utover til en L-form mens skulderbladene klemmes sammen. Forfatterens påstand om skuldrehelse er uten kilder.
- PMC12110944 (Healthcare 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12110944/ — tester skulderbladsretraksjon ved 90° og 45° abduksjon, ikke face pull. Brukes kun som bakgrunn: mellom- og nedre trapezius aktiveres i begge posisjoner.
- Trenerkilder (ikke fagfellevurdert, fra søkesammendrag): kabel i øye- til pannehøyde, albuene minst i skulderhøyde, tommel bakover for utadrotasjon, la ikke albuene falle ned eller gå langt bak. Kvalitet: lav.

Rettelser (tekst):
- opp[0]: «øyehøyde» er greit (øye- til skulderhøyde). Rigg bør matche.
- ut[0]: «albuene høyt og utover» → «albuene i skulderhøyde og ut til siden, ikke over skulderen».
- ut[1]: «drei underarmene lett ut» → «roter underarmene opp og ut slik at hendene ender over albuenivå, tommel mot ørene».
- feil: legg til «albuene løftes over skulderen og skuldrene trekkes mot ørene (øvre trapezius)» og «tung vekt gir innadrotasjon».
- sikker: ok. Legg til «ikke over hodehøyde».

RIG (nåværende → anbefalt):

| | Nå | Anbefalt |
|---|---|---|
| Kabel | (168, 56), brysthøyde (ca. 22 enheter under skulder) | y ≈ 25–34, øye- til skulderhøyde |
| Start | ua 90, fa 90 (arm horisontal, S 85°) | ok |
| Slutt: overarm | ua 260 (nesten horisontalt bak kroppen, S −85°) | kan ikke vises i sidebilde, se under |
| Slutt: underarm | fa 70 | se under |
| Overkropp | −5° | 0 til −5° |

Problemet: i sidebildet vil en overarm som peker ut til siden ved skulderhøyde bli vist som en prikk/kort stripe (foreshortening). Rigget har fast segmentlengde og viser derfor en arm som peker rett bakover, noe som ligner ekstrem skulderekstensjon (85° mot normalt 45–60°). Reelt står overarmen nær frontalplanet (hori­sontal abduksjon ca. 80–110° fra rett frem). Anbefaling: bytt til topp- eller frontvisning (rigget har allerede `view:'top'` og `view:'front'`), eller legg til en foreshortening-parameter for overarmen.

Skaderisiko og stopp: skulder (albuene over skulderhøyde med innadrotasjon, tung vekt), nakke (haken skyves frem, skuldre trekkes opp). Stopp ved stikkende skuldersmerte. Hold vekten lett (12–15 reps, som teksten sier).

### 3.7 Biceps curl (`biceps`)

Verdict: OK.

Kilder:
- ACE Bicep Curl: https://www.acefitness.org/resources/everyone/exercise-library/70/bicep-curl/ — albuene nær midten av kroppen, bryst stille slik at bare armene beveger seg, skuldre i linje med håndledd og albuer, senk sakte.
- Distal bicepssene-ruptur, videoanalyse (PMC9214967): https://pmc.ncbi.nlm.nih.gov/articles/PMC9214967/ — 56 klipp: 96 % supinert underarm, 71 % med helt strak albue, 82 % isometrisk. Markløft sto for 71 % og biceps curl for 10,7 %.
- Brukerundersøkelsen PMC10821116: https://pmc.ncbi.nlm.nih.gov/articles/PMC10821116/ — biceps curl med manual: 101 smerterapporter blant 495 (ca. 20 %), blant de mer smerteutsatte armøvelsene. Skuldre mest rammet region (1114 tilfeller), deretter korsrygg og albue (463). Ikke brutt ned per øvelse.

Rettelser (tekst):
- ut: legg til «senk til nesten strak arm, men ikke smekk albuen i». 
- feil: legg til «albuene driver bak kroppen i bunn».
- sikker: «Stopp ved smerte i albuen eller i innsiden av albuen (distal bicepssene). Ikke heng ned i strak arm under tung last eller rykk opp fra bunn.»

RIG: geometrien stemmer. Overkropp 0°, overarm 5–10° foran lodd (albue stille), albuefleksjon 5° → 155°. Små justeringer valgfrie: start ua 180 (S 0) og slutt ua 170 er fint. Supinasjon kan ikke vises i sideriggen.

Skaderisiko og stopp: distal bicepssene (strak arm + supinert + tung last, særlig menn som løfter), albuer (volum), korsrygg (sving). Disse rupturstudiene er observasjonelle og små, så de viser mønster, ikke årsak.

## 4. Animasjonsspesifikasjon (til slutt)

Vinkler: «overarm mot overkropp» (S): + foran, − bak overkroppslinjen. Rig-vinkler ved siden av. Alle angitt som verdensvinkler for sidegeometri.

| Øvelse | Overkropp (to) | Overarm start | Overarm slutt | Albuefleksjon slutt | Hode/nakke | Merknad |
|---|---|---|---|---|---|---|
| manualroing | 70° konstant | ua 180 (S 70°) | ua 250–265 (S 0 til −15°) | 65–90° | `nk` = `to`, blikk ned/litt frem | Albue 30–45° fra siden (frontalt). |
| kabelroing | +5° konstant (±3°) | ua 90–100 | ua 200 (S ≈ −15°) | 110–125° | `nk` = `to` | Hendene foran navle/mage. Ikke lene bak lodd. |
| nedtrekk | −10 til −15° konstant | ua 5–15, fa 5–15 | ua 170–180, fa 35–45 (S 0 til −10°) | 130–140° | `nk` = `to` | Albuer ned, aldri bak kroppen. Stang til øvre bryst, foran hodet. |
| strikknedtrekk | −10° konstant | som nedtrekk | som nedtrekk | 130–140° | `nk` = `to` | Rett teksten (sitter) eller tegn knestående. |
| pullups | 0° → −5° | ua 0, fa 0 | ua 175–180, fa 10–15 (S 0 til −10°) | ca. 130–150° | `nk` 0 til +10 (hake over stang uten nakkestrekk) | Skulderbredde grep, knær lett bøyd (sn 70–80). |
| trx | −50° → −35° | ua 55, fa 55 (strake, i linje med stropp) | ua ca. 160, fa 10–20 (S ≈ −15°) | 130–150° | `nk` = `to` | Fiks pose 1: nå S −105°, fleksjon 180°. |
| facepull | 0 til −5° | ua 90, fa 90, kabel y ≈ 25–34 | sideriss kan ikke vise albue ut. Bruk topp-/frontvisning: overarm 80–100° fra rett frem (≤ 20–30° bak frontalplan), albuer i skulderhøyde, ER 60–90° | 90–120° | `nk` = `to`, haken inn | Nå 85° ekstensjon og kabel i brysthøyde. |
| biceps | 0° konstant | ua 175–180 (S 0–5°) | ua 170–175 | 140–155° | `nk` = `to` | OK. Albue stille ved siden av kroppen. |

Frontalplan-info (som sideriggen ikke viser):

| Øvelse | Albue fra overkropp (abduksjon) |
|---|---|
| manualroing | 30–45° |
| kabelroing (lat) | 30–45° |
| kabelroing (bakre skulder, valgfri variant) | 70–90°, lettere vekt |
| nedtrekk, pull-ups | ca. 30–45° ved bredde ca. 1–1,3 × skulderbredde (albue ender under skulder) |
| trx | 30–45° (lat) eller 70–90° (high row) |
| facepull | 80–100° (skulderhøyde), ER 60–90° |
| biceps | 0–15° |

## 5. Hvor kildene er uenige eller svake

1. Skulderblad før arm (ACE-ekspertpanelet): Price beskriver at skulderblad naturlig elevere og roterer utover ved armen opp i pulldown. Rubenstein og Kaselj advarer mot å trekke skulderbladene bak/ned før armen beveger seg. Praktisk: «sett skulder ned, men la bladene bevege seg fritt».
2. Retrahert mot protrahert skulderblad i roing: Lehman 2004 viste høyest aktivitet i protrahert variant men anbefalte retrahert for stabilitet. Padovan 2026: fast skulderblad ga mer lat eksentrisk. Ikke avklart.
3. Front mot bak nedtrekk: EMG-forskjeller går begge veier. Skadedata mangler (PMC13510307).
4. Albuevinkel 45° mot 90° i roing: ingen direkte hode-til-hode studie av albuevinkel alene. Informasjonen er indirekte fra abduksjonsstudier.
5. Face pull: ingen direkte EMG funnet. Albuehøyde og utadrotasjon støttes av ACE high row, bånd pull-apart-studien og trenerkilder.
6. Grepsbredde i pull-ups: Prinold & Bull er liten (n = 11), kinematikk uten skadedata. Narrativ review fant at grepsbredde ikke endrer lat-EMG konsistent.
7. Fenwick 2009 (roing, korsrygg): kun sett via PMC13510307. Ikke lest i original.

## 6. Kildeliste

Åpne/primære (lest i fulltekst via Europe PMC eller direkte):

- ACE Seated Lat Pulldown: https://www.acefitness.org/resources/everyone/exercise-library/158/seated-lat-pulldown/
- ACE Correct Cues for Scapular Motion: https://www.acefitness.org/certifiednewsarticle/2384/correct-cues-for-scapular-motion/
- ACE Seated Row: https://www.acefitness.org/resources/everyone/exercise-library/48/seated-row/
- ACE Single Arm Row: https://www.acefitness.org/resources/everyone/exercise-library/126/single-arm-row/
- ACE Pull-ups: https://www.acefitness.org/resources/everyone/exercise-library/191/pull-ups/
- ACE Bicep Curl: https://www.acefitness.org/resources/everyone/exercise-library/70/bicep-curl/
- ACE High Row: https://www.acefitness.org/resources/everyone/exercise-library/336/high-row/
- ACE TRX Single-arm Row: https://www.acefitness.org/resources/everyone/exercise-library/92/trx-reg-single-arm-row/
- ACE «A Back-to-School Program»: https://www.acefitness.org/resources/pros/expert-articles/8944/a-back-to-school-program-an-evidence-based-approach-to-training-the-back/
- ACE «Dynamite Delts»: https://www.acefitness.org/continuing-education/prosource/september-2014/4972/dynamite-delts-ace-research-identifies-top-shoulder-exercises/
- Lehman m.fl. 2004, muskelaktivering i lat-øvelser (PMC449729): https://pmc.ncbi.nlm.nih.gov/articles/PMC449729/
- Padovan m.fl. 2024, front mot bak lat pull-down, HD-EMG (PMC11057623): https://pmc.ncbi.nlm.nih.gov/articles/PMC11057623/
- Padovan m.fl. 2025, seated row skulderbladsposisjoner (PMC12821611): https://pmc.ncbi.nlm.nih.gov/articles/PMC12821611/
- Buonsenso m.fl. 2025, pulldown grep/underarm (PMC12452428): https://pmc.ncbi.nlm.nih.gov/articles/PMC12452428/
- Narrativ review, lat-EMG i styrkeøvelser (PMC13510307): https://pmc.ncbi.nlm.nih.gov/articles/PMC13510307/
- Prinold & Bull 2016, pull-up skulderbladskinematikk (PMC4916995): https://pmc.ncbi.nlm.nih.gov/articles/PMC4916995/
- Suspensjons-roing, EMG (PMC7734360): https://pmc.ncbi.nlm.nih.gov/articles/PMC7734360/ (kun sammendrag lest)
- Bånd pull-apart, håndposisjon og retning (PMC8975561): https://pmc.ncbi.nlm.nih.gov/articles/PMC8975561/
- Skulderbladsretraksjon ved 90° og 45° (PMC12110944): https://pmc.ncbi.nlm.nih.gov/articles/PMC12110944/
- Skulderblad-retraksjon, nedre trapezius (PMC10324291): https://pmc.ncbi.nlm.nih.gov/articles/PMC10324291/
- Distal bicepssene-ruptur, videoanalyse (PMC9214967): https://pmc.ncbi.nlm.nih.gov/articles/PMC9214967/
- Brukerundersøkelse, smerteutsatte øvelser (PMC10821116): https://pmc.ncbi.nlm.nih.gov/articles/PMC10821116/

Svakere/ikke-fagfellevurdert (merket i teksten):

- Eric Cressey, smerte i sluttposisjon i roing: https://ericcressey.com/troubleshoot-end-range-shoulder-pain/
- Healthline, normal skulderbevegelighet (ekstensjon 45–60°): https://www.healthline.com/health/shoulder-range-of-motion
- Human Kinetics (Chad Landers), Cuban-style face pull: https://us.humankinetics.com/blogs/excerpt/cuban-style-face-pull
- Snarr & Esco 2013 (suspensjons-inverted row): https://www.asep.org/asep/asep/JEPonlineDecember2013_Snarr_Esco.pdf (kun sammendrag via søk)
- Trenerkilder for face pull (søkesammendrag, ikke åpnet): powerliftingtechnique.com/face-pulls, majorfitness.com «how to do the face pull»

Ikke tilgjengelig for meg: NCBI Bookshelf/StatPearls (bot-sjekk), Physiopedia (403), powerliftingtechnique.com (403).
