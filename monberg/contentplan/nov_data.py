
KUNDE = 'MonBerg Monheim am Rhein'
ZEITRAUM = 'November 2026'
STAND = 'Stand: 19. November 2026'

LEGENDE = [
    ('PLAN', 'Plan.', ''),
    ('HAURER', 'Empfehlung. Die Empfehlung von Haurer Media ist rein eine Empfehlung und basiert auf Erfahrung. Die Entscheidung obliegt euch: Wir geben lediglich eine Empfehlung ab, am Ende des Tages entscheidet ihr.', 'h'),
    ('STATUS', '<span class="s-online">online</span> = gepostet · <span class="s-geschnitten">geschnitten</span> = fertig zum Posten · gedreht = im Schnitt · <span class="s-produktion">in Produktion</span> = wird gerade erstellt · <span class="s-drehen">drehen</span> = Material fehlt noch', 'raw'),
]

REGELN = [
    ('Paket', 'Laut Angebot 2026-0808-MB-B: 8 Videos organisch, 4 Videos für Anzeigen, 4 Carousel- oder Fotobeiträge, 3 Kanäle (Instagram, TikTok, Facebook), bis zu 3 Drehtermine im Monat.'),
    ('Rhythmus', '8 organische Reels pro Monat laut Paket, auf allen drei Kanälen. <span class="hh">Haurer-Empfehlung: etwa zwei pro Woche.</span>'),
    ('Reihenfolge', 'Bereits gedrehte Videos kommen zuerst. Sketche, Serie und zweideutige Clips wechseln sich ab, nie zwei zweideutige Clips direkt hintereinander.'),
    ('Dreh 04.11.', 'Vier Videos gedreht: 01 Eisstockschießen auf dem MonBerg (Ad) · 02 „So früh hatte ich noch nie einen stehen.“ · 03 „Kommt auf Fotos kleiner rüber.“ · 04 MonGarten vs. MonStrand – Das Duell (mit Drohne)'),
    ('Dreh 27.11.', 'Auf Kundenwunsch: Die dekorierte Location wird abgedreht (06).'),
    ('Anzeigen', 'Online: Eisstockschießen auf dem MonBerg.'),
]

# (nr, datum, video, format, status, haurer)  | Monatszeile: ('MONAT',)
KALENDER = [
    ('NOVEMBER',),
    ('01', 'Do 12.11.', 'Eisstockschießen auf dem MonBerg', 'Ad · organisch', 'online',
     '', 'Gepostet am 12.11. Als Anzeige bereits online.'),
    ('02', 'Mo 16.11.', 'So früh hatte ich noch nie einen stehen.', 'Zweideutig', 'online',
     ''),
    ('03', 'November', 'Kommt auf Fotos kleiner rüber.', 'Zweideutig', 'online', ''),
    ('04', 'Fr 20.11.', 'MonGarten vs. MonStrand · Das Duell', 'Sketch', 'geschnitten',
     ''),
    ('05', 'diese Woche', 'Die Firmenfeier ist freiwillig.', 'Sketch · Chatverlauf', 'produktion',
     'Wird diese Woche als Chatverlauf umgesetzt. Passt mitten in die Planung der Weihnachtsfeiern.'),
    ('06', 'nach Dreh 27.11.', 'Die dekorierte Location', 'Location', 'drehen',
     '<b>Zum 1. Advent am So 29.11. posten</b> – zwei Tage nach dem Dreh, passend zum Start in die Adventszeit.',
     'Auf Kundenwunsch. Dreh am Fr 27.11.'),
]

