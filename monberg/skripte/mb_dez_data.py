import os, runpy
_F = runpy.run_path(os.path.join(os.path.dirname(__file__), 'mb_final_data.py'))
_S = {k['nr']: k for b in _F['BLOECKE'] for k in b['skripte']}


def S(alt, neu, ad):
    k = dict(_S[alt], nr=neu, ad=ad)
    k['vorb'] = k['vorb'].replace('Gleiche Einstellung wie 01', 'Gleiche Einstellung wie 05')
    return k


KOPF = 'MonBerg · Drehskripte Dezember · Kundenfassung · Stand 19.11. · 2026-1119-MB-D'
TITEL = 'MonBerg · Drehskripte Dezember'
UNTER = 'KUNDENFASSUNG · 4 ADS · 8 ORGANISCH · 5 OPTIONAL · STAND 19.11.2026'
ABLAUF_LAB = _F['ABLAUF_LAB']
REIHE_H = _F['REIHE_H']

INTRO = [
    ('Schlüsselung für Dezember',
     'Laut Angebot 2026-0808-MB-B sind 8 organische Videos und 4 Ads gebucht. Aus den 17 Skripten sind deshalb zuerst die 4 Videos mit dem höchsten '
     'Adpotenzial gesetzt (01–04), danach die 8 stärksten organischen (05–12). Die übrigen 5 stehen am Schluss als optional (13–17): Sie werden gedreht, '
     'wenn am Drehtag Zeit bleibt, und gehen als Reserve in den Pool.'),
    ('Woran Adpotenzial gemessen ist',
     'Eine Ad läuft bei Menschen, die den MonBerg und unsere Serien nicht kennen. Sie muss deshalb ohne Vorwissen funktionieren, in der ersten Sekunde '
     'zeigen, worum es geht, mehrere belegte Fakten tragen (Fläche, Gästezahl, Wintergarten, Strand, Standesamt) und mit einer klaren Aufforderung enden. '
     'Jedes Skript trägt seine Einstufung: hoch, mittel oder gering. Die Ads werden erst nach Freigabe durch MonBerg geschaltet.'),
    _F['INTRO'][1],
    _F['INTRO'][3],
]
LOOKS = [
    _F['LOOKS'][0],
    ('Gast', 'Alltagskleidung eines Besuchers, Jacke an', 'In 03 und 08 ist der Gast nur als Stimme zu hören.'),
]
LOOK_HINWEIS = _F['LOOK_HINWEIS']

REIHENFOLGE_TEXT = ('Gedreht wird weiter nach Orten, damit nichts umgebaut werden muss. In jedem Block zuerst die Vertragsvideos 01–12, '
                    'die optionalen 13–17 nur, wenn Zeit bleibt.')
REIHENFOLGE = [
    ('Block 1 · Eingang & Wintergarten', '01 Ausreden vs. MonBerg · 05 Ist das hier der Eingang? · 06 Kann ich hier mal kurz telefonieren? · 07 Sätze, die wir jede Woche hören · 08 Der Anruf · optional 13 Was er sagt, was er meint · 14 Der Blick', 'ca. 40–55 Min.'),
    ('Block 2 · Eisstockbahn & Strand', '09 Die Jury · optional 15 Erklär mir … in 10 Sekunden · danach 10 Minuten am MonStrand für Gegenschnitte und Geräusche', 'ca. 25–35 Min.'),
    ('5 Min. Pause', 'Kein Outfitwechsel.', ''),
    ('Block 3 · Bar & Tische', '02 Die Ja-Wort-Probe · 03 Schnellfragerunde · 04 3 Dinge vor der Firmenfeier · 10 Der Sitzplan · 11 Event-Deutsch, Deutsch-Event · 12 Unpopuläre Meinung · optional 16 Wer zuerst lacht · 17 Hör mal, wo wir sind', 'ca. 45–55 Min.'),
    ('Nur Vertragsvideos', 'Ohne die optionalen Skripte reichen etwa 2 Stunden.', ''),
]
KLAEREN = []
BLOECKE = []


def B(banner, text, *skripte):
    BLOECKE.append(dict(banner=banner, text=text, skripte=list(skripte)))


B('DEZEMBER · ADS · 4 VON 4', 'Die vier Skripte mit dem höchsten Adpotenzial. Funktionieren ohne Vorwissen, tragen belegte Fakten und enden mit einer klaren Aufforderung.',
  S('06', '01', ('hoch',
    'Fünf belegte Fakten in 25 Sekunden, jede Ausrede ist ein Einwand, den echte Entscheider haben (Platz, Wetter, Konferenzraum). Der Schluss ist lustig, ohne die Botschaft zu verwässern.',
    'Hook in der ersten Sekunde: „Ich hab echt keine Lust auf die Weihnachtsfeier.“ Jeder Konter mit Fakt als Einblendung. Am Ende Einblendung „Firmenfeier am MonBerg · Jetzt anfragen“. Im Frühjahr dieselbe Ad als Sommerfest-Fassung.')),
  S('11', '02', ('hoch',
    'Spricht zwei Zielgruppen zugleich an, Firmen und Brautpaare, und trägt den stärksten Alleinstellungsfakt: offizielle Standesamt-Location. Die Pointe versteht man ohne Vorwissen.',
    'Mit der Frage „Wollt ihr …?“ als Hook beginnen, Einleitung kürzen. Zwei Fassungen ausspielen: Firmenfeier (wie im Skript) und Hochzeit („Wollt ihr hier heiraten?“ – „Ja.“). Schluss-Einblendung „Offizielle Standesamt-Location · Jetzt Termin anfragen“.')),
  S('14', '03', ('hoch',
    'Das schnellste Format mit den meisten Fakten: Strand, Garten, bis zu 1.500 Gäste, Wintergarten, Standesamt. Das Tempo hält die Leute im Video, der letzte Satz ist schon die Aufforderung.',
    'Auf 12–15 Sekunden schneiden, nur die Faktenfragen und „Lieblingsmonat?“ – „Der, in dem ihr bucht.“ Jede Antwort zusätzlich als Einblendung.')),
  S('15', '04', ('hoch',
    'Echter Nutzwert für genau die Person, die die Feier organisiert. Baut Vertrauen auf, bevor der MonBerg vorkommt, und endet mit „früh anfragen“.',
    'Für Planer von Sommerfesten und der nächsten Weihnachtsfeier. Die drei Punkte als Einblendung mitlaufen lassen. Schluss-Einblendung „Jetzt früh anfragen“.')),
)

B('DEZEMBER · ORGANISCH · 8 VON 8', 'Die acht stärksten Formate für den organischen Feed: Serien, Wiedererkennung, Kommentare.',
  S('01', '05', ('gering', 'Der Witz lebt von der Serie „Kurze Frage“, für Fremde fehlt der Zusammenhang. Organisch stark als vorletzte Folge.', None)),
  S('02', '06', ('gering', 'Abschluss der Serie, ohne Vorwissen schwächer. Organisch die logische letzte Folge.', None)),
  S('03', '07', ('mittel', 'Trifft Planer sehr genau, trägt aber kaum Fakten. Gut als Serie, als Ad nur Reserve.', None)),
  S('07', '08', ('mittel', 'Folge 2 („Endlich mal jemand früh dran“) und Folge 3 („Bis zu 1.500 Gäste“) taugen als Reserve-Ad, Folge 1 nur organisch.', None)),
  S('08', '09', ('gering', 'Unterhaltung mit Eisstock, kein Fakt und keine Aufforderung. Organisch stark, passt zur Saison.', None)),
  S('10', '10', ('mittel', 'Das Weihnachtsfeier-Thema des Monats, trifft das Orga-Team genau. Ohne Fakt, deshalb organisch.', None)),
  S('12', '11', ('gering', 'Ein Kommentar-Format: Die Stärke ist die Frage „Welches fehlt?“, nicht der Verkauf.', None)),
  S('13', '12', ('gering', 'Ein Kommentar-Format mit vielen kurzen Folgen, ideal für einen regelmäßigen Rhythmus im Feed.', None)),
)

B('OPTIONAL · NUR WENN ZEIT BLEIBT', 'Werden am Drehtag nur gedreht, wenn nach den Vertragsvideos Zeit bleibt. Gehen als Reserve in den Pool.',
  S('04', '13', ('mittel', 'Trägt den Fakt „bis zu 1.500 Gäste“, die Pointe hängt aber an den Einblendungen. Überschneidet sich mit 07.', None)),
  S('05', '14', ('mittel', 'Jede Folge zeigt einen Fakt, ist mit 6–8 Sekunden aber zu kurz für eine eigenständige Ad.', None)),
  S('09', '15', ('mittel', 'Folge 2 („Erklär mir den MonBerg“) trägt viele Fakten, die anderen Folgen sind Unterhaltung.', None)),
  S('16', '16', ('gering', 'Reine Unterhaltung, lebt von echten Lachern am Set.', None)),
  S('17', '17', ('gering', 'Ein Interaktions-Format für Kommentare, ohne Aufforderung zur Anfrage.', None)),
)
