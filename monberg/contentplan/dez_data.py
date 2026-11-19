KUNDE = 'MonBerg Monheim am Rhein'
ZEITRAUM = 'Dezember 2026'
STAND = 'Stand: 19. November 2026'

LEGENDE = [
    ('PLAN', 'Plan.', ''),
    ('HAURER', 'Empfehlung. Die Empfehlung von Haurer Media ist rein eine Empfehlung und basiert auf Erfahrung. Die Entscheidung obliegt euch: Wir geben lediglich eine Empfehlung ab, am Ende des Tages entscheidet ihr.', 'h'),
    ('STATUS', '<span class="s-online">online</span> = gepostet · <span class="s-geschnitten">geschnitten</span> = fertig zum Posten · gedreht = im Schnitt · <span class="s-drehen">drehen</span> = Material fehlt noch', 'raw'),
]

REGELN = [
    ('Paket', 'Laut Angebot 2026-0808-MB-B: 8 Videos organisch, 4 Videos für Anzeigen, 4 Carousel- oder Fotobeiträge, 3 Kanäle (Instagram, TikTok, Facebook), bis zu 3 Drehtermine im Monat.'),
    ('Rhythmus', '8 organische Reels laut Paket, auf allen drei Kanälen. <span class="hh">Haurer-Empfehlung: etwa zwei pro Woche.</span>'),
    ('Reihenfolge', 'Bereits gedrehte Videos kommen zuerst. Die Folgen von „Kurze Frage …“ nie direkt hintereinander, damit die Serie nicht ermüdet.'),
    ('Dreh 19.11.', 'Gedreht: 01 „Kurze Frage …“ · Wo kann ich parken? · 02 „Alleine krieg ich den nicht hoch.“ · 09 „Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen? (Ad)'),
    ('Nächster Drehtermin', 'Steht noch aus. Drehtermine stehen spätestens sieben Tage vorher fest. Alle Videos mit Status „drehen“ hängen an diesem Termin, die Daten folgen, sobald er feststeht.'),
    ('Drehskripte', 'Sprechtexte und Ablauf aller neuen Videos stehen im PDF „MonBerg · Drehskripte Dezember“ (2026-1119-MB-D). Die Nummer des Drehskripts steht jeweils unter dem Titel.'),
    ('Anzeigen', 'Vier Ad-Videos (09–12). Ausgewählt nach Adpotenzial: Sie funktionieren ohne Vorwissen, tragen belegte Fakten und enden mit einer klaren Aufforderung. Geschaltet wird erst nach eurer Freigabe.'),
    ('Optional', 'Die Videos unter „Dezember · optional“ werden mitgedreht, wenn am Drehtag Zeit ist, und gehen als Reserve in den Pool.'),
    ('Carousels', 'Vier Carousel- oder Fotobeiträge. <span class="hh">Haurer-Empfehlung: aus dem Material der dekorierten Location vom 27.11. und der Drehtage, zum Beispiel die Bereiche des MonBerg im Überblick.</span>'),
]

KALENDER = [
    ('DEZEMBER · ORGANISCH',),
    ('01', 'Dezember', '„Kurze Frage …“ · Wo kann ich parken?', 'Serie', 'gedreht',
     'Erste Folge im Dezember. Die weiteren Folgen mit Abstand posten, damit man die Serie wiedererkennt.'),
    ('02', 'Dezember', 'Alleine krieg ich den nicht hoch.', 'Zweideutig', 'gedreht', ''),
    ('03', 'nach Drehtermin', 'Sätze, die wir jede Woche hören', 'Serie', 'drehen',
     'Mehrere Folgen am Stück gedreht, eine davon im Dezember, der Rest als Vorrat.', 'Drehskript 07'),
    ('04', 'nach Drehtermin', 'Der Sitzplan', 'Sketch', 'drehen',
     'Mitten in der Saison der Weihnachtsfeiern, trifft genau das Orga-Team.', 'Drehskript 10'),
    ('05', 'nach Drehtermin', '„Kurze Frage …“ · Ist das hier der Eingang?', 'Serie', 'drehen', '', 'Drehskript 05'),
    ('06', 'nach Drehtermin', 'Event-Deutsch, Deutsch-Event', 'Serie', 'drehen',
     'Holt Kommentare über die Frage am Schluss.', 'Drehskript 11'),
    ('07', 'nach Drehtermin', '„Kurze Frage …“ · Kann ich hier mal kurz telefonieren?', 'Serie', 'drehen',
     'Abschluss der Serie.', 'Drehskript 06'),
    ('08', 'nach Drehtermin', 'Unpopuläre Meinung', 'Serie', 'drehen',
     'Acht kurze Folgen aus einem Dreh. Eine im Dezember, der Rest als Vorrat für die nächsten Monate.', 'Drehskript 12'),
    ('DEZEMBER · ADS',),
    ('09', 'Dezember', '„Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen?', 'Serie · Ad', 'gedreht', ''),
    ('10', 'nach Drehtermin', 'Ausreden vs. MonBerg', 'Sketch · Ad', 'drehen',
     'Fünf belegte Fakten in 25 Sekunden, jede Ausrede ist ein echter Einwand.', 'Drehskript 01'),
    ('11', 'nach Drehtermin', 'Die Ja-Wort-Probe', 'Sketch · Ad', 'drehen',
     'Spricht Firmen und Brautpaare an. <b>Zwei Fassungen ausspielen: Firmenfeier und Hochzeit.</b>', 'Drehskript 02'),
    ('12', 'nach Drehtermin', 'Schnellfragerunde', 'Tempo · Ad', 'drehen',
     'Die meisten Fakten im höchsten Tempo, der letzte Satz ist schon die Aufforderung.', 'Drehskript 03'),
    ('DEZEMBER · OPTIONAL',),
    ('13', 'optional', '3 Dinge, die du vor der Firmenfeier klären solltest', 'Nutzwert', 'drehen',
     '<b>Reserve für eine Ad.</b>', 'Drehskript 04'),
    ('14', 'optional', 'Der Anruf', 'Serie', 'drehen', '', 'Drehskript 08'),
    ('15', 'optional', 'Die Jury', 'Serie', 'drehen', 'Passt zur Eisstock-Saison.', 'Drehskript 09'),
    ('16', 'optional', 'Was er sagt, was er meint', 'Serie', 'drehen', '', 'Drehskript 13'),
    ('17', 'optional', 'Der Blick', 'Serie', 'drehen', '', 'Drehskript 14'),
    ('18', 'optional', 'Erklär mir … in 10 Sekunden', 'Challenge', 'drehen', '', 'Drehskript 15'),
    ('19', 'optional', 'Wer zuerst lacht', 'Challenge', 'drehen', '', 'Drehskript 16'),
    ('20', 'optional', 'Hör mal, wo wir sind', 'Ton-Rätsel', 'drehen', '', 'Drehskript 17'),
]
