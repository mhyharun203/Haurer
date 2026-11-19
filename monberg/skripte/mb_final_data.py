import os, runpy
_A = runpy.run_path(os.path.join(os.path.dirname(__file__), 'mb_ideen_data.py'))
_ALT = {k['nr']: k for b in _A['BLOECKE'] for k in b['skripte']}


def K(nr, titel, tags, hook, ablauf, ending, vorbereitung, alt_ending=None):
    return dict(nr=nr, titel=titel, tags=tags, hook=hook, ablauf=ablauf, ending=ending, alt=alt_ending, vorb=vorbereitung)


def ALT(alt_nr, neu_nr):
    return dict(_ALT[alt_nr], nr=neu_nr)


KOPF = 'MonBerg · Drehskripte · Kundenfassung · Stand 19.11. · 2026-1119-MB-D'
TITEL = 'MonBerg · Drehskripte'
UNTER = 'KUNDENFASSUNG · 17 KURZFORMATE ZUM VORLESEN · STAND 19.11.2026'
ABLAUF_LAB = 'Sprechtext zum Vorlesen / Ablauf'
REIHE_H = ('BLOCK', 'SKRIPTE', 'ZEIT')

INTRO = [_A['INTRO'][0], _A['INTRO'][1], _A['INTRO'][2],
    ('Requisiten',
     'Pappschilder mit den Zahlen 1–10 (zwei Sätze) · dicker Stift · Stoppuhr oder Handy mit Timer · eine Mappe und ein Kugelschreiber · '
     'ein Zettel als Sitzplan · ein Handy mit Lautsprecher für den Anruf · drei Karten mit den Zahlen 1, 2 und 3 · eine Handvoll Konfetti · '
     'ein Mikrofon für die Geräusche in Skript 17.'),
]
LOOKS = [
    ('Team 1 und Team 2', 'Arbeitskleidung, wie das Team bei einer Veranstaltung aussieht', 'Alle Skripte. Bei den Serien immer gleich, damit man sie wiedererkennt.'),
    ('Gast', 'Alltagskleidung eines Besuchers, Jacke an', 'In 07 und 14 ist der Gast nur als Stimme zu hören.'),
]
LOOK_HINWEIS = _A['LOOK_HINWEIS']

REIHENFOLGE_TEXT = ('Drei Blöcke, nach Orten sortiert, damit nichts umgebaut werden muss. Draußen zuerst, solange das Licht gut ist. '
                    'Die Geräusche für 17 werden nebenbei in jedem Block aufgenommen. Gesamt etwa 2 Stunden 30 Minuten mit Pausen.')
REIHENFOLGE = [
    ('Block 1 · Eingang & Wintergarten', '01 Ist das hier der Eingang? · 02 Kann ich hier mal kurz telefonieren? · 03 Sätze, die wir jede Woche hören · 04 Was er sagt, was er meint · 05 Der Blick · 06 Ausreden vs. MonBerg · 07 Der Anruf', 'ca. 55 Min.'),
    ('Block 2 · Eisstockbahn & Strand', '08 Die Jury · 09 Erklär mir … in 10 Sekunden · danach 10 Minuten am MonStrand für die Gegenschnitte aus 05 und die Strand-Geräusche aus 17', 'ca. 35 Min.'),
    ('5 Min. Pause', 'Kein Outfitwechsel.', ''),
    ('Block 3 · Bar & Tische', '10 Der Sitzplan · 11 Die Ja-Wort-Probe · 12 Event-Deutsch, Deutsch-Event · 13 Unpopuläre Meinung · 14 Schnellfragerunde · 15 3 Dinge vor der Firmenfeier · 16 Wer zuerst lacht · 17 Hör mal, wo wir sind (Abschluss)', 'ca. 55 Min.'),
    ('Wenn die Zeit knapp wird', 'Zuerst drehen: 01, 02, 03, 06, 08, 12, 13. Diese tragen die Serien und die meisten Fakten.', ''),
]
KLAEREN = []
BLOECKE = []


def B(banner, text, *skripte):
    BLOECKE.append(dict(banner=banner, text=text, skripte=list(skripte)))


B('BLOCK 1 · EINGANG & WINTERGARTEN', 'Team 1, Team 2, Gast · Skripte 01–07 · ca. 55 Minuten. Start des Drehs, solange das Licht gut ist.',
  ALT('01', '01'), ALT('06', '02'),
  K('03', 'Sätze, die wir jede Woche hören', 'Serie · Sketch · 8–12 s je Folge · Team 1, Team 2, Gast',
    'Gast: „Wir sind so ca. 100 Leute.“',
    ['Team 1 und Team 2 stehen mit der Mappe am Eingang. Der Gast sagt einen Anfrage-Klassiker, das Team reagiert trocken, fast ohne Worte. Jede Folge ist ein eigener Clip.',
     'Folge 1 · Gast: „Wir sind so ca. 100 Leute.“ · Team 2 nickt freundlich und schreibt in die Mappe. Nah auf die Mappe: „140“.',
     'Folge 2 · Gast: „Das Wetter wird schon.“ · Team 1 zeigt wortlos Richtung Wintergarten. Einblendung: „Überdacht.“',
     'Folge 3 · Gast: „Wir wollen was ganz Entspanntes. Nicht so lang.“ · Team 2 schreibt in die Mappe. Nah: „bis 3 Uhr“.',
     'Folge 4 · Gast: „Die Rede vom Chef ist ganz kurz.“ · Team 1 und Team 2 gleichzeitig: „Mhm.“',
     'Folge 5 · Gast: „Wir sagen euch bis morgen Bescheid.“ · Team 2 klappt die Mappe zu, Team 1 schaut auf die Uhr.'],
    'Reaktion des Teams → kurzer Blick in die Kamera → Cut. Einblendung: „Welchen Satz hört ihr am häufigsten?“',
    'Alle Folgen mit derselben Einstellung drehen: Gast nah, dann Gegenschnitt auf das Team. Die Zahlen in der Mappe vorher mit dickem Stift vorschreiben, damit sie im Bild lesbar sind. Freundlich bleiben, das Team macht sich nie über den Kunden lustig, es kennt ihn nur gut.'),
  ALT('03', '04'), ALT('04', '05'), ALT('05', '06'),
  K('07', 'Der Anruf', 'Serie · Sketch · 10–15 s je Folge · Team 1, Team 2, Gast als Stimme',
    'Gast am Telefon: „Hi, wir bräuchten was für morgen. So 200 Leute.“',
    ['Team 1 nimmt einen Anruf an und stellt auf Lautsprecher. Team 2 steht daneben mit der Mappe. Der Gast ist nur als Stimme zu hören.',
     'Folge 1 · Gast: „Hi, wir bräuchten was für morgen. So 200 Leute.“ · Team 1 schaut langsam zu Team 2. · Team 1: „Morgen?“ · Gast: „Oder übermorgen. Wir sind flexibel.“ · Team 2 lehnt sich zurück und atmet aus. · Team 1: „Ich ruf Sie gleich zurück.“',
     'Folge 2 · Gast: „Hi, wir wollten für die Weihnachtsfeier anfragen. Für nächstes Jahr.“ · Team 1 und Team 2 schauen sich an. Team 2 legt die Hand aufs Herz. · Team 2: „Endlich mal jemand früh dran.“',
     'Folge 3 · Gast: „Habt ihr noch Platz für die ganze Firma?“ · Team 1: „Wie viele seid ihr?“ · Gast: „Alle.“ · Team 2: „Bis zu 1.500 Gäste.“ · Gast, nach einer Pause: „… dann sind wir zu wenige.“'],
    'Team 1 legt auf, beide schauen in die Kamera → Cut.',
    'Die Stimme des Gastes wird separat sauber eingesprochen und im Schnitt über den Lautsprecher-Ton gelegt. Im Bild nur das Team: Halbnah auf beide, Handy flach in der Hand von Team 1. Folge 2 ist die Botschaft, früh anzufragen, ohne sie auszusprechen.'),
)

B('BLOCK 2 · EISSTOCKBAHN & STRAND', 'Team 1, Team 2, Gast · Skripte 08–09 · ca. 35 Minuten. Requisiten: Pappschilder, Stoppuhr. Danach kurz zum MonStrand für Gegenschnitte und Geräusche.',
  ALT('07', '08'), ALT('09', '09'),
)

B('5 MIN. PAUSE · BLOCK 3 · BAR & TISCHE', 'Team 1, Team 2, Gast · Skripte 10–17 · ca. 55 Minuten.',
  K('10', 'Der Sitzplan', 'Sketch · 20–25 s · Team 1, Team 2, Gast',
    'Gast mit Zettel: „Also. Sitzplan.“',
    ['Team 1 und Team 2 sitzen an einem Tisch, Team 2 mit Mappe und Kugelschreiber. Der Gast spielt den Kollegen aus dem Orga-Team und liest von einem Zettel.',
     'Gast: „Also. Sitzplan. Vertrieb nicht neben Buchhaltung.“ · Team 2 nickt und schreibt.',
     'Gast: „Marketing nicht neben IT, die reden sonst nur über Passwörter.“ · Team 2 schreibt weiter.',
     'Gast: „Und Jürgen nicht neben Jürgen.“ · Team 1: „Wie viele Jürgens habt ihr?“ · Gast: „Vier.“',
     'Gast: „Der Chef in die Mitte. Nein, doch nicht. An den Rand. Nein, doch in die Mitte …“',
     'Team 1 und Team 2 schauen sich an. Team 2, ganz ruhig: „Wie wär’s mit freier Platzwahl?“',
     'Der Gast lässt den Zettel sinken, schaut die beiden lange an: „… ihr seid Genies.“'],
    '„Ihr seid Genies.“ → Gast zerknüllt den Zettel → Cut.',
    'Gast nah, das Team im Gegenschnitt. Die Namen sind Beispiele und dürfen gegen andere getauscht werden, nur keine echten Kunden- oder Mitarbeiternamen. Ein Tisch, der schon steht, reicht völlig.'),
  ALT('17', '11'),
  K('12', 'Event-Deutsch, Deutsch-Event', 'Serie · Direkt in die Kamera · 15–20 s · Team 1, Team 2',
    'Einblendung: „Event-Deutsch → Deutsch“',
    ['Team 1 und Team 2 stehen nebeneinander an der Bar und schauen in die Kamera. Team 1 sagt den Begriff, Team 2 übersetzt trocken. Pro Clip drei bis vier Begriffe.',
     'Team 1: „Get-together.“ · Team 2: „Alle stehen am Buffet.“',
     'Team 1: „Lockerer Ausklang.“ · Team 2: „Bis drei Uhr.“',
     'Team 1: „Kurze Begrüßung.“ · Team 2: „Zwanzig Minuten.“',
     'Team 1: „Dresscode casual.“ · Team 2: „Einer kommt trotzdem im Anzug.“',
     'Team 1: „Open End.“ · Team 2: „Der Vertrieb geht als Letzter.“',
     'Team 1: „Wir halten es klein.“ · Team 2: „Die ganze Firma kommt.“',
     'Team 1 zum Schluss: „Welches fehlt?“'],
    '„Welches fehlt?“ → Cut. Die Antworten aus den Kommentaren werden die nächste Folge.',
    'Alle Paare am Stück drehen, im Schnitt auf zwei Clips verteilen. Beide schauen immer in die Kamera, nie zueinander. Kurze Pause zwischen Begriff und Übersetzung, die Pointe braucht den Moment.'),
  ALT('14', '13'),
  K('14', 'Schnellfragerunde', 'Tempo-Format · Serie · 15–20 s · Team 1 oder Team 2, Gast als Stimme',
    'Gast aus dem Off: „Schnellfragerunde. Nicht nachdenken.“',
    ['Team 1 steht vor der Kamera. Der Gast fragt aus dem Off in hohem Tempo, Team 1 antwortet ohne Pause. In Folge 2 steht Team 2 vor der Kamera.',
     'Gast: „Schnellfragerunde. Nicht nachdenken.“',
     'Gast: „Strand oder Garten?“ · Team 1: „Ja.“',
     'Gast: „Glühwein oder Cocktail?“ · Team 1: „Erst das eine.“',
     'Gast: „Rede lang oder kurz?“ · Team 1: „Gar nicht.“',
     'Gast: „Wie viele Gäste?“ · Team 1: „Bis zu 1.500.“',
     'Gast: „Und wenn’s regnet?“ · Team 1: „Wintergarten.“',
     'Gast: „Kann man hier heiraten?“ · Team 1: „Standesamt-Location.“',
     'Gast: „Lieblingsmonat?“ · Team 1: „Der, in dem ihr bucht.“'],
    '„Der, in dem ihr bucht.“ → kurzes Lächeln → Cut.',
    'Fragen und Antworten werden einzeln gedreht und im Schnitt eng aneinandergesetzt, so entsteht das Tempo. Die Fragen sauber separat einsprechen. Gleicher Bildausschnitt für die ganze Runde.'),
  K('15', '3 Dinge, die du vor der Firmenfeier klären solltest', 'Nutzwert · Direkt in die Kamera · 25–30 s · Team 1, Team 2',
    'Team 1: „Drei Dinge, die du klären solltest, bevor du die Firmenfeier planst.“',
    ['Team 1 spricht in die Kamera, Team 2 steht daneben und hält jeweils die Karte mit der Zahl hoch.',
     'Team 1: „Drei Dinge, die du klären solltest, bevor du die Firmenfeier planst.“',
     'Team 2 hält die 1 hoch. · Team 1: „Die ehrliche Gästezahl. Mit Partnern, mit allen, die ‚vielleicht‘ gesagt haben.“',
     'Team 2 hält die 2 hoch. · Team 1: „Den Plan B fürs Wetter. Bei uns ist das der überdachte Wintergarten.“',
     'Team 2 hält die 3 hoch. · Team 1: „Wie alle wieder nach Hause kommen. Das klärt man vorher, nicht um eins nachts.“',
     'Team 2: „Und dann: früh anfragen.“'],
    '„Und dann: früh anfragen.“ → beide nicken in die Kamera → Cut.',
    'Ruhig und kompetent sprechen, das ist der seriöse Clip zwischen den Sketchen. Halbnah, beide im Bild. Die Zahlenkarten vorher mit dickem Stift schreiben.'),
  ALT('15', '16'),
  K('17', 'Hör mal, wo wir sind', 'Ton-Rätsel · Serie · 15–20 s je Folge · Team 1',
    'Einblendung: „Augen zu. Wo am MonBerg sind wir?“',
    ['Nur Geräusche, das Bild ist anfangs schwarz oder sehr nah. Jedes Geräusch steht drei Sekunden allein, dann kommt die Auflösung im Bild. Pro Folge vier Geräusche.',
     'Folge 1 · Ein Eisstock gleitet über die Bahn und klackt → Eisstockbahn · Schritte im Quarzsand → MonStrand · Gläser stoßen an → Bar · Regen aufs Dach des Wintergartens → Wintergarten.',
     'Folge 2 · Ein Liegestuhl wird aufgeklappt → MonStrand · Eiswürfel fallen ins Glas → Bar · Wind in den Palmen → MonStrand · Mikrofon-Check „eins, zwei“ → Eventfläche.',
     'Folge 3 · Ein Cocktail-Shaker → Bar · Ein Kronkorken springt ab → Bar · Ein Stuhl wird über den Boden geschoben → Wintergarten · Eine Kaffeemaschine → Teamküche.',
     'Team 1 zum Schluss in die Kamera: „Wer alle vier erkannt hat: ab in die Kommentare.“'],
    '„Ab in die Kommentare.“ → Cut.',
    'Geräusche nebenbei in jedem Block aufnehmen, Mikrofon nah an der Quelle, je 10 Sekunden. Vor Ort prüfen, was es wirklich gibt, und nur echte Geräusche verwenden. Der Regen nur, wenn es am Drehtag regnet, sonst durch ein anderes Geräusch ersetzen. Im Schnitt erst Ton, dann Bild, nie umgekehrt.'),
)

for _b in BLOECKE:
    for _k in _b['skripte']:
        _k['vorb'] = _k['vorb'].replace('in Block 1 und 3 mitnehmen', 'in Block 1 und 2 mitnehmen')
