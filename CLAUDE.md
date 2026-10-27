Haurer Media — Briefing für Claude

Dieser Text wird zu Beginn jeder Sitzung geladen. Danach weiß Claude, wer du bist,
was ihr verkauft, wie eure Dokumente und Videos aussehen und welche Regeln gelten.
Stand: 27.10.2026.

## 1 — Wer

- **Harun Gür**, Inhaber **Haurer Media**, Video- und Social-Media-Agentur, Sitz Hilden.
- Antworte **immer auf Deutsch**, direkt und tempoorientiert. „Einfach machen" statt lange fragen.
- Kontakt: business@haurer.de · info@haurer.de
- Umfeld: David (Dreh/Schnitt), Nazli, Rabia (Minijob).

## 2 — Preise

Quelle: `haurer-media/website/src/data/preise.ts` — die Website ist maßgeblich.
Niemals unter Listenpreis anbieten; der Kunde kann sie nachlesen.

### Monatliche Betreuung (Retainer)

| Paket | Netto/Monat | Reels | Carousel/Foto | Drehtage | Kanäle |
|---|---|---|---|---|---|
| Marke | 3.950 € | 10 | 4 | 1 | 1 |
| Wachstum | 5.530 € | 14 | 6 | 1–2 | 2 |
| Marktführer | 7.900 € | 20 | 8 | 2 (prio) | 3–4 |
| Individuell | 11.500 € | individuell | individuell | 3+ | alle |

Setup einmalig: 990 €
Zusätzlicher Drehtag: 1.890 €

**Rechner-Logik:** Nur additive Regler, nie nach unten rechnen. Aufpreise liegen ÜBER der
Paketrate, damit Dazubuchen nie günstiger ist als die nächste Stufe:

- je zusätzliches Reel: 440 €
- je zusätzlicher Carousel-/Fotobeitrag: 150 €
- mehrere Standorte: 450 €

Der Online-Rechner kennt NUR Reels, Beiträge und Standorte — keine Drehtage, keine Kanäle,
keine Stories, keine Auswertung. Wer ein individuelles Angebot rechnet, darf diese Posten
deshalb nicht als 'laut Preisliste' ausweisen.

### Einzelprojekte (ab-Preise, inkl. Konzept, 1 Drehtag, Schnitt, Color, Sound)

| Projekt | ab |
|---|---|
| Social Reel | 1.690 € |
| Testimonial-Video | 2.290 € |
| Produktvideo | 2.890 € |
| Eventfilm | 3.500 € |
| Recruiting-Video | 5.300 € |
| Imagefilm | 6.300 € |

### Zuschläge Einzelprojekte

| Zuschlag | Preis |
|---|---|
| Klassisch | 0 € |
| Motion Graphics | 550 € |
| Animation | 1.450 € |
| Drohnenaufnahmen | 350 € |
| Zweite Kamera | 470 € |
| Profi-Sprecher | 270 € |
| Untertitel / Captions | 170 € |
| Mehrformat-Export | 230 € |

## 3 — Dokumenten-CI (Angebote, Verträge, PDFs)

Alle Kundendokumente entstehen als HTML und werden mit Chrome headless nach PDF gedruckt
(`--headless --no-pdf-header-footer --print-to-pdf`). Aufbau immer gleich:

- **Kopf:** links `HAURER MEDIA` in Versalien, Sperrung 0.14em, „MEDIA" in Gold **#c8973f**;
  rechts die Dokumentart gesperrt in Grau. Darunter eine 2,5 px goldene Linie.
- **Schrift:** Helvetica Neue / Arial, 10–10,5 pt, Zeilenabstand 1,5. Fließtext im Blocksatz.
- **Parteien** nebeneinander in zwei gerahmten Kästen, Überschriften „ANBIETER" / „EMPFÄNGER"
  in Gold, gesperrt, 8,5 pt.
- **Eckdaten-Kasten:** dunkler Block **#141922**, Rahmen #2a3140, Beschriftungen in Gold
  **#eaa33c**, Preis groß in Gold. Dieser Kasten darf nie über einen Seitenumbruch reißen.
- **Positionstabellen:** graue Kopfzeile, dünne Linien #e2e5ea, Summenzeile dunkel mit
  goldenem Betrag, Beträge rechtsbündig.
- **Fuß:** dünne Linie, darunter Anschrift und Gültigkeit in 8 pt Grau.
- Unterschriftenzeilen nie allein auf eine letzte Seite rutschen lassen.

Vorlagen auf dem Mac: `~/Claude/haurer-media/angebot/`, `~/Claude/haurer-media/vertraege/`.

### Skript- und Ideen-PDFs für Kunden

Zwei Bauarten, beide Chrome-Headless aus HTML:

**Kurzform** (`~/Claude/skript_pdf.py`, für ein einzelnes Skript): Kopfzeile
`HAURER MEDIA · SKRIPT` in Blau **#1e3a5f**, darunter eine 3 px goldene Linie **#c8973f**.
Titel 26 px, Meta-Zeile (Kunde, Datum) grau. Abschnittsüberschriften in Versalien, gold,
mit goldenem Strich links. Fließtext 14,5 px.

**Lange Kundenfassung** (von Hand gebaut, Beispiele: MonBerg Ad-Skripte, proOffice
Themen-Ideen, Videoskripte): Kopf `HAURER.` / `MEDIA — VIDEO & SOCIAL MEDIA`, daneben eine
**Dokumentnummer** im Schema `JJJJ-MMTT-KÜRZEL-TYP` (z. B. `2026-0917-MB-E` für MonBerg
Entwurf, `2026-0904-PO-I` für proOffice Ideen). Darunter ein Kopfblock mit Kunde,
vollständiger Firmierung, Anschrift, Stand, Zweck und Umfang.

Danach in dieser Reihenfolge:

- **Konzept** — ein Absatz, der die Idee und die durchgehende Mechanik erklärt
  (wer spricht, wen er anspricht, welches Versprechen, welcher Schlusssatz).
- **Faktenblock** als Paare Begriff/Wert: Lage, Bereiche, Ausstattung, Verfügbarkeit,
  Anfahrt. Nur belegte Angaben — falsche Fakten sind hier schon passiert („Rheinblick",
  „höchster Punkt der Stadt") und mussten zurückgerufen werden.
- **Beim Dreh** — praktische Hinweise für den Drehtag, inklusive rechtlicher Punkte
  (erkennbare Gäste in Werbung brauchen eine Zusage).
- **Die Skripte** einzeln nummeriert (`AD 01`, `Skript 04`), je mit Hook, Sprechtext und CTA.
- Fehlende Angaben stehen ausdrücklich als **„Offen: …"** unter dem jeweiligen Punkt,
  nie als erfundene Zahl.

Ablage: `~/Claude/skripte/`, Dateiname `<Kunde>_<Art>_<Anzahl>_<Datum>.pdf`.
Skripte gehören zusätzlich ins CRM (`/api/scripts`) — aber **erst nach Freigabe**.

## 4 — Video- und Caption-Stil

**Devin-Jatho-Look** als Grundlage: Montserrat zweistufige Captions, Light Sweep über
Sonderwörter, Motion-Graphics (m², Etagen-Haus, Counter, Big-Word, Icon-Burst, Pin).
Kette: `style_clip.py` → `talkinghead_caption.py` → `add_audio.py`.

Regeln, die hart in der Engine stehen (nicht verhandelbar, weil sonst wieder verloren):

- **Maximal 4 Wörter je Caption-Block.** Fünf und mehr füllen das Bild.
- **Kein Block endet auf einem Füllwort** (Artikel, Präposition, Konjunktion, Hilfsverb);
  Zahlen bleiben bei ihrer Einheit.
- **Jedes Wort steht mindestens 0,55 s**, Mindeststandzeit je Block 0,8 s, notfalls mit
  Nachlauf bis 0,45 s hinter dem Ton. Abblende 0,16 s.
- **Nicht jeder Block fliegt ein**: bei Clips unter 20 s nur jeder dritte, sonst jeder zweite.
- **Abspann wird erkannt** (harter Schnitt ins Dunkle bis Clipende) — Captions, Emojis und
  Grafiken enden davor.
- **Emojis und Motion-Grafiken weichen der Schrift aus**; findet sich kein Platz, entfällt
  die Grafik lieber, als dass sie auf dem Text liegt.
- **Zähler zählen erst ab 10 hoch**, kleinere Zahlen stehen sofort.
- **Timer- und Countdown-Passagen nie anschneiden** (Watchtime). Cut-Zeiten per Frame prüfen.
- **Musikerkennung:** nur Takt-Autokorrelation zählt (> 0,30 = Beat). Pegel, Stille und
  Flachheit melden zweimal falsch „Musik". Atempausen erzeugen einen Pseudo-Takt.
- Pro Kunde eine **Stilkarte** in `~/.jarvis/caption_style/<Kunde>.json`: Wortlisten, Farben,
  Korrekturen, Renderwerte, Beat-Datei und -Lautstärke.

Marketing-Anglizismen mit **ihrem** Artikel: „**die** Hook".

## 5 — Posten

- Veröffentlicht wird über **Metricool**; `social_pipeline.py` lädt vorher auf das eigene
  Hosting (admin.haurer.de), Ausweichwege Catbox und Litterbox.
- **Videos werden neu remuxt** (Hash-Buster), **Bilder nicht** — sonst entstehen kaputte Dateien.
- **TikTok-Bilder höchstens 1080 px** breit. Größere Bilder bleiben stumm auf PENDING stehen.
- **Instagram-Karussell:** instagramData.type = "POST", Collab über das Feld collaborators
  (Liste aus username und deleted:false) — das kann die Schnittstelle.
- **Reels:** type = "REEL", YouTube immer type = "short" (sonst Querformat-Prüfung).
- **Sound aus TikTok oder Instagram lässt sich über Metricool nicht wählen.** Entweder Ton
  fest ins Video rendern oder als Erinnerung planen und in der App posten.
- Zeitangaben **immer in Europe/Berlin** rechnen, auch wenn der Rechner anders steht.

## 6 — Kunden

**Die Wahrheit steht im CRM auf admin.haurer.de, nicht in einer Liste.** Eine Kopie neben der
Wahrheit veraltet und führt zu Fehlern — genau das ist am 04.09.2026 passiert.

Abruf: GET https://admin.haurer.de/api/customers mit Bearer-Token (JARVIS_TOKEN).

Beim Abgleich wichtig: Das CRM führt **Personen**, die Lieferungen führen **Firmen**.
Die Brücke ist das Feld company (Bartosch → pro office, Musa → Monberg EVENT & BAR,
Mehmet → Smilance, Chris → Cafe New York).

## 7 — Harte Regeln

- **Passwörter, Logins, CAPTCHAs macht nur Harun selbst.** Nie über den Chat.
- **Konto-Erstellung verboten.**
- **Kundenpreise einzelner Bestandskunden niemals** in Anzeigen, Kaltakquise oder
  öffentlichen Antworten — nur Listenpreise.
- **Anzeigen werden nie automatisch gepostet**, nur nach Kundenfreigabe.
- **Keine .env mit echten Schlüsseln in ein Repository.**
- **Erst zeigen, dann hochladen.** Texte und Beiträge sieht Harun vor der Veröffentlichung.
- **Nichts erfinden.** Fehlt eine Angabe, steht „Offen: …" im Dokument statt einer Zahl.
- Regeln gehören als Constraint in die Engine, nicht nur in eine Wissensdatei.

## 8 — Gedächtnis aus den bisherigen Sitzungen

Die verlinkten Dateien liegen im Gedächtnis-Ordner auf dem Mac, nicht in diesem Repository.

- [Faceless-Business Research](project-faceless-business-research.md) — Deep Research 18.07.2026: E-Book-Idee gesättigt/gedeckelt; Empfehlung digitale Produkte über eigenen Checkout, Plattform nur als Traffic

- [JARVIS Lebens-Autopilot](project-jarvis-lebens-autopilot.md) — Block F Stand 16.07.: Tagesregie/Gym-Pakt/Nur-Anfangen/Multi-Konto-Rechnungswächter gebaut; offen Nr. 49; Scheduler-Zeiten-Vertrag
- [JARVIS Präsenz](project-jarvis-praesenz.md) — „fühlt sich wie ein Tool an": 17 von 35 proaktiven Momenten hingen an isAwake() (feuerten ~3 % der Zeit); Warteschlange + Anwesenheit über HIDIdleTime statt Kamera (spart ~12 $/Monat); Essens-Scanner; Kamera nur aus dem Terminal testbar
- [JARVIS lokale Modelle](project-jarvis-lokale-modelle.md) — localFirst war durch `hasHistory` tot (0 von 219 lokal), 31.07. repariert + Rauschfilter; nur 7 % der Spracheingaben sind echte Befehle → Türsteher ist das offene Problem, nicht das Modell
- [JARVIS Abo-Fallback](project-jarvis-abo-fallback.md) — bei leerem API-Guthaben arbeitet JARVIS über das Claude-Abo weiter (src/abo.ts + src/tool_cli.ts, 152 Tools erreichbar); ~10 s pro Antwort, Notbetrieb; braucht Neustart
- [JARVIS Lexware](project-jarvis-lexware.md) — seit 30.07. wieder live (Key nachgetragen); 63 offen/105k „überfällig", aber 0 bezahlte im Juli → Bankabgleich in Lexware prüfen, bevor gemahnt wird
- [JARVIS Bug-Audit 17.07.](project-jarvis-bugaudit.md) — 4-Agenten-Voll-Review + ~16 echte Bugs gefixt (Echo-Schluck, Hue-Crash, atomares Memory, ingest-Datenverlust, Doppel-Rechnung u.a.); Selbsttest 48/0; braucht Neustart
- [JARVIS Release-Audit 20.07.](project-jarvis-releaseaudit.md) — 4-Agenten-Audit, 38 Befunde: alle 5 HOCH gefixt (Crash-Schutz, History-Races, sqlite-Injection, Wecker-Nachholen, tote Orbit-Animation, Headless-Auto-Approve); Rest-Liste dokumentiert; braucht Neustart
- [JARVIS Dev-Requests](project-jarvis-devrequests.md) — Nacht-Batch 18.07.: Spotify-nicht-auto, Gute-Nacht-Szene, verkauft-TikTok, Skript-PDF, Auto-Thumbnail done; Monatsabschluss teilweise; 9 groß offen + 2 brauchen Harun
- [JARVIS Ideen-Archiv](project-jarvis-ideen-archiv.md) — ~/.jarvis/ideen.md, 104 Ideen (20.07.: +Block G Nutzen, H Deep-Probleme, I Wow-Animationen inkl. Holo-Globus); Trigger „Jarvis, Ideen"; Harun priorisiert
- [JARVIS Geister-Cutter](project-jarvis-geistercutter.md) — schneidet Talking-Head-Drehs autonom nachts (auto_editor→style_clip→Portal-Entwurf); Freigabe = Sicherheitsnetz; Scheduler 02:30 --scan
- [JARVIS Nachtschicht 23.07.](project-jarvis-nachtschicht-2307.md) — B-Roll-Bibliothek, Alltag komplett (#49/93/94/95), Deck-Wow komplett (8, inkl. Hand-Gesten), Ein-Satz-Video #125 (Beweis-Video!), Mission-Control #126, Set-Regie #128; 149 Tools; braucht Neustart
- [JARVIS Nachtschicht 21.07.](project-jarvis-nachtschicht.md) — 20 Builder-Agenten: 19 neue Tools (Wächter, Prognose, Krisen-Schild, Lead-Röntgen, Case-Study, Foto-Ernte, Disk-Autopilot 365GB, …) + Holo-Globus + Transfer-Kino; 133 Tools verdrahtet; Befunde: Floresia-TikTok tot, Lexware-Key fehlt, TCC-Sperren
- [JARVIS Stimmerkennung](project-jarvis-stimmerkennung.md) — Sprecher-Verifikation ging beim Parakeet-Umstieg verloren, 21.07. nachgerüstet + bewiesen; offen: Harun macht `npm run enroll` (15s) + Neustart; Schwelle 0.65, Debug via JARVIS_VOICE_DEBUG
- [JARVIS Mitdenken](project-jarvis-mitdenken.md) — Kernwunsch 20.07.: Fähigkeiten-Concierge + Gesprächsfäden + Mitdenk-Momente 11:15/17:30 + Stimmung lesen; gebaut v1, braucht Neustart; Design-Prinzip: JARVIS bietet an, Harun muss nichts kennen
- [JARVIS Wow-Backlog](project-jarvis-wow-backlog.md) — freigegebene Ideen: Holo-Hand-Gestensteuerung (A/B/C), Holo-Desktop-Modus, Renderwatch, Sonnenaufgang, Fokus-Modus u.a.

- [Blender-Renderfarm (RTX 5090)](project-blender-renderfarm.md) — foto-realistische 3D-Auto-Animationen vom Mac per SSH auf den Gaming-PC dispatchen; Revuelto-Assembly (853 Teile), HDRI+AgX+OIDN, Kino-Post per ffmpeg

- [Harun Gür / Haurer Media](user-harun-haurer-media.md) — who the user is: owner of a video production agency
- [Haruns Alltagsprobleme](user-harun-alltag-probleme.md) — Essen/Auftauen, Rechnungen→Inkasso, Gebete, Prokrastination, Kalender leer; Basis für Lebens-Autopilot (ideen.md Block F)
- [Haurer website rebuild](project-haurer-website-rebuild.md) — new Astro site replacing the old Webflow haurer.de
- [JARVIS voice assistant](project-jarvis-voice-assistant.md) — Mac voice assistant side project; M0 core loop, next is wake word
- [JARVIS Kalender](project-jarvis-calendar.md) — eigene Monatsansicht über macOS-Kalender; David-Schicht-PDF-Import offen (braucht Beispiel-PDF)
- [JARVIS + DaVinci Resolve](project-jarvis-resolve.md) — Resolve Python scripting API live-confirmed; basis for video-edit automation; Auto-Cut (pauses) built
- [JARVIS latency fixes](project-jarvis-latency.md) — Parakeet STT (~75ms listen) + leaner Edge TTS; needs npm restart
- [JARVIS Karten-Workflow](project-jarvis-card-workflow.md) — clean_card (Duplikate löschen) + sort_card (Dreh-Cluster + VLM-Votum, Frage pro Dreh)
- [JARVIS Türsensor](project-jarvis-door-sensor.md) — Hue-Bewegungsmelder Eingang: Ankunft-Briefing (Logik 1) + wer-kam-rein David/Nazli (Logik 2)
- [Metricool integration](project-metricool-integration.md) — MCP set up & live-tested; post local-folder videos to the right client
- [Gemini video analysis](project-gemini-video-analysis.md) — set up & working; watch local videos, transcribe, write captions
- [Jargon-Artikel](feedback-jargon-artikel.md) — Harun will „die Hook" (nicht „der Hook"); engl. Marketing-Begriffe mit seinem Artikel
- [Marketing-Skills](project-marketing-skills.md) — Corey Haines' 64-Skill-Pack installiert + mit Haurer-Kontext (.agents/product-marketing.md) gefüttert; Kundenliste mit Branchen
- [JARVIS next features](project-jarvis-next-features.md) — Video-Coach ✓, Self-Dev-Loop ✓, Ausbau-Paket 04.07. ✓ (Sonnet, Wake-Word, Kunden-Reports, Angebots-PDF, Reschedule, Meeting-Briefing, Digest)
- [JARVIS Fitness & Tagesplaner](project-jarvis-fitness-planner.md) — geplant: Supplement-Motivator, Kamera-Protein-Tracker (foods.json), Tagesplaner über mehrere Quellen; CarPlay-UI unrealistisch (nur Sprache)
- [JARVIS Persona](project-jarvis-fitness-planner.md) — persönlichkeit frei editierbar in ~/.jarvis/persona.md (live, Film-JARVIS-Ton)
- [JARVIS Ex-Kunden](project-jarvis-exkunden.md) — Namen steckten in memory.md (wird ganz in den Prompt geladen), in ~30 Werkzeug-Beispielen, in fest verdrahteten Metricool-BRANDS-Maps und in der posted_log-Vereinigung; Fix = Kundensperre am Prompt-Ende, live aus dem CRM
- [Kundenquelle = CRM](project-kunden-quelle.md) — seit 18.08.2026 sagt nur noch admin.haurer.de, wer Kunde ist; JARVIS zieht stündlich, lokale Dateien führen keine Kundenliste mehr
- [Haurer Admin-App](project-haurer-admin.md) — internes Next.js CRM (~/Claude/haurer-admin): Login Harun+David, Kunden, Skripte (JARVIS-Upload), Todos, Apollo.io-Sync
- [JARVIS Command Deck](project-jarvis-deck.md) — Vollbild-Film-HUD (npm run deck); Vorgabe: Iron-Man-FUI-Stil, Original-Kern, KEINE Spielgrafik; Kunden als Dossier-Mappe
- [Talkinghead-Stil](project-talkinghead-stil.md) — Devin-Jatho-Look: Montserrat 2-Tier-Text + Light Sweep + Motion-Graphics (m², Etagen-Haus); Stilkarten pro Kunde
- [Lead-Magnet Immobilien](project-leadmagnet-immobilien.md) — Playbook-Funnel KOMPLETT (22.07.): Immobilien- + NEU Autohaus-Playbook (je 11 S., leadmagnet-autohaus/), 2 Astro-LPs (/playbook, /autohaus-playbook), Lead-Endpoint /api/leadmagnet LIVE auf admin (CRM-Anbindung + Honeypot + Consent, live getestet), PDFs auf admin/downloads/…h7k2x9/…m3q8w1; Sequenz um Playbook-Slots ergänzt; offen: Website-Deploy (Haruns SFTP) + Nurture-Mails + Test-Lead löschen
- [Wachstumsplan 2026](project-wachstumsplan-2026.md) — 16.08.: gesichert 11.750 € (MonBerg inzwischen Kunde — Zahl überholt), pro office 40 % Klumpenrisiko; 50k nicht in 12 Monaten sondern Monat 30–36, realistisch 26–30k; Engpass ist der fehlende Vertrieb, nicht das Werkzeug; pro office + Smilance nicht anfassen, Instantly nicht scharf schalten
- [Haurer Vertrieb](project-haurer-vertrieb.md) — Ads-Umbau 22.07.: Playbook-Kampagnen Makler+Autohaus live (je 10€/Tag, Conversions), NRW-Kampagne pausiert (420€/0 Leads), 250€+400€ Gutscheine, Negativ-Keywords überall; Warmup läuft → Kaltversand ~Anfang August
- [Sonnet-5 Thinking-Falle](reference-sonnet5-thinking-default.md) — claude-sonnet-5 denkt per Default → frisst kleine max_tokens auf → leerer Text; Fix `thinking: disabled` (sonnet-4-6 nicht betroffen)
- [Schnitt & Watchtime](feedback-schnitt-watchtime.md) — nie Watchtime-Passagen (Timer) anschneiden; Cut-Zeiten per Frame-Check verifizieren; Beat 0.42
- [Safe-Zone im Code erzwingen](feedback-safezone-im-code.md) — Regeln gehören als Constraint in die Render-Engine, nicht nur in Wissensdateien
- [Smilance Terminbuchung](project-smilance-buchung.md) — Buchungsseite + Admin in haurer-admin (nicht als Artifact: keine geteilte Speicherung); 3 CSS/React-Bugs dokumentiert
- [Preisanpassung 2026](project-preisanpassung-2026.md) — Marktrecherche 28.07.: Pakete deutlich unter Marktwert, neue Leiter (2.990/3.990/4.790/6.990) fertig, Einführung bis nach dem pro-office-Termin aufgeschoben
- [Werkbank (Video-Stil-Analyse)](project-werkbank.md) — Referenzvideo → benanntes Stil-Rezept → auf eigenes Rohvideo anwenden; in haurer-admin, Runner-Pattern weil der Server nicht rendern kann; Wortschatz=Kunde, Look=Rezept; jedes Feld trägt seine Sicherheit
- [Korrektur-Kurve](project-korrektur-kurve.md) — Messlatte für JARVIS-Intelligenz: 10,1 % Korrekturquote, fällt nicht; Faktor 5 zwischen Schnitt (13,7 %) und Code (2,6 %) = wo die Wirklichkeit urteilt vs. nur Harun; Geschmacks-Gedächtnis in ~/Claude/jarvis/geschmack
- [Musikerkennung im Rohclip](feedback-musikerkennung.md) — Pegel/Stille/Flachheit sagen zweimal falsch „Musik"; nur Takt-Autokorrelation zählt (>0,3 = Beat); bei lauter Atmo JARVIS_BEAT_VOL=0.55 statt Kartenwert
- [Regie-Pass gesperrt](project-regie-pass-gesperrt.md) — Motion-Design fällt aus: API-Guthaben leer (antwortet mit 400, nicht 401) + claude-CLI-Login abgelaufen; Ersatz JARVIS_REGIE_PLAN; Harun muss einloggen
- [haurer-admin deployen](project-haurer-admin-deploy.md) — `railway up`, NICHT GitHub (Push löst nichts aus); vor Schemaänderungen `node scripts/sicherung.mjs`, sonst leert db push Tabellen (16.08. Skripte verloren, kein Restore im Hobby-Tarif)
- [Resolve Text-Plugin](project-resolve-textengine.md) — ~/Claude/resolve-textengine: Transkript→Text-Effekte in der Safe Zone; enthält die harten Resolve-21-API-Grenzen (Titel immer V1, kein SetDuration, Macros nur via ImportFusionComp, GetLeftOffset in Quell-FPS)
- [Sprachassistent 2026](project-sprachassistent-2026.md) — Neubau ab 28.08.2026, JARVIS explizit verworfen; 25 Recherchen in ~/Claude/voice-research/; Ziel gedreht: nicht 300ms jagen, sondern nie unterbrechen + früher anfangen
- [Büro B1.03 Umbau](project-buero-b103-umbau.md) — Walnuss/BESTÅ-Raumgestaltung 08.09.2026 als Artifact; Türzuordnung geklärt (GLASSVIK 60×38 auf 120×38, HEDEVIKEN 60×64); Raummaße geschätzt, Harun misst nach
- [Higgsfield Upload-Workaround](reference-higgsfield-upload-workaround.md) — `generate create --image <pfad>` scheitert an S3-Signatur; erst `upload create`, dann UUID übergeben
- [Statistik-Scheduler](project-statistik-scheduler.md) — Portal-Zahlen waren 24 Tage tot (JARVIS-Scheduler weg + Metricool-Datumsformat, Fehler still geschluckt); seit 14.09.2026 launchd + Exit 1 bei Fehlschlag
- [proOffice Karussells](project-prooffice-karussells.md) — Referenzstil aus dem Gastfreundschaft-Post; KI-Hintergründe abgelehnt, echte Standortfotos aus ~/Downloads/Objekte, Bild muss zum Standort des Themas passen

---

Wenn du etwas nicht weißt: nachfragen oder nachsehen, nicht raten.
