import os, runpy
_D = runpy.run_path(os.path.join(os.path.dirname(__file__), 'mb_dez_data.py'))
_S = {k['nr']: k for b in _D['BLOECKE'] for k in b['skripte']}


def K(nr, titel, tags, hook, ablauf, ending, vorbereitung, alt_ending=None, ad=None):
    return dict(nr=nr, titel=titel, tags=tags, hook=hook, ablauf=ablauf, ending=ending, alt=alt_ending, vorb=vorbereitung, ad=ad)


KOPF = 'MonBerg · Drehskripte Bar · Kundenfassung · Stand 20.11. · 2026-1120-MB-D'
TITEL = 'MonBerg · Drehskripte an der Bar'
UNTER = 'KUNDENFASSUNG · 4 SKRIPTE ZUM VORLESEN · STAND 20.11.2026'
ABLAUF_LAB = 'Sprechtext zum Vorlesen / Ablauf'
REIHE_H = ('REIHENFOLGE', 'SKRIPT', 'ZEIT')

INTRO = [
    ('Absicht des Drehs',
     'Vier Skripte für einen Abenddreh an der Bar: zwei Ads und zwei Serienformate. '
     'Jede Rolle hat ihre Sätze wörtlich. Am Set wird Satz für Satz vorgelesen und direkt gespielt. Versprecher sind kein Problem: Satz neu ansetzen, der Schnitt verdichtet.'),
    ('Besetzung',
     'Team 1 und Team 2: zwei Personen aus dem MonBerg-Team. Gast: eine Person, die einen Besucher oder Kunden spielt. Hinter der Kamera: Haurer Media.'),
    ('Ort & Licht',
     'Alles an der Bar. Die Barbeleuchtung ist das Hauptlicht, dazu ein Licht von vorn auf die Gesichter. Im Hintergrund soll die Bar mit Gläsern und Flaschen erkennbar sein, '
     'damit man den Ort sofort sieht. Das Fenster nach draußen nicht ins Bild nehmen.'),
    ('Requisiten',
     'Eine Mappe und ein dicker Stift (07) · vorgeschriebene Seiten in der Mappe mit „140“ und „bis 3 Uhr“ (07) · zwei Gläser mit Getränk für den Gast (01, 13) · ein Zettel mit dem Sitzplan für den Gast (10) · '
     'nichts weiter, alles andere liefert die Bar.'),
]

LOOKS = [
    ('Team 1 und Team 2', 'Arbeitskleidung, wie das Team bei einer Veranstaltung aussieht', 'In allen vier Skripten gleich, damit man die Serien wiedererkennt.'),
    ('Gast', 'Alltagskleidung, Jacke an oder über dem Hocker', 'In 01 als Mitarbeiter einer Firma, in 07 und 13 als Kunde bei der Anfrage, in 10 als Orga-Kollege. Kleidung darf gleich bleiben.'),
]
LOOK_HINWEIS = 'Empfehlung / Orientierung: Die konkreten Teile entscheidet jede Person selbst.'

REIHENFOLGE_TEXT = ('Zuerst die Ad, solange alle frisch sind. Danach die beiden Serien, zum Schluss der Sitzplan. Gesamt etwa 70 Minuten.')
REIHENFOLGE = [
    ('1', '01 Ausreden vs. MonBerg (Ad)', 'ca. 20 Min.'),
    ('2', '07 Sätze, die wir jede Woche hören · 5 Folgen', 'ca. 20 Min.'),
    ('3', '13 Was er sagt, was er meint · 3 Folgen', 'ca. 15 Min.'),
    ('4', '10 Der Sitzplan (Ad)', 'ca. 15 Min.'),
]
KLAEREN = []
BLOECKE = []


def B(banner, text, *skripte):
    BLOECKE.append(dict(banner=banner, text=text, skripte=list(skripte)))


B('AD · AN DER BAR', 'Team 1, Team 2, Gast · ca. 20 Minuten.',
  K('01', 'Ausreden vs. MonBerg', 'Sketch · Ad · 25–30 s · Team 1, Team 2, Gast',
    'Gast, an der Bar, seufzt: „Ich hab echt keine Lust auf die Weihnachtsfeier.“',
    ['Der Gast sitzt an der Bar und spielt einen Mitarbeiter ohne Lust auf die Weihnachtsfeier. Team 1 steht hinter der Bar, Team 2 lehnt seitlich am Tresen. Beide kontern jede Ausrede mit einem Fakt, trocken und ohne eine Miene zu verziehen.',
     'Gast, ins Glas schauend: „Ich hab echt keine Lust auf die Weihnachtsfeier.“',
     'Gast: „Die ist doch eh immer im Konferenzraum.“ · Team 1, poliert ein Glas: „Bei uns gibt’s fast 3.500 Quadratmeter.“',
     'Gast: „Da ist nie Platz für alle.“ · Team 2: „Bis zu 1.500 Gäste.“',
     'Gast: „Und wenn’s regnet?“ · Team 1: „Überdachter Wintergarten.“',
     'Gast: „Im Winter ist eh alles grau.“ · Team 2: „Palmen. Quarzsand. Liegestühle.“',
     'Gast, nach langer Pause, leise: „… ich hab nichts zum Anziehen.“',
     'Team 1 und Team 2 schauen sich an. Schulterzucken. Team 1 schiebt dem Gast wortlos ein Glas hin.',
     'CTA · Team 1 schaut in die Kamera: „Und ihr? Plant eure Firmenfeier am MonBerg. Fragt jetzt bei uns an.“'],
    'CTA von Team 1 in die Kamera → Cut. Einblendung: „Firmenfeier am MonBerg · Jetzt anfragen“.',
    'Einstellungen: 1. Halbtotale über den Tresen auf alle drei, als Grundeinstellung. 2. Gast nah, für jede Ausrede. 3. Team 1 und Team 2 jeweils nah, für jeden Konter. '
    'Jede Ausrede und jeder Konter als eigener Take, mindestens zwei Mal. Die Konter kurz und schnell sprechen, die Pause vor „nichts zum Anziehen“ lang lassen. '
    'Im Schnitt läuft jeder Fakt zusätzlich als Einblendung mit.',
    ad=('hoch',
        'Fünf belegte Fakten in 25 Sekunden, jede Ausrede ist ein Einwand, den echte Entscheider haben. Die Bar im Hintergrund zeigt sofort, wo man ist. Endet mit einem gesprochenen CTA.',
        'Hook in der ersten Sekunde, ohne Einleitung. Jeder Konter mit Fakt als Einblendung. Am Ende „Firmenfeier am MonBerg · Jetzt anfragen“. Geschaltet wird nach eurer Freigabe.')),
)

B('SERIEN & AD · AN DER BAR', 'Team 1, Team 2, Gast · Skripte 07, 13, 10 · ca. 50 Minuten. Gleiche Plätze und gleicher Bildausschnitt für alle Folgen einer Serie.',
  K('07', 'Sätze, die wir jede Woche hören', 'Serie · Sketch · 8–12 s je Folge · Team 1, Team 2, Gast',
    'Gast: „Wir sind so ca. 100 Leute.“',
    ['Der Gast sitzt an der Bar und erzählt von seiner Feier. Team 1 und Team 2 stehen ihm gegenüber, Team 2 mit der Mappe. Der Gast sagt einen Anfrage-Klassiker, das Team reagiert trocken, fast ohne Worte. Jede Folge ist ein eigener Clip.',
     'Folge 1 · Gast: „Wir sind so ca. 100 Leute.“ · Team 2 nickt freundlich und schreibt in die Mappe. Nah auf die Mappe: „140“.',
     'Folge 2 · Gast: „Das Wetter wird schon.“ · Team 1 zeigt wortlos mit dem Daumen über die Schulter. Einblendung: „Überdachter Wintergarten.“',
     'Folge 3 · Gast: „Wir wollen was ganz Entspanntes. Nicht so lang.“ · Team 2 schreibt in die Mappe. Nah: „bis 3 Uhr“.',
     'Folge 4 · Gast: „Die Rede vom Chef ist ganz kurz.“ · Team 1 und Team 2, gleichzeitig: „Mhm.“',
     'Folge 5 · Gast: „Wir sagen euch bis morgen Bescheid.“ · Team 2 klappt die Mappe zu, Team 1 schaut auf die Uhr.'],
    'Reaktion des Teams → kurzer Blick in die Kamera → Cut. Einblendung: „Welchen Satz hört ihr am häufigsten?“',
    'Einstellungen: 1. Gast nah über den Tresen, er spricht zum Team, nicht in die Kamera. 2. Gegenschnitt auf Team 1 und Team 2 zusammen. 3. Nah auf die Mappe für „140“ und „bis 3 Uhr“. '
    'Die Zahlen vorher mit dickem Stift auf zwei Seiten schreiben, damit sie lesbar sind. Alle fünf Folgen am Stück, ohne Umbau. '
    'Freundlich bleiben: Das Team macht sich nie über den Kunden lustig, es kennt ihn nur gut.'),
  K('13', 'Was er sagt, was er meint', 'Untertitel-Gag · Serie · 15–20 s je Folge · Team 1, Gast',
    'Gast: „Wir planen eigentlich nur was ganz Kleines.“',
    ['Gast und Team 1 stehen sich am Tresen gegenüber. Der Gast spricht komplett ernst und freundlich. Was er wirklich meint, steht im Schnitt als Einblendung darunter. Am Set werden nur die Sätze gesprochen.',
     'Folge 1 · Gast: „Wir planen eigentlich nur was ganz Kleines.“ · Einblendung: „Die ganze Firma kommt.“',
     'Team 1: „Wie viele seid ihr denn?“',
     'Gast: „So zwanzig.“ · Einblendung: „Plus Partner. Plus Kinder. Plus der Vertrieb aus Hamburg.“',
     'Team 1, ganz ruhig: „Bei uns passen bis zu 1.500 Gäste.“',
     'Gast: „Ach, so viele werden’s nicht.“ · Einblendung: „Doch.“',
     'Folge 2 · Gast: „Wir schauen uns erstmal nur unverbindlich um.“ · Einblendung: „Die Feier ist nächste Woche.“ · Team 1: „Wann wäre denn euer Termin?“ · Gast: „Ist noch ganz offen.“ · Einblendung: „Freitag.“',
     'Folge 3 · Gast: „Budget ist eigentlich nicht so wichtig.“ · Einblendung: „Der Chef weiß noch nichts davon.“ · Team 1: „Und wer entscheidet am Ende?“ · Gast: „Ich. Also … eigentlich.“ · Einblendung: „Nein.“'],
    'Letzte Einblendung bleibt kurz stehen, Gast lächelt unschuldig in die Kamera → Cut.',
    'Einstellungen: 1. Gast nah, mit Platz unten im Bild für die Einblendung. 2. Team 1 nah für die Rückfragen. Nach jedem Satz des Gastes zwei Sekunden Pause halten, '
    'dort steht später die Einblendung. Der Gast spielt nie übertrieben, der Witz steht allein in der Schrift. Drei Folgen am Stück drehen.'),
  K('10', 'Der Sitzplan', 'Sketch · Ad · 20–25 s · Team 1, Team 2, Gast',
    'Einblendung: „Wenn du den Sitzplan für die Weihnachtsfeier machen musst.“ · Gast: „Vertrieb nicht neben Buchhaltung.“',
    ['Team 1 und Team 2 sitzen an einem Bartisch oder am Tresen, Team 2 mit Mappe und Stift. Der Gast spielt den Kollegen aus dem Orga-Team, der die Weihnachtsfeier plant, und liest von einem Zettel ab. Er wird mit jedem Punkt komplizierter, das Team bleibt ruhig.',
     'Gast, sofort, ohne Einleitung: „Vertrieb nicht neben Buchhaltung.“ · Team 2 nickt und schreibt.',
     'Gast: „Marketing nicht neben IT, die reden sonst nur über Passwörter.“ · Team 2 schreibt weiter.',
     'Gast: „Und Jürgen nicht neben Jürgen.“ · Team 1: „Wie viele Jürgens habt ihr?“ · Gast: „Vier.“',
     'Gast: „Der Chef in die Mitte. Nein, doch nicht. An den Rand. Nein, doch in die Mitte …“',
     'Team 1 und Team 2 schauen sich an. Team 2, ganz ruhig: „Wie wär’s mit freier Platzwahl?“',
     'Der Gast lässt den Zettel sinken und schaut die beiden lange an: „… ihr seid Genies.“',
     'Team 1, entspannt: „Bis zu 1.500 Gäste, fast 3.500 Quadratmeter. Da findet jeder seinen Platz.“',
     'Team 2, trocken: „Auch alle vier Jürgens.“ · Der Gast zerknüllt den Zettel und wirft ihn hinter sich.',
     'CTA · Team 1 schaut in die Kamera: „Sitzplan-Stress? Feiert am MonBerg. Fragt jetzt bei uns an.“'],
    'CTA von Team 1 in die Kamera → Cut. Einblendung: „Firmenfeier am MonBerg · Jetzt anfragen“.',
    'Worum es geht: Jeder, der schon mal eine Firmenfeier organisiert hat, kennt den Sitzplan-Stress. Das Team nimmt ihn mit einem Satz ab und liefert danach die Fakten, warum das am MonBerg funktioniert. '
    'Einstellungen: 1. Halbtotale auf alle drei am Tisch, Bar im Hintergrund. 2. Gast nah für jeden Punkt. 3. Team 1 und Team 2 nah für die Reaktionen und „freie Platzwahl“. '
    'Jeder Punkt des Gastes ein eigener Take, schneller werden zum Ende hin. Die Namen sind Beispiele, nur keine echten Kunden- oder Mitarbeiternamen. Einen beschriebenen Zettel für den Gast bereitlegen. Die zwei Schlusssätze und den CTA zusätzlich einzeln aufnehmen, damit die Ad auch ohne „Genies“ geschnitten werden kann.',
    ad=('hoch',
        'Trifft genau die Person, die die Feier organisiert und die Location aussucht. Das Problem kennt jeder ohne Vorwissen, die Pointe bleibt hängen, und am Ende stehen zwei belegte Fakten und die Aufforderung.',
        'Die Einblendung „Wenn du den Sitzplan für die Weihnachtsfeier machen musst.“ steht ab der ersten Sekunde, der Gast startet ohne Einleitung. Fakten zusätzlich als Einblendung. Schluss: „Firmenfeier am MonBerg · Jetzt anfragen“. Geschaltet wird nach eurer Freigabe. Im Frühjahr als Sommerfest-Fassung.')),
)
