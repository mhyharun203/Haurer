"""Contentplan MonBerg im Stil des Café-New-York-Contentplans. Aufruf: python3 -I mb_plan.py out.html"""
import html, sys

E = html.escape

KUNDE = 'MonBerg Monheim am Rhein'
ZEITRAUM = 'November / Dezember 2026'
STAND = 'Stand: 19. November 2026'

LEGENDE = [
    ('PLAN', 'Plan.', ''),
    ('HAURER', 'Empfehlung. Die Empfehlung von Haurer Media ist rein eine Empfehlung und basiert auf Erfahrung. Die Entscheidung obliegt euch: Wir geben lediglich eine Empfehlung ab, am Ende des Tages entscheidet ihr.', 'h'),
    ('STATUS', '<span class="s-online">online</span> = gepostet · <span class="s-geschnitten">geschnitten</span> = fertig zum Posten · gedreht = im Schnitt · <span class="s-produktion">in Produktion</span> = wird gerade ohne Dreh gebaut · <span class="s-drehen">drehen</span> = Material fehlt noch', 'raw'),
]

REGELN = [
    ('Paket', 'Laut Angebot 2026-0808-MB-B: 8 Videos organisch, 4 Videos für Anzeigen, 4 Carousel- oder Fotobeiträge, 3 Kanäle (Instagram, TikTok, Facebook), bis zu 3 Drehtermine im Monat.'),
    ('Rhythmus', '8 organische Reels pro Monat laut Paket, auf allen drei Kanälen. <span class="hh">Haurer-Empfehlung: etwa zwei pro Woche.</span>'),
    ('Reihenfolge', 'Bereits gedrehte Videos kommen zuerst. Sketche, Serie und zweideutige Clips wechseln sich ab, nie zwei zweideutige Clips direkt hintereinander.'),
    ('Dreh 04.11.', 'Vier Videos gedreht: 01 Eisstockschießen auf dem MonBerg (Ad) · 02 „So früh hatte ich noch nie einen stehen.“ · 03 MonGarten vs. MonStrand – Das Duell · 05 „Kommt auf Fotos kleiner rüber.“ (mit Drohne)'),
    ('Dreh 19.11.', 'Drei Videos gedreht: 07 „Kurze Frage …“ · Wo kann ich parken? · 09 „Alleine krieg ich den nicht hoch.“ (mit Fotobox statt Sonnenschirm) · 11 „Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen? (Ad)'),
    ('Nächster Drehtermin', 'Steht noch aus. Drehtermine stehen spätestens sieben Tage vorher fest. Alle Videos mit Status „drehen“ hängen an diesem Termin. Die Reihenfolge im Dezember ist eine Empfehlung, die Daten folgen, sobald der Termin feststeht.'),
    ('Anzeigen', 'Vier Ad-Videos im Monat. Bisher online: Eisstockschießen. Gedreht am 19.11.: „Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen? Empfehlung für die nächsten Ads: Die Kündigung und das Angebotsvideo „Wo würde euer Team feiern?“, beide sprechen Firmenfeiern an.'),
    ('Optional', 'Die Videos unter „Dezember · optional“ werden mitgedreht, wenn am Drehtag Zeit ist, und ersetzen bei Bedarf einen Termin oben. Es rutscht nichts in den Januar.'),
    ('Carousels', 'Vier Carousel- oder Fotobeiträge im Monat, noch nicht im Kalender. Empfehlung: aus dem Material der Drehtage, zum Beispiel die Bereiche des MonBerg im Überblick zur Weihnachtsfeier-Saison.'),
]

# (nr, datum, video, format, status, haurer)  | Monatszeile: ('MONAT',)
KALENDER = [
    ('NOVEMBER',),
    ('01', 'Mi 11.11.', 'Eisstockschießen auf dem MonBerg', 'Ad · organisch', 'online',
     '', 'Als Anzeige bereits online. Organisch voraussichtlich am Mi 11.11.'),
    ('02', 'Fr 13.11.', 'So früh hatte ich noch nie einen stehen.', 'Zweideutig', 'gedreht',
     '<b>Direkt nach dem Eisstockschießen</b> – solange der Weihnachtsbaum gerade aktuell ist.'),
    ('03', 'Di 17.11.', 'MonGarten vs. MonStrand · Das Duell', 'Sketch', 'gedreht',
     '<b>Kommt auf Fotos kleiner rüber (Zweideutig)</b> bewusst nicht direkt danach, sondern mit einem Sketch dazwischen.'),
    ('04', 'diese Woche', 'Die Firmenfeier ist freiwillig.', 'Sketch · Chatverlauf', 'produktion',
     'Wird diese Woche als Chatverlauf umgesetzt, ohne Drehtag. Passt mitten in die Planung der Weihnachtsfeiern.'),
    ('05', 'Di 24.11.', 'Kommt auf Fotos kleiner rüber.', 'Zweideutig', 'gedreht', ''),
    ('06', 'Do 26.11.', 'Offen', '–', 'drehen',
     'Mögliche Idee: <b>kurzer Stimmungs-Clip zum 1. Advent</b> (29.11.), aus dem Material vom 04.11.'),
    ('DEZEMBER',),
    ('07', 'nach Drehtermin', '„Kurze Frage …“ · Wo kann ich parken?', 'Serie', 'gedreht',
     'Start der Serie. Die nächsten Folgen im Abstand von etwa einer Woche, damit man die Serie wiedererkennt.'),
    ('08', 'nach Drehtermin', 'Die Kündigung', 'Sketch', 'drehen',
     'Spricht Geschäftsführer und HR direkt an, mitten in der Saison der Firmenfeiern.'),
    ('09', 'nach Drehtermin', 'Alleine krieg ich den nicht hoch.', 'Zweideutig', 'gedreht',
     'Dritter zweideutiger Clip. Umgesetzt mit einer <b>Fotobox</b> statt des Sonnenschirms.'),
    ('10', 'nach Drehtermin', 'Bitte keine Arbeitsthemen.', 'Kurzclip', 'drehen',
     'Passt genau in die Zeit, in der die Teams selbst feiern.'),
    ('11', 'nach Drehtermin', '„Kurze Frage …“ · Habt ihr Platz für zwei weitere Personen?', 'Serie · Ad', 'gedreht',
     'Als <b>Ad-Video</b> gedreht. Organisch zusätzlich als Folge der Serie möglich.'),
    ('12', 'nach Drehtermin', 'Montag danach', 'Sketch', 'drehen',
     'Nach den ersten Weihnachtsfeier-Wochenenden. Die Spuren im Büro auf Weihnachten anpassen: <b>Lametta statt Sand, Foto aus dem Wintergarten statt vom MonStrand.</b>'),
    ('13', 'nach Drehtermin', 'Was das Team wirklich denkt', 'Team', 'drehen',
     'Letzter Post vor Weihnachten. Zeigt das Team persönlich.'),
    ('DEZEMBER · OPTIONAL',),
    ('14', 'optional', '„Kurze Frage …“ · Und wenn’s regnet?', 'Serie', 'drehen',
     'Wenn am Drehtag Zeit ist. Ersetzt sonst eine Folge der Serie oben.'),
    ('15', 'optional', 'Wer übernimmt die Organisation?', 'Sketch', 'drehen',
     'Wenn gepostet, dann noch im Dezember, zum Beispiel zwischen den Jahren.'),
    ('16', 'optional', 'Wo würde euer Team feiern?', 'Angebot', 'drehen',
     'Eher als <b>Ad-Video</b> als organisch, siehe Anzeigen.'),
    ('17', 'optional', 'POV · Hinter der Bar', 'POV', 'drehen', 'Schnell gedreht, ohne eigenen Aufbau.'),
    ('18', 'optional', 'Vom Schreibtisch an den MonBerg', 'Image', 'drehen', ''),
    ('19', 'optional', 'Ich hab dir einen Termin eingestellt.', 'Kurzclip', 'drehen',
     'Spielt im Liegestuhl am MonStrand. Nur mit Jacken und Decken als Winter-Fassung drehen, sonst weglassen.'),
]

CSS = '''
@page { size: A4; margin: 13mm 15mm 14mm; }
@page cover { margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Helvetica, "Helvetica Neue", Arial, sans-serif; color: #0b0b0d; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cover { page: cover; height: 297mm; padding: 18mm 15mm 0; position: relative; break-after: page; }
.kick { font-size: 7pt; letter-spacing: .32em; color: #8a6420; }
.cover .mid { position: absolute; left: 15mm; right: 15mm; top: 158mm; }
.cover .line { width: 45mm; height: 1.1mm; background: #b8862b; margin-bottom: 3mm; }
.cover h1 { font-size: 27pt; line-height: 1.12; margin: 0 0 3mm; }
.cover .sub { color: #6c675f; font-size: 9pt; }
.cover .foot { position: absolute; left: 15mm; right: 15mm; top: 250mm; border-top: .5pt solid #e8e3d9; padding-top: 2mm; display: flex; justify-content: space-between; font-size: 6.6pt; color: #8d877c; }
.page { padding: 0; }
tbody.g { break-inside: avoid; }
h2 { font-size: 17pt; margin: 0 0 3mm; }
h3 { font-size: 12.5pt; margin: 4mm 0 2mm; }
table.kv { width: 100%; border-collapse: collapse; font-size: 7.4pt; }
table.kv td { padding: 2mm 2.5mm; border-bottom: .5pt solid #e8e3d9; vertical-align: top; line-height: 1.4; }
table.kv td.k { width: 26%; background: #f3f1ec; font-weight: 700; font-size: 6.8pt; }
table.kv td.k.h { color: #8a6420; }
.hh { color: #8a6420; font-style: italic; }
table.cal { width: 100%; border-collapse: collapse; font-size: 7.4pt; }
table.cal th { text-align: left; color: #b8862b; font-size: 6.4pt; letter-spacing: .06em; padding: 1.5mm 1.5mm; border-bottom: 1pt solid #eaa33c; }
table.cal td { padding: 1.6mm 1.5mm; vertical-align: top; line-height: 1.35; }
table.cal tr.p td { border-top: .5pt solid #e8e3d9; }
table.cal tr.p.first td { border-top: none; }
table.cal tr.m td { color: #8d877c; font-size: 6.4pt; letter-spacing: .18em; padding-top: 2.5mm; border-top: .5pt solid #e8e3d9; }
table.cal td.nr { color: #b8862b; width: 7%; }
table.cal td.z { width: 9%; font-size: 6.4pt; letter-spacing: .03em; }
table.cal td.z.h { color: #b8862b; }
table.cal td.d { width: 12%; color: #6c675f; }
table.cal td.f { width: 11%; }
table.cal td.st { width: 12%; font-weight: 700; }
table.cal td.v { font-weight: 700; }
.note { font-weight: 400; color: #6c675f; font-size: 6.8pt; margin-top: .6mm; }
table.cal td.hv { color: #8a6420; font-style: italic; }
table.cal td.hv b { font-style: normal; }
tr { break-inside: avoid; }
.s-online { color: #2e8b3d; font-weight: 700; }
.s-geschnitten { color: #b8862b; font-weight: 700; }
.s-drehen { color: #c0392b; font-weight: 700; }
.s-produktion { color: #1e3a5f; font-weight: 700; }
.s-gedreht { color: #0b0b0d; font-weight: 400; }
'''


def kv(rows):
    out = []
    for k, v, t in rows:
        val = v if t == 'raw' else (f'<span class="hh">{E(v)}</span>' if t == 'h' else E(v))
        out.append(f'<tr><td class="k{" h" if t == "h" else ""}">{E(k)}</td><td>{val}</td></tr>')
    return '<table class="kv">' + ''.join(out) + '</table>'


def cal():
    rows = []
    for r in KALENDER:
        if len(r) == 1:
            rows.append(f'<tbody class="g"><tr class="m"><td colspan="6">{E(r[0])}</td></tr></tbody>')
            continue
        nr, d, v, f, st, h = r[:6]
        note = r[6] if len(r) > 6 else ''
        rows.append(f'<tbody class="g"><tr class="p"><td class="nr">{nr}</td><td class="z">PLAN</td><td class="d">{E(d)}</td>'
                    f'<td class="v">{E(v)}{f'<div class="note">{E(note)}</div>' if note else ''}</td><td class="f">{E(f)}</td><td class="st s-{st}">{E(st)}</td></tr>')
        if h:
            rows.append(f'<tr class="hrow"><td></td><td class="z h">HAURER</td><td></td><td class="hv" colspan="3">{h}</td></tr>')
        rows.append('</tbody>')
    return ('<table class="cal"><thead><tr><th>NR.</th><th>ZEILE</th><th>DATUM</th><th>VIDEO</th><th>FORMAT</th><th>STATUS</th></tr></thead>'
            + ''.join(rows) + '</table>')


out = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Contentplan MonBerg</title><style>{CSS}</style></head><body>
<div class="cover">
<div class="kick">HAURER MEDIA × MONBERG</div>
<div class="mid"><div class="line"></div><h1>Contentplan<br>{E(ZEITRAUM)}</h1><div class="sub">{E(KUNDE)}</div></div>
<div class="foot"><span>{E(STAND)}</span><span>Haurer Media · business@haurer.de</span></div>
</div>
<div class="page">
<h2>Contentplan · {E(ZEITRAUM)} · MonBerg</h2>
<h3>Legende</h3>{kv(LEGENDE)}
<h3>Regeln</h3>{kv([(k, v, "raw") for k, v in REGELN])}
<h3>Kalender</h3>{cal()}
</div></body></html>'''
open(sys.argv[1], 'w').write(out)
