# Kvalitetssikring: hofte- og kjerneøvelser (teknikktekst og animasjonsgeometri)

Gjelder `dagbok.html` (objektene LIB og RIG), øvelsene rdl, enbensrdl, hipthrust, enbenship, plank, baertur, deadbug, pallof. Filen er kun lest, ikke endret.

Målgruppe: mann 50 år, hobbyutøver, halvmaraton. Ledd- og skaderrisiko (korsrygg, hofter, skuldre, nakke) er vektlagt.

## Hvordan dette er gjort, og hvor sikkert det er

- Kildene er hentet og lest i denne økten (se kildelisten, K1 til K22). Noe er lest i fulltekst (via Europe PMC), noe er bare sett som søkeresultat-utdrag. Det står markert der det gjelder.
- Physiopedia (RDL og Deadlift Exercise), NSCA-artikkelen og McGill-sitatene om plank ga 403 eller var bare tilgjengelige som søkeutdrag. De er derfor merket «sekundær (kun utdrag)».
- Flere pmc.ncbi.nlm.nih.gov-sider ga captcha ved direkte henting. Samme artikler ble lest via Europe PMC sin fulltekst-API.
- Det finnes lite kontrollert forskning på selve «riktig teknikk» for disse øvelsene. De fleste tekniske detaljer (dybde, vinkler, armvinkel) hviler på coaching-kilder (ACE, Harvard, Physiopedia) og én smal biomekanikkstudie for hip thrust. Der jeg regner ut vinkler fra RIG-geometrien er det merket «regnet ut».
- Ingen kilde oppgir tall for armvinkel i RDL, bekkentilt i grader, eller «riktig» knevinkel i toppen av hip thrust. Slike tall under er min tolkning av geometri og kildenes tekst, ikke målte verdier.

### Slik er RIG regnet
Segmentlengder: legg 28, lår 30, overkropp 40, nakke 14, overarm 22, underarm 20 (SEG-objektet). Vinkelkonvensjon som oppgitt (0 = opp, 90 = frem, 180 = ned). Alle koordinater under er regnet fra `solve()` med ankel/hofte/skulder som ankerpunkt. Koordinatene brukes bare til å sammenligne poser. Én enhet er omtrent 1,5 cm. Hoftefleksjon (grader) = overkroppens vinkel minus lårets «opp-retning» (th). Knefleksjon = sn minus th.

Et strukturelt funn som gjelder flere øvelser: overkroppen (40) er lang i forhold til lår (30) og legg (28). Menneskets hofte-til-skulder er ca. 1,15 ganger lårlengden, ikke 1,33. Derfor må armene vinkles mye bakover for å holde stangen/manualen nær beina. Det er en modellbegrensning, ikke en teknisk feil i selve posene.

---

## 1. rdl (rumensk markløft, stang eller manualer)

**Verdict: OK med mindre endringer i teksten og tre justeringer i animasjonen. Animasjonen er ikke farlig feil.**

### Hva kildene sier
- ACE «Do it Better» og «Technique Series» (K1, K2, lest): lett og konstant knebøyning (ikke bøy mer som i en knebøy, ikke strekk knærne under senkingen). Senk til du kjenner stramming i baksiden av lårene, «vanligvis ca. knehøyde; mer bevegelige kan gå til midt på leggen». Slutt-dybden settes av hamstring-fleksibilitet, ikke av en fast avstand. Stangen i kontakt med kroppen hele veien; jo lenger fra kroppen, desto mer belastning på korsryggen. Se ned mot gulvet (speil strammer nakken). Start fra stativ i lår-/midjehøyde, ikke fra gulvet. Rette ben-varianten er for erfarne.
- ACE-biblioteket (K3, lest): bryst opp, lett bøyde knær, stang mot lårene, stopp når du kjenner strekk bak lårene, stang tett inntil kroppen opp og ned.
- Physiopedia (K4, kun søkeutdrag): stangen går ned «under kneleddet, eller til punktet der du kjenner behov for å bøye ryggen/knærne mer». Knefleksjon ca. 15 grader. Stangen «nær beina i stedet for rett under skuldrene, som reduserer dreiemomentet på korsryggen». Deadlift Exercise-siden (kun utdrag) sier «under knærne eller midt på leggen hvis formen tillater det».
- Biomekanikkartikkel om RDL (K5, lest): RDL utføres med lett bøyd kne, rett spinal, skuldre bak og ned, hofteavstand. Ingen vinkler oppgitt.
- Narrativ oversikt om markløft og nøytral rygg (K6, lest): trente løftere viser ofte naturlig litt lumbal fleksjon uten klar evidens for skade. Forfatterne omdefinerer «nøytral» til «kontrollert og stabil», ikke stiv. Overdreven fleksjon under tung last og i utmattet tilstand kan likevel være en risikofaktor. Lastprogresjon (rask økning) er sterkere skadeprediktor enn tekniske avvik.

### (a) Dybde, knevinkel, armer vs. stang

**Hvor dypt?** Til hamstringstrekk, og stopp ved første tegn på at bekkenet slutter å rotere og ryggen vil runde. For de fleste er det omtrent knehøyde (K1, K2). Midt på leggen er forbeholdt de som kan det uten at ryggen endrer seg. Teksten i LIB sier «til de passerer knærne, ... (ofte midt på leggen)». Det er for ambisiøst for en 50-åring og strider mot ACE. Anbefalt: «ned til omtrent knehøyde (litt under kneet hvis du er bevegelig)».

**Hva bestemmer endepunktet?** Ikke stangen i seg selv, men hamstringtrekk og at korsryggen fortsatt står uendret (K1, K2, K4). Regnet ut: stangsentrum i RIG-pose 1 ender ca. 12 enheter (ca. 18 cm) over kneleddet. Det er en nedre-lår-posisjon, altså grunnere enn teksten. Animasjonen er med andre ord konservativ og går dermed godt, men bryter med teksten som sier «midt på leggen».

**Knevinkel.** Kildene sier «lett og konstant» (K1, K2); Physiopedia nevner ca. 15 grader. Teksten sier 10 til 15. RIG-pose 0 har 0 graders knefleksjon (rette ben), pose 1 har 26 grader. Det betyr at animasjonen viser en synlig kneøkning på 26 grader mens teksten sier «de holder seg slik hele tiden». Det er den tydeligste feilen.

**Armer «hengende vertikalt» eller «stang tett på kroppen»?** Ingen av kildene sier at armene må henge vertikalt. Alle sier at stangen skal være tett på kroppen (K1, K2, K3, K4). Physiopedia sier eksplisitt at stangen skal gå tett langs beina «i stedet for rett under skuldrene», fordi det reduserer momentet på korsryggen. Når overkroppen heller fremover ligger skuldrene foran stangen, og armene peker derfor litt bakover/nedover mot lårene. Tett på kroppen vinner over vertikale armer. RIG-poses armer (ua/fa 218, dvs. 38 grader bakover fra vertikalt) går riktig retning. Størrelsen er trolig i øvre kant. Det skyldes den lange overkroppen i modellen (se over), ikke at poseringen er galt. Ingen kilde oppgir en armvinkel. Jeg anslår 15 til 30 grader som realistisk.

Stangen går i tillegg noe fremover rundt kneet (knehodet og leggen er ikke på samme linje som låret). Det er min tolkning, ikke en kildeopplysning, men bør vises: stangen skal ikke «snike seg inn» i kneet.

### Rettelser

LIB-tekst (rdl):
- `ut[1]`: Erstatt «til de passerer knærne, eller til du kjenner full strekk i baksiden av lårene (ofte midt på leggen)» med «til omtrent knehøyde, eller til du kjenner tydelig strekk bak lårene og ryggen fortsatt er uendret. Midt på leggen bare hvis du er bevegelig nok til det uten at ryggen endrer seg.»
- `ut[0]`: Behold «send hoftene bakover». Legg til «hold hodet i forlengelsen av ryggen og se mot gulvet, ikke i speilet» (K2, nakke).
- `feil`: Legg til «Du ser opp eller inn i speilet: nakken strammes og ryggen følger blikket.» «Du lener deg bakover i toppen» er riktig (hyperekstensjon i lås). Behold.
- `opp[0]`: Legg til «Ta stangen fra stativ i lår- til midjehøyde i stedet for fra gulvet» (K2).
- `sikker`: Behold «Stopp hvis ryggen begynner å runde seg». Legg til «Øk vekten sakte over uker. Hastig lastøkning er en større skadefaktor enn små tekniske avvik» (K6). Legg til «Rette ben/stiff-leg er for øvede».
- `pust`: Ingen av kildene sier noe om pust. Behold, men ikke påstå dokumentasjon.

### Anatomiske vinkler animasjonen bør vise

| Parameter | Topp | Bunn | Nåværende RIG | Avvik |
|---|---|---|---|---|
| Knefleksjon | ca. 5 til 10° | ca. 15 til 20°, nærmest konstant | 0° → 26° | Pose 0 for rett, pose 1 for bøyd. Endring 26° er for stor |
| Hoftefleksjon | 0° | ca. 80 til 90° | 0° → 83° | OK |
| Overkropp fra vertikal | 0° | ca. 65 til 75° | 0° → 65° | OK, litt grunt |
| Stang fra anklene (x) | over lår | over mellomfot, ca. 6 enheter foran ankelen | 5 enheter foran | OK |
| Stangens høyde | øvre lår | ca. knehøyde | 12 enheter over kne | Grunnere enn teksten |
| Armvinkel (bakover fra vertikalt) | 0° | 15 til 30° | 38° | Litt for mye, men modellbegrensning |
| Rygg | nøytral | nøytral (uendret) | rett linje | OK, ingen lumbal kurve vises |
| Hode | i forlengelse | i forlengelse | følger overkropp | OK |

Foreslått pose (regnet ut): pose 0 `sn:0, th:-8, to:0, ua:180, fa:180`; pose 1 `sn:0, th:-15, to:72, ua:215, fa:215`. Gir knefleksjon 8° til 15°, hoftefleksjon 87°, stang ca. 6 enheter foran ankelen, ca. 7 enheter over kneet.

### Skaderisiko og stopptegn
- Korsrygg: ryggen runder seg (lumbal fleksjon som ikke var der i starten), stangen drifter bort fra beina, smerte i korsrygg under eller etter.
- Hamstring: ved dypt, tungt og sakte (eksentrisk) er hamstring-strekk en plausibel risiko for en løper. Stopp ved skarp strekksmerte eller krampe bak lår.
- Nakke: å se opp eller i speilet (K1).
- Hvis hoftene ikke går bakover og knærne bøyer seg mer, gjør du en knebøy, ikke RDL. Stopp og reduser dybden.

---

## 2. enbensrdl (enbens rumensk markløft)

**Verdict: OK med små rettelser. Animasjonen er geometrisk god.**

### Hva kildene sier
- ACE (K7, lest): bryst opp, myke knær, hoftebredde. Strekk fri legg rett bakover mens overkroppen lener seg frem. Lang, flat rygg. «Komfortabelt punkt», ingen fast dybde. Armene kan holdes ut til balanse.
- Kohortstudie om enbens RDL hos friidrettsutøvere (K8, lest): standbenets kne lett bøyd, spinal nøytral, overkroppen «så parallell med gulvet som mulig», fritt ben i forlengelse. Unngå hofterotasjon og abduksjon i standbenet. Hånd på vegg/rekkverk mot motsatt side for balanse. Dybde avhenger av hamstring-fleksibilitet; ingen numerisk dybde.
- Biomekanikk for enbens RDL generelt: ingen av kildene målte vinkler.

### Vurdering
LIB sier «senk til overkroppen er nesten parallell med gulvet eller du mister nøytral rygg» som matcher K8. «Hold hoftene vendt mot gulvet» matcher K8 (unngå rotasjon). Manual i motsatt hånd er standard coaching, men K7 og K8 beskriver det ikke. Det er derfor «valgfritt», som teksten sier.

Regnet ut pose 1 (`sn:5, th:-8, to:75, la/lb:262`): knefleksjon 13°, hoftefleksjon 83°, overkropp 15° over horisontalen, fritt ben 8° under horisontalen (7° lavere enn overkroppslinja). Det er nærmest en T-form, godt innenfor «i flukt». Foten på fritt ben (`f2:180`) peker rett ned mot gulvet, som viser nøytral hoftestilling.

### Rettelser
- LIB `opp`: Legg til «Stå med lett bøyd kne, ikke låst» (finnes allerede), og «ha hånden i lett kontakt med en vegg eller stol mot sida av fritt ben om du er usikker» (K8).
- LIB `ut[2]`: Behold, men legg til «dybden er der du ennå kan holde ryggen og hoftene stille, ikke så dypt som mulig».
- LIB `feil`: Legg til «Fritt ben kastes høyere enn overkroppen: korsryggen svaier.» (min tolkning, K8 sier fritt ben i forlengelse).
- Animasjon: pose 0 har 0° knefleksjon. Bytt til `th:-6` for lett bøyd kne som i teksten. Manualen henger ca. 26 enheter foran ankelen (ua 195). Bruk `ua/fa:205 til 210` så manualen henger nærmere forfoten.

### Skaderisiko og stopptegn
- Fall/balanse: sett den andre foten ned umiddelbart ved ustø. En 50-åring bør bruke støtte i starten.
- Korsrygg: runding eller rotasjon i bekkenet (åpen hofte).
- Hamstring: som rdl. Gjenta jevnt på begge sider.

---

## 3. hipthrust

**Verdict: OK i teksten (liten mangel), men MÅ ENDRES i animasjonen: føttene «flyter» ca. 6 cm over gulvet i toppen, og benken svever.**

### Hva kildene sier
- Biomekanikkstudie (K9, lest i Europe PMC-fulltekst, Brazil et al. 2021): 19 trente menn, barbell hip thrust, 70 % av 1RM. Hofteekstensjon-ROM 75 ± 19°; kneekstensjon-ROM 21 ± 7°; bekken-trunk-ROM 12 ± 21° (både ekstensjon og fleksjon forekom mellom deltakere). Stangens vertikale forflytning 0,361 m. Lockout-vinkler for kne/hofte/bekken er ikke oppgitt. Ingen sikkerhetsråd.
- Oversikt om supine bridge del I (K10, lest delvis): maksimal fysiologisk hofteekstensjon er ca. 20° forbi nøytral. Det barbell hip thrust avsluttes når trunk-bekken-lår er parallelt med gulvet; 5 til 6 cm høyere gir hofte-hyperekstensjon. Overdreven lumbal lordose og fremre bekkentilt er «ofte observert», drevet av erector spinae-dominans. Mer knefleksjon gir mer sete og mindre hamstringsaktivitet. Hamstringkramper er vanlig i enbens bridge, og føttene nærmere setet kan redusere det. Posterior bekkentilt ga høyere setemuskel-aktivitet enn fremre tilt i én studie (25 deltakere).
- Oversikt om bridge og korsryggsmerter del II (K11, lest delvis): ved ekstensjonsmønster-LBP skal ryggraden «ikke gå utover nøytral». Bekkenhevingen skal komme primært fra hofteekstensjon, ikke fra korsryggen. Knefleksjon 60 til 90° anbefales. Barbell hip thrust med rygg mot benk «ser ut til å lette begrensning av lumbal hyperekstensjon». Samme kilde sier motsatt for fleksjonsmønster-LBP (der foretrekkes hyperekstensjon). Forfatteren sier selv at dette er «stort sett teoretisk» og ikke formelt testet. Kildene er altså uenige, og det finnes ingen god evidens for at hyperekstensjon er nødvendig for friske.
- ACE (K12, lest): stangen på toppen av hoftene (pute), hofter presses til full ekstensjon, muskelspenning gjennom hele bevegelsen. Ingen vinkler eller skulderplassering.
- Contreras, praksisblogg (K13, K14, lest, ikke fagfellevurdert): toppen er den vanskeligste delen, erektorene produserer ekstensjon og fremre tilt. Han opplevde at maksimal svai ga korsryggsmerter hos noen klienter. «Scoop»-metoden bruker bevisst bakoverrotert bekken og hake mot brystet. Begge metoder har vertikale legger i lockout og skulderblad lavt mot benken. Lavere benk reduserer hyperekstensjon.

### (b) Besvarelse
- **Kan korsryggen hyperekstendere i toppen?** Ja. Det er den vanlige feilen (K10, K13). Når hoftene har nådd rett linje, er mer høyde på hoftene kun korsrygg-svai og hofte-hyperekstensjon (K10). Kildene er ikke enige om hvor mye ekstensjon som er «lov» (K11 vs K13), men ingen anbefaler maksimal svai for en frisk 50-åring. Behold «ribbeina nede» og «rett linje».
- **Riktig bekkenposisjon.** Nøytral til lett posterior tilt i toppen, drevet av setemuskelen (K10, K11, K13). Ingen kilde oppgir grader. Jeg anslår «noen få grader bakoverrotert, ikke maks». Tekstens «klem setet» gir det. Legg til «ribbeina ned mot bekkenet».
- **Skulderblad.** Kantene av benken ved nedre del av skulderbladene, lavt (K13, K14; LIB sier det samme). Ikke på nakken. Skulderleddet står noen cm over benkplata.
- **Kne/legg i toppen.** Leggene omtrent vertikale, kne ca. 90° (K13, K14; K11 sier 60 til 90° knefleksjon i bridge). Det er ingen studie som viser at nøyaktig 90° er best. K10 sier mer knefleksjon gir mer sete og mindre hamstring. Fottrinn nærmere setet hvis hamstring krampar.

### RIG-sjekk (regnet ut)
- Pose 1 (`sn:0, th:270, to:-90`): kne 90°, legg vertikal, overkropp og lår i perfekt rett linje (0° hofteekstensjon). Det samsvarer med K10 («parallelt med gulvet»). God.
- Pose 0 (`sn:-31, th:240, to:-55`): hofte ca. 65° fleksjon, overkropp ca. 35° over horisontalen. Rimelig.
- **Feil:** ankelen er i (128, 132) i pose 0 og (125, 128) i pose 1. Foten løftes altså 4 enheter (ca. 6 cm) og glir 3 enheter. Føttene skal være plantet. Grunnen er at figuren er forankret i skulderen, ikke i foten.
- **Feil:** benk-rektangelet går til y=132, men gulvet er y=138. Benken svever 6 enheter.
- Skulderleddet står ved x=55; benkkanten ved x=58. Kanten bør ligge ca. 7 til 8 enheter nedover overkroppen fra skulderleddet (nedre del av skulderbladene), altså x≈62 til 63.
- Lumbal kurve og bekkentilt kan ikke tegnes med denne rigen (ingen bekken-segment). Dette må løses i tekst/etikett.

### Rettelser
Animasjon (hipthrust og enbenship): pose 1 `sn:-8, th:270, to:-84` (gir ankel (128, 132) som i pose 0, knevinkel ca. 98°, legg ca. 8° fra vertikalt, hofte i samme høyde som benktopp). Benk: `h:32` (y 106 til 138) og `x:22, w:40` slik at kanten ligger ved x≈62.

LIB-tekst (hipthrust):
- `ut[0]`: «...løft hoftene til overkropp og lår er i en rett linje (ikke høyere), leggene omtrent vertikale».
- `ut[1]`: «Ribbeina ned mot bekkenet, rull bekkenet litt bakover og klem setet. Ikke svai korsryggen.»
- `feil[2]`: «Hoftene løftes for høyt: det er korsryggen som svaier, ikke hoftene som jobber.»
- `feil`: Legg til «Hamstring krampar: flytt føttene nærmere setet» (K10).
- `tips`: Behold «Underarmene nede, ikke dytt med hodet.»
- `sikker`: Behold pute og stabil benk. Legg til «Stopp ved smerte i korsrygg eller hoftebøyer».

### Skaderisiko og stopptegn
- Korsrygg: svai i toppen, smerte i korsryggen (ikke i setet).
- Nakke: hodet presset mot benk eller hake som kastes bakover.
- Hamstring: kramper (flytt føttene nærmere).
- Hofte: spenning/«klikk» foran i hoften i toppen kan tyde på for stor hofteekstensjon eller hoftebøyer-stramhet.

---

## 4. enbenship (enbens hip thrust)

**Verdict: OK i hovedsak. Samme animasjonsrettelser som hipthrust (fot og benk). Teksten er veldig kort og bør utvides litt.**

### Hva kildene sier
K10 (single-leg bridging: 40 til 54 % MVIC seteknebøy og høyere hamstringsaktivitet; hamstringkramper vanlig). K11 (progresjon til enbens: hold bekkenet i nivå). K13 (anbefaler samme topp-prinsipper).

### Vurdering
Fritt ben i RIG: `la:55 → 70`, `lb:70`. Låret går fra 35° over horisontalen til 20° over horisontalen med strukket kne. Det er et strukket fritt ben noe over standbenets lår. Det er akseptabelt. Alternativ er kne bøyd 90° mot brystet. Begge brukes. Hoftene skal holdes i nivå (K11), og dette kan ikke vises i sidevisning.

### Rettelser
- LIB `opp`: «Samme som hip thrust, men ett ben løftet (kne bøyd mot brystet eller strukket i linje med låret på det andre)».
- LIB `ut`: Behold. Legg til «ribbeina ned, ikke svai korsryggen» (K10). Legg til at hoften skal ikke synke på løftet bens side (K11).
- LIB `feil`: Behold. Legg til «Hamstring krampar: flytt foten nærmere setet».
- LIB `sikker`: «Stopp ved krampe eller smerte i korsrygg» (utvid fra bare «krampe»).
- Animasjon: som hipthrust.

### Skaderisiko
Høyere hamstringsbelastning enn to bens (K10). Fremre bekkentilt og svai lettere ved ensidig last (K10). Stopp ved korsryggsmerte eller krampe.

---

## 5. plank (underarmsplank)

**Verdict: OK med to rettelser i teksten (varighet, tegn på tapt form) og en geometrijustering i animasjonen.**

### Hva kildene sier
- ACE Front Plank (K15, lest): albuer under skuldrene, stram kjernen, hold skuldre stablet over albuer uten å trekke dem opp, fortsett å puste; hold minst 5 sekunder; stopp ved smerte i korsryggen.
- ACE-søkeutdrag (K16, kun utdrag): hvis du ikke klarer 10 sekunder uten at hoftene synker, gå ned på knærne. Anbefaler 10 sekunder på og 2 av, fire til seks sett. Lange hold mister verdi og gir dårlig holdning.
- Harvard Health (K17, lest): hode, nakke og hæler i én linje, se ned, stram magen, pust jevnt. 10 til 30 sekunder per hold, 2 til 3 sett; kan jobbe opp til 1 til 2 minutter, men lite ekstra nytte utover 2 minutter. Ved ryggproblemer: på knærne eller stående mot benk i 45°.
- Tverrsnittsstudie om plank og korsryggsmerter (K18, lest, 117 voksne): testen ble avsluttet ved tap av nøytral stilling (overdreven lumbal ekstensjon eller bekkensenk). Personer med korsryggsmerter holdt planken lenger enn de uten. Forfatterne konkluderer at plankvarighet alene ikke er en markør for rygghelse. Bro-til-plank-forholdet (bakre kjede relativt til fremre) var knyttet til lavere funksjonshemming. Anbefaler å trene bakre kjede (hip thrust, enbens bro) ved siden av.
- McGill (K19, kun utdrag fra pressen/søk, sekundær): korte, gjentatte 10-sekunders hold er bedre enn lange. Han har sett plank-relatert skade hos folk med ryggsmerter som holdt for lenge. Dette er ikke verifisert mot originalkilden.

### (c) Besvarelse
- **Albuer.** Rett under skuldrene (K15, K18, ACE). LIB sier det samme. Riktig.
- **Hvor lenge.** Kildene er uenige. McGill/ACE: korte hold, ca. 10 sekunder gjentatt. Harvard: 10 til 30 sekunder, 2 til 3 sett. K18: lengde alene sier lite. LIB sier 30 til 45 sekunder. Det er i øvre ende og greit hvis formen holder, men mer enn Harvard og ACE anbefaler. Anbefalt tekst: «10 til 30 sekunder, 2 til 4 sett. Stopp når formen går; flere korte hold slår ett langt.»
- **Tegn på tapt form.** Hoftene synker (korsrygg-svai), rumpa løfter seg (pike), hodet henger ned eller kastes opp, skuldrene stiger mot ørene, smerte i korsrygg eller skuldre (K15, K17, K18). Teksten har de fleste. Legg til skuldre mot ørene og «magen stram» som siste test.

### RIG-sjekk (regnet ut)
`sn=th=to=78` er en perfekt rett linje fra ankel til skulder, 12° over horisontalen. Albuen står rett under skulderen (`ua:180`). Hodet følger overkroppen (nøytral nakke). Det er riktig.

Geometrifeil (kosmetisk): albuen står ved y≈131,6 med underarmen på y≈131,6, men gulvet er y=138, så underarmen svever ca. 4 enheter. Tåen står 3 enheter under gulvlinja. Løsning: `at:[45,125]` og `sn=th=to=83`. Gir albu på gulvet, tå på gulvet og 7° helning (realistisk ca. 7 til 10°).

### Rettelser
LIB `ut[2]`: «Pust rolig mens du holder 10 til 30 sekunder. Gjenta 2 til 4 ganger.»
LIB `tips[1]`: «Stopp når formen går» (finnes). Legg til «Hell heller 4 gode hold på 15 sekunder enn ett slapt på 45».
LIB `feil`: legg til «Skuldrene trekkes mot ørene».
LIB `sikker`: Behold. Legg til «Har du korsryggsplager: plank på knær eller mot benk».

### Skaderisiko og stopptegn
Korsrygg-svai (hoftene synker), smerte i korsrygg eller skuldre, skuldre som skyter mot ørene, pusten som stopper opp. Planken er en ensidig fremre kjerneøvelse; K18 anbefaler at den kombineres med bakre kjede.

---

## 6. baertur (farmer's walk)

**Verdict: OK. Liten tekstjustering («lange skritt») og en kosmetisk justering av gangsyklus. Kildegrunnlaget er svakt for detaljer.**

### Hva kildene sier
- ACE Farmer's Carry (K20, lest): manualer ved siden av hoftene, armer hengende, rett rygg, fast grep, gå en bestemt distanse og snu.
- Muskelaktiveringsstudie (K21, lest): farmer's carry ga høyere aktivering av korsryggsmuskler (longissimus, multifidus) enn statisk hold; plank ga mye mer mage. Antagelig drevet av ustabilitet. Studien målte ikke skaderisiko. Én deltaker ble ekskludert fordi grepet ikke holdt.
- Unilateral farmer's walk (K22, lest, om ensidig bæring): McGill sin sammenligning viser at 30 kg i hver hånd gir markant lavere spinal kompresjon enn 30 kg i én hånd. Ensidig bæring gir mer lateral bøy og skjærkrefter. Stopp-kriterier i studien: lateral fleksjon over 8°, dårlig gange eller utmattelse. Ingen sikker lastgrense fantes før denne studien.
- NSCA (kun søkeutdrag, sekundær): hold overkroppen høy, gå sakte og kontrollert, unngå lateral bøy; start med like vekter i begge hender.

### Vurdering
LIB er i all hovedsak kompatibel med kildene. Kildene gir ingen skrittlengde. Teksten «rolige, lange skritt» kan oppfattes som oversteg. Jeg foreslår «jevne, normale skritt». Det er min vurdering, ikke en kildeopplysning. «Skuldrene bak og ned» har ingen direkte kilde i de lesne tekstene, men er konsistent med ACE «rett rygg» og K22 «høy overkropp».

**«Høy kropp»** (cue) er trygt og støttet av K22 og NSCA-utdraget.

RIG: overkropp og armer er lodrett (ua/fa 180), manualen ved hoften. Det matcher K20. Fritt ben svinger `la:150 → 210` (±30° fra vertikalt). Ved normal gange er hofteekstensjon bak kroppen typisk ca. 10 til 15°, ikke 30° (generell gangbiomekanikk, ikke fra kildene over). Standbenet står stille i begge poser, så bare det ene benet beveger seg. Det er en forenkling. Foreslått `la:150 → 195` (30° frem, 15° bak) og eventuelt tilsvarende motfase på nærbenet.

### Rettelser
- LIB `ut[0]`: «Gå jevne, kontrollerte skritt 20 til 30 meter.»
- LIB `feil`: Legg til «Skuldrene trekkes opp» (finnes), «Grepet slipper: bruk lettere vekt, ikke strikk eller stropper først».
- LIB `sikker`: Legg til «Velg en vekt du kan bære hele distansen uten å lene deg eller heve skuldrene. Ensidig bæring (suitcase) belaster korsryggen mer (K22). Start med to like vekter.»
- Animasjon: reduser bakre benutslag som over.

### Skaderisiko og stopptegn
Sidelening (K22: lateral fleksjon > 8° var stoppkriterium), skuldre mot ørene, hakkete gange, grepet svikter, smerte i korsrygg/skuldre. Rydd gulvet; manualer på føttene er en reell risiko.

---

## 7. deadbug

**Verdict: OK i hovedsak. Teksten bør presisere «nøytral/lett mot gulvet» og kvalitet fremfor antall. Animasjonen viser frie benet noe høyt over gulvet.**

### Hva kildene sier
- Harvard Health (K23, lest): kne og hofte 90°, armer over skuldrene. Hold korsryggen presset ned uten å svaie. Trekk nedre mage inn mot navlen (som å lukke en stram bukse). Strekk ett ben til parallelt med gulvet og noen få cm over, mens motsatt arm går bak hodet. Stopp der du kan holde ryggen flat og magen aktiv. 8 til 12 repetisjoner, 1 til 2 sett, 3 til 4 ganger i uka. «Siste repetisjon skal se like god ut som den første.» Fortsett å puste, ikke hold pusten. Lettere: føttene i gulvet, én arm om gangen. Stopp ved smerte.
- NHS-trust (Frimley) via søkeutdrag (K24, kun utdrag): trykk nedre rygg forsiktig mot gulvet, strekk ett ben og motsatt arm, bytt side, ca. 10 sakte repetisjoner, 3 sett.
- Studie av dead bug (Korea; K25, kun søkeutdrag): utført med spinal i nøytral stilling og abdominal draw-in.
- Søkeutdrag fra treningskilder (K26, svak): hvis ryggen buer seg, er bevegelsen for stor; forkort løftearmen (gjør ett ben/én arm av gangen).

### (d) Besvarelse
- **Kvalitet vs. repetisjoner.** Kildene prioriterer kvalitet: 8 til 12 repetisjoner/1 til 2 sett (K23), ca. 10 sakte × 3 (K24). Ingen støtter høye repetisjonstall. LIB sier «kvalitet fremfor antall» men ikke hvor mange. Anbefalt: «6 til 10 kontrollerte repetisjoner per side, 2 til 3 sett; stopp seriene når korsryggen løfter seg.»
- **Korsrygg mot gulvet.** Kildene sier «presset ned/forsiktig mot gulvet» (K23, K24), men K25 bruker nøytral spinal. Noen kilder sier «flat». Det er en nyanse: målet er at korsryggen ikke skal bevege seg, ikke at den skal klemmes hardt i gulvet. LIB sier «presse korsryggen lett mot gulvet», som er greit. Jeg anbefaler å legge til «ikke klem hardt, men la den ikke svaie. Korsryggen skal være stille under hele bevegelsen».

### RIG-sjekk (regnet ut)
- Start: lår vertikalt (hofte 90°), legg horisontalt (kne 90°), armer rett opp. Matcher K23 helt.
- Slutt: arm `-90` (langs gulvet bakover, i skulderhøyde), fritt ben `la:80, lb:85` (ca. 10° og 5° over horisontalen). Ankelen havner ca. 16 enheter (ca. 24 cm) over gulvlinja, målt fra mattelinja, og ca. 8 enheter over hofteleddets høyde. K23 sier «parallelt og noen få cm over gulvet». Benet er altså noe høyt. Foreslått `la:88, lb:90`.
- Nærbein står i 90/90 under hele bevegelsen. Riktig motsatt arm/ben-par: nær arm + fjernt ben.
- Merk: «fjern arm» tegnes som en kopi av nær arm og forskyves 3 enheter. Begge armer ser derfor ut til å gå bakover. Det er en kosmetisk begrensning i rigen. Hvis mulig vises den fjerne armen oppe.
- Korsrygg-kurve og bekkenstilling kan ikke vises. Overkroppen er en rett linje flatt på matta (OK som «ryggen stille»).

### Rettelser
- LIB `opp[1]`: «Hold korsryggen stille og lett mot gulvet, ikke klem hardt og ikke la den svaie.»
- LIB `ut`: legg til «Strekk bare så langt du kan holde ryggen stille».
- LIB `tips`: «6 til 10 rolige repetisjoner per side, 2 til 3 sett. Siste repetisjon skal se like god ut som den første.»
- LIB `feil`: legg til «Ribbeina åpner seg og buer ut.» (K24).
- Animasjon: `la:88, lb:90`.

### Skaderisiko og stopptegn
Korsryggen løfter seg eller svaier, ribbeina åpner seg, nakken spenner seg, pusten stopper, smerte i korsrygg. Lav risiko ellers (K23).

---

## 8. pallof (Pallof press)

**Verdict: OK. Retningen og prinsippet er riktig i både tekst og animasjon. Små presiseringer i teksten og en dimensjonsfeil i animasjonen (armene for lange).**

### Hva kildene sier
- Åpen studie av holdningskontroll under Pallof press (K27, lest): lateral kraft fra kabel/strikk skaper dreiemoment; målet er å holde bekken og spinal nøytrale mot torsjonen. Konvensjonelt holder man overkroppen stille mens albuene bøyes og strekkes. I studien ble albuene holdt strake og posisjonen holdt isometrisk. I stående varianter lente deltakere seg lateralt bort fra strikken for å holde balansen, særlig i tandem-stilling. Bøyd kne/kneling er enklere enn stående. Standbredde og høyde på kraften endrer vanskelighetsgraden.
- Catalyst Athletics (K28, lest): stå på tvers av ankeret med kabel/strikk i brysthøyde, press hendene rett frem fra brystet til strake armer og tilbake. Kjernen må hindre rotasjon mot ankeret. Bevegelse kun i armene. 3 til 5 sett à 10 til 20 reps eller isometrisk 20 til 30 sekunder.
- Sussex-PDF (K29): ga ikke lesbar tekst (komprimert PDF). Kun et søkeutdrag: «hold kjernen stram, ta noen skritt bort for spenning, rett frem».
- Anti-core-oversikt (K30, lest): anti-rotasjon, anti-ekstensjon og anti-lateral fleksjon fungerer som kategori; ingen teknikkdetaljer for Pallof.

### (e) Besvarelse
- **Retning på pressen.** Rett frem fra brystet, vinkelrett på kabelen (K27, K28). Ikke mot kabelen, ikke bort fra. LIB: «Press hendene rett frem fra brystet til strake armer» er riktig.
- **Kroppen skal ikke rotere.** Det er hele poenget (K27, K28). LIB sier «uten å la kroppen rotere mot kabelen». Det er riktig. Legg også til «hold hofte og skuldre vinkelrett frem».
- **Vanlige feil.** Å lene seg bort fra kabelen er dokumentert (K27, lateral lening i stående). «Skuldrene trekkes opp» er fornuftig coaching (K28 «brace»).

### RIG-sjekk (regnet ut)
Toppvisning: overkropp som horisontal stang, hoder foran, hender langs midtlinja frem fra brystet. Kabelen kommer fra siden (anker ved x=22), omtrent vinkelrett i start og skråere når armene strekkes. Overkroppen er statisk. Riktig. Kablen fester «foran» skulderlinja noe, så strekket peker litt bakover. Det er realistisk når man står en kabelsteg unna.

Feil: i pose `h:1` er hendene ved y=44, 54 enheter fra skuldrene. Armen er 42 enheter (ua 22 + fa 20) i sidevisningen. Armene er 25 % for lange. Hender bør stoppe ved y≈57 (`h≈0,6`).

### Rettelser
- LIB `opp`: legg til «Sett kabelen i brysthøyde og stå slik at kabelen drar rett i siden av deg».
- LIB `ut`: «Press hendene rett frem fra brystet... Hold hofte og skuldre vinkelrett frem (ikke vri mot kabelen)». Hold: «2 sek» er greit, med 5 til 10 repetisjoner per side.
- LIB `tips`: Behold. Legg til «gjør begge sider».
- LIB `lett`: «Stå nærmere ankeret, eller kneel på ett kne» (K27: kneling er lettere).
- Animasjon: reduser `h` slutt til ca. 0,6.

### Skaderisiko og stopptegn
Rotasjon i overkroppen (mist kontrollen), svai i korsrygg, skuldre opp mot ørene, ubehag i skulder ved strakt arm. Lav risiko; vekten bør være lett.

---

## Animasjonsspesifikasjon (sammendrag)

Alle vinkler i RIG-konvensjon. «Nå» er nåværende RIG, «Foreslått» er mitt forslag. Tall merket (r) er regnet ut av meg fra geometrien, ikke fra kilder.

| Øvelse | Parameter | Nå (pose 0 → 1) | Foreslått (pose 0 → 1) | Begrunnelse |
|---|---|---|---|---|
| rdl | sn / th / to | 0/0/0 → 8/-18/65 | 0/-8/0 → 0/-15/72 | Konstant lett kne (8 → 15°), hofte 87°, mer hengslet (r) |
| rdl | ua = fa | 180 → 218 | 180 → 215 | Stang mot lår, mellomfot (r) |
| rdl | tekst | «forbi knærne / midt på leggen» | «ca. knehøyde» | K1, K2 |
| enbensrdl | pose 0 th | 0 | -6 | Lett kne også i start |
| enbensrdl | ua = fa (pose 1) | 195 | 205 til 210 | Manual nærmere forfot (r) |
| hipthrust | sn / th / to (pose 1) | 0/270/-90 | -8/270/-84 | Ankel (128,132) plantet; kne ca. 98° (r) |
| hipthrust | benk | y 106 til 132, x 22 til 58 | y 106 til 138, x 22 til 62 | Benk på gulvet, kant ved nedre skulderblad |
| enbenship | pose 1 | som over | som over | Samme fot- og benkjustering |
| plank | at / sn=th=to | [45,130] / 78 | [45,125] / 83 | Albu og tå i gulvet (r) |
| baertur | la (pose 1) | 210 | 195 | Mindre bakover-utslag (generell gangbiomekanikk) |
| deadbug | la / lb (pose 1) | 80 / 85 | 88 / 90 | Benet «noen få cm over gulvet» (K23) |
| pallof | h (slutt) | 1 | ca. 0,6 | Armlengde 42, ikke 54 (r) |

### Anatomiske hovedmål (hva figuren bør vise)

| Øvelse | Nøkkelposisjon | Mål |
|---|---|---|
| rdl | Bunn | Kne ca. 15°, hofte ca. 85°, overkropp ca. 70° fra vertikalt, stang ved/rett over kne, nær bein, ryggen uendret |
| enbensrdl | Bunn | Standkne ca. 13°, overkropp og fritt ben nesten horisontale i én linje, hofter mot gulvet |
| hipthrust | Topp | Skuldrer på benkkant, overkropp+lår i rett linje (0° ekstensjon), kne ca. 90 til 100°, legger nesten vertikale, bekken lett bakover, ribbein ned, hake lett mot bryst |
| plank | Hold | Rett linje ankel-hofte-skulder-hode, albue under skulder, ca. 7 til 12° helning |
| baertur | Gange | Høy overkropp, armer rett ned, manual ved hoften, moderat skrittlengde |
| deadbug | Slutt | Nærbein 90/90, fjern arm og ben strukket nesten parallelt med gulv, korsrygg stille |
| pallof | Topp | Armer strake rett frem fra brystet, overkropp uten rotasjon, kabel fra siden |

---

## Kildeliste

Alle åpne. «Lest» = innhold hentet og lest i økten. «Utdrag» = kun sett som søkeresultat-sammendrag.

- K1. ACE, The ACE Do it Better Series: The Romanian Deadlift (lest). https://www.acefitness.org/continuing-education/certified/may-2025/8865/the-ace-do-it-better-series-the-romanian-deadlift/. Slutt-dybde ca. knehøyde, mid-shin for bevegelige; konstant lett kne; stang i kontakt med kroppen.
- K2. ACE, ACE Technique Series: Romanian Deadlift (lest). https://www.acefitness.org/continuing-education/prosource/january-2016/5767/ace-technique-series-romanian-deadlift/. Samme innhold; se ned, ikke i speil; start fra stativ; rette ben bare for erfarne.
- K3. ACE Exercise Library, Romanian Deadlift (lest). https://www.acefitness.org/resources/everyone/exercise-library/317/romanian-deadlift/. Lett, konstant kne; flat rygg; stang tett på kroppen; stopp ved strekk bak lår.
- K4. Physiopedia, Romanian deadlift og Deadlift Exercise (kun utdrag; direkte henting ga 403). https://www.physio-pedia.com/Romanian_deadlift og https://www.physio-pedia.com/Deadlift_Exercise. Stangen nær beina i stedet for under skuldrene; kne ca. 15°; dybde under kne eller midt på legg om formen tillater.
- K5. An Electromyographic Analysis of Romanian, Step-Romanian, and Stiff-Leg Deadlift (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC8835508/. Beskriver RDL med lett bøyde knær, rett spinal, skuldre bak og ned; ingen vinkler.
- K6. Beyond the Neutral Spine: narrativ oversikt, lav ryggskade ved markløft (lest, delvis). https://pmc.ncbi.nlm.nih.gov/articles/PMC13120164/. Moderat lumbal fleksjon er ikke dokumentert skadelig hos trente; nøytral omtolkes som kontrollert; lastprogresjon er viktigere enn teknikk.
- K7. ACE Exercise Library, Single-Leg Romanian Deadlift (lest). https://www.acefitness.org/resources/everyone/exercise-library/329/single-leg-romanian-deadlift/. Myke knær, flat rygg, fritt ben bakover, komfortabel dybde.
- K8. The Effect of Single Leg Romanian Deadlift on the Risk of Hamstring Strain Injuries in Track and Field Athletes (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC12048357/. Lett bøyd standkne, nøytral spinal, parallelt med gulv så langt mulig, unngå hofterotasjon.
- K9. A comprehensive biomechanical analysis of the barbell hip thrust (Brazil et al., 2021; lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC8006986 (abstract https://pubmed.ncbi.nlm.nih.gov/33780488/). Hofte-ROM 75°, kne-ROM 21°, bekken-trunk-ROM 12 ± 21°; lockout-vinkler ikke oppgitt.
- K10. Supine Bridge Exercise: A Narrative Review (Part I) (lest delvis via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC11981018/. Maks fysiologisk hofteekstensjon ca. 20°; hip thrust-slutt = parallelt; lumbal hyperekstensjon og fremre tilt vanlig feil; mer knefleksjon gir mer sete; kramper.
- K11. Supine Bridge Exercise for Low Back Pain (Part II) (lest delvis via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC12145699/. Uenige anbefalinger etter LBP-type; bekkenløft fra hofte, ikke korsrygg; kne 60 til 90°; «stort sett teoretisk».
- K12. ACE, Understanding the Barbell Hip Thrust (lest). https://www.acefitness.org/continuing-education/certified/november-2019/7403/understanding-the-barbell-hip-thrust/. Stang på toppen av hoftene med pute; full hofteekstensjon; ingen vinkler.
- K13. Contreras, praksisblogg om hip thrust og fremre bekkentilt (lest; ikke fagfellevurdert). https://bretcontreras.com/?p=7735.
- K14. Contreras, praksisblogg om «scoop» og «hinge»-metode (lest; ikke fagfellevurdert). https://bretcontreras.com/?p=42836. Vertikale legger og lavt skulderblad mot benk i begge metoder; bakoverrotert bekken i «scoop».
- K15. ACE Exercise Library, Front Plank (lest). https://www.acefitness.org/resources/everyone/exercise-library/32/front-plank/. Albuer under skuldre; skuldre stablet; stopp ved smerte.
- K16. ACE, planksøk (kun utdrag). https://www.acefitness.org/resources/everyone/blog/6327/plank-variations-5-plank-variations-to-strengthen-your-core/. 10 s på / 2 s av; gå ned på knærne hvis hoftene synker.
- K17. Harvard Health, Straight talk on planking (lest). https://www.health.harvard.edu/blog/straight-talk-on-planking-2019111318304. 10 til 30 s per hold, 2 til 3 sett, lite ekstra nytte utover 2 min; hode-nakke-hæl i linje; regresjon ved ryggproblemer.
- K18. The Core of the Issue: Plank Performance and Pain in the Lower Back (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC12155697/. Albuer under skuldre; testen avsluttes ved tap av nøytral stilling; plankvarighet alene er ikke en markør for rygghelse.
- K19. McGill-sitater om korte plank-hold (sekundær, kun søkeutdrag). Ikke verifisert mot originalkilde. Relatert primærkilde: McGill 2010, Clinical tools to quantify torso flexion endurance, https://www.backfitpro.com/medical-scientific-articles/2010/[76]McGill,S.M.(2010)Clinical-tools-to-quantify-torso-flexion-endurance[Occupational-Ergo.].pdf (ikke lest).
- K20. ACE Exercise Library, Farmer's Carry (lest). https://www.acefitness.org/resources/everyone/exercise-library/359/farmer-s-carry/. Manualer ved hoftene, armer hengende, rett rygg, fast grep.
- K21. The Quantification of Muscle Activation During the Loaded Carry Movement Pattern (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC11042841/. Farmer's carry ga høyere ryggstrekker-aktivering enn hold; plank høyere mage; ingen skaderisiko målt.
- K22. Fat-Free Mass and the Balance Error Scoring System Predict an Appropriate Maximal Load in the Unilateral Farmer's Walk (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC6315369. Tosidig bæring gir lavere spinal kompresjon enn ensidig; stopp ved lateral fleksjon over 8°.
- K23. Harvard Health, The many benefits of the dead bug (lest). https://www.health.harvard.edu/exercise-and-fitness/the-many-benefits-of-the-dead-bug. 90/90, korsrygg ned uten svai, ben parallelt noen cm over gulv, 8 til 12 reps, kvalitet.
- K24. Frimley Health NHS, core and diastasis recti exercises (kun utdrag). https://www.fhft.nhs.uk/patients-and-visitors/patient-information-library/pelvic-health-core-and-diastasis-recti-abdominis-exercises. Trykk nedre rygg forsiktig ned; ca. 10 sakte reps × 3.
- K25. Korea (kun søkeutdrag): dead bug utført med nøytral spinal og abdominal draw-in. https://koreascience.or.kr/article/JAKO201718155358635.pdf.
- K26. Treningskilder om dead bug (svak, kun utdrag): forkort bevegelsen hvis ryggen buer seg. https://thebarbellphysio.com/core-movement-every-fitness-athlete-needs-master-optimal-performance/.
- K27. Effect of Body Position and Support Surface on the Postural Control Challenge During the Pallof Press Exercise (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC11857476/. Lateral kraft, hold bekken/spinal nøytral, lateral lening i stående, kneling er enklere.
- K28. Catalyst Athletics, Pallof Press (lest). https://catalystathletics.com/exercise/526/Pallof-Press. Press rett frem fra brystet, motstå rotasjon, 3 til 5 × 10 til 20 eller 20 til 30 s hold.
- K29. Sussex Sport, anti-rotation Pallof press (PDF ikke lesbar). https://www.sussex.ac.uk/sport/documents/anti-rotations-pallof-press.pdf.
- K30. The role of anti-core exercises in public health (lest via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC13143152/. Kategoridefinisjon; ingen teknikkdetaljer.

## Hvor usikkerheten er størst

1. **RDL-dybde og armvinkel:** Ingen kilde oppgir tall. Konklusjonene hviler på ACE (knehøyde / mid-shin), Physiopedia-utdrag og min geometriberegning.
2. **Hip thrust lockout-vinkler:** Ingen kilde oppgir lockout-vinkler for kne, hofte eller bekken. «Rett linje» og «vertikale legger» kommer fra Contreras og ACE-tekst; 90° kne er coaching-konvensjon, ikke en målt optimal verdi.
3. **Hyperekstensjon i korsryggen:** Kildene er uenige (K11 anbefaler det ved enkelte LBP-typer, motsatt ved andre). For en frisk 50-åring: nøytral til lett posterior tilt er forsvarlig.
4. **Plankvarighet:** McGill-sitatene er sekundære. Harvard og ACE er mer konservative enn LIBs 30 til 45 sekunder.
5. **Farmer's walk skrittlengde og skulderposisjon:** Ingen kilder gir tall. «Normale skritt» er min vurdering.
6. **Alle «regnet ut»-tall** avhenger av at RIG-proporsjonene (1 enhet ≈ 1,5 cm) er riktige. De er brukt til sammenligning mellom poser, ikke som absolutte mål.
