
KUNDE = 'MonBerg Monheim am Rhein'
ZEITRAUM = 'November / Anfang Dezember 2026'
STAND = 'Stand: 24. November 2026'

LEGENDE = [
    ('PLAN', 'Plan.', ''),
    ('HAURER', 'Empfehlung. Die Empfehlung von Haurer Media ist rein eine Empfehlung und basiert auf Erfahrung. Die Entscheidung obliegt euch: Wir geben lediglich eine Empfehlung ab, am Ende des Tages entscheidet ihr.', 'h'),
    ('STATUS', '<span class="s-online">online</span> = gepostet · gedreht = Material ist da · <span class="s-drehen">drehen</span> = Material fehlt noch', 'raw'),
]

REGELN = [
    ('Paket', 'Laut Angebot 2026-0808-MB-B: 8 Videos organisch, 4 Videos für Anzeigen, 4 Carousel- oder Fotobeiträge, 3 Kanäle (Instagram, TikTok, Facebook), bis zu 3 Drehtermine im Monat.'),
    ('Rhythmus', '8 organische Reels pro Monat laut Paket, auf allen drei Kanälen. <span class="hh">Haurer-Empfehlung: etwa zwei pro Woche.</span>'),
    ('Reihenfolge', 'Bereits gedrehte Videos kommen zuerst. Sketche, Serie und zweideutige Clips wechseln sich ab, nie zwei zweideutige Clips direkt hintereinander.'),
    ('Dreh 04.11.', 'Vier Videos gedreht: 01 Eisstockschießen auf dem MonBerg (organisch und als Ad 10) · 02 „So früh hatte ich noch nie einen stehen.“ · 03 MonGarten vs. MonStrand – Das Duell · 05 „Kommt auf Fotos kleiner rüber.“ (mit Drohne)'),
    ('Dreh 19.11.', 'Drei Videos gedreht: 08 „Kurze Frage …“ · Wo kann ich parken? · 09 „Alleine krieg ich den nicht hoch.“ · 11 „Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen? (Ad)'),
    ('Dreh 23.11.', 'Abenddreh an der Bar, vier Videos gedreht: 06 Was er sagt, was er meint · 12 Ausreden vs. MonBerg (Ad) · 13 Der Sitzplan (Ad) · 14 Hier kannst du … hier eher nicht (Ad)'),
    ('Dreh 27.11.', 'Auf Kundenwunsch: Die dekorierte Location wird abgedreht (07).'),
    ('Anzeigen', 'Vier Ads im November (10–13), dazu eine Ad Anfang Dezember (14). Online: Eisstockschießen auf dem MonBerg. Die weiteren Ads werden jeweils nach eurer Freigabe geschaltet.'),
]

# (nr, datum, video, format, status, haurer, notiz)  | Monatszeile: ('MONAT',)
KALENDER = [
    ('NOVEMBER',),
    ('01', 'Do 12.11.', 'Eisstockschießen auf dem MonBerg', 'Sketch', 'online', ''),
    ('02', 'Mo 16.11.', 'So früh hatte ich noch nie einen stehen.', 'Zweideutig', 'online', ''),
    ('03', 'Fr 20.11.', 'MonGarten vs. MonStrand · Das Duell', 'Sketch', 'online', ''),
    ('04', 'Di 24.11.', 'Die Firmenfeier ist freiwillig.', 'Sketch · Chatverlauf', 'gedreht',
     'Passt mitten in die Planung der Weihnachtsfeiern.'),
    ('05', 'Do 26.11.', 'Kommt auf Fotos kleiner rüber.', 'Zweideutig', 'gedreht', ''),
    ('06', 'Sa 28.11.', 'Was er sagt, was er meint', 'Serie', 'gedreht', ''),
    ('07', 'So 29.11.', 'Die dekorierte Location', 'Location', 'drehen',
     'Zum 1. Advent, zwei Tage nach dem Dreh, passend zum Start in die Adventszeit.',
     'Auf Kundenwunsch. Dreh am Fr 27.11.'),
    ('ANFANG DEZEMBER',),
    ('08', 'Di 01.12.', '„Kurze Frage …“ · Wo kann ich parken?', 'Serie', 'gedreht', ''),
    ('09', 'Do 03.12.', 'Alleine krieg ich den nicht hoch.', 'Zweideutig', 'gedreht', ''),
    ('ADS',),
    ('10', 'November', 'Eisstockschießen auf dem MonBerg', 'Ad', 'online', ''),
    ('11', 'Mo 23.11.', '„Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen?', 'Serie · Ad', 'gedreht', '',
     'Schaltung als Anzeige nach eurer Freigabe.'),
    ('12', 'Fr 27.11.', 'Ausreden vs. MonBerg', 'Sketch · Ad', 'gedreht', '',
     'Schaltung nach eurer Freigabe.'),
    ('13', 'Mo 30.11.', 'Der Sitzplan', 'Sketch · Ad', 'gedreht', '',
     'Schaltung nach eurer Freigabe.'),
    ('14', 'Mi 02.12.', 'Hier kannst du … hier eher nicht', 'Trend · Ad', 'gedreht',
     'Die stärkste Ad aus dem Bar-Dreh: alle Innenbereiche in 25 Sekunden, endet mit „Und hier fragst du an.“',
     'Schaltung nach eurer Freigabe.'),
]
