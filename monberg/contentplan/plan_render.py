"""Contentplan-Renderer im Stil des Café-New-York-Contentplans. Aufruf: python3 -I plan_render.py daten.py out.html"""
import html, runpy, sys

E = html.escape
D = runpy.run_path(sys.argv[1])
KUNDE, ZEITRAUM, STAND = D['KUNDE'], D['ZEITRAUM'], D['STAND']
LEGENDE, REGELN, KALENDER = D['LEGENDE'], D['REGELN'], D['KALENDER']
TITEL = D.get('TITEL', 'Contentplan')
KAL_TITEL = D.get('KAL_TITEL', 'Kalender')
ZEILE = D.get('ZEILE', 'PLAN')
OHNE_DATUM = D.get('OHNE_DATUM', False)
KAL_H = D.get('KAL_H', ('NR.', 'ZEILE', 'DATUM', 'VIDEO', 'FORMAT', 'STATUS'))
STATI = ('online', 'geschnitten', 'gedreht', 'produktion', 'drehen')

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
table.cal td.st.frei { width: 22%; font-weight: 400; color: #6c675f; font-size: 6.8pt; }
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
            rows.append(f'<tbody class="g"><tr class="m"><td colspan="{5 if OHNE_DATUM else 6}">{E(r[0])}</td></tr></tbody>')
            continue
        nr, d, v, f, st, h = r[:6]
        note = r[6] if len(r) > 6 else ''
        dz = '' if OHNE_DATUM else f'<td class="d">{E(d)}</td>'
        stl = 'in Produktion' if st == 'produktion' else st
        stc = f' s-{st}' if st in STATI else ' frei'
        rows.append(f'<tbody class="g"><tr class="p"><td class="nr">{nr}</td><td class="z">{ZEILE}</td>{dz}'
                    f'<td class="v">{E(v)}{f'<div class="note">{E(note)}</div>' if note else ''}</td><td class="f">{E(f)}</td><td class="st{stc}">{E(stl)}</td></tr>')
        if h:
            rows.append(f'<tr class="hrow"><td></td><td class="z h">HAURER</td>{"" if OHNE_DATUM else "<td></td>"}<td class="hv" colspan="3">{h}</td></tr>')
        rows.append('</tbody>')
    hs = [h for i, h in enumerate(KAL_H) if not (OHNE_DATUM and i == 2)]
    return ('<table class="cal"><thead><tr>' + ''.join(f'<th>{E(h)}</th>' for h in hs) + '</tr></thead>'
            + ''.join(rows) + '</table>')


out = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{E(TITEL)} MonBerg</title><style>{CSS}</style></head><body>
<div class="cover">
<div class="kick">HAURER MEDIA × MONBERG</div>
<div class="mid"><div class="line"></div><h1>{E(TITEL)}<br>{E(ZEITRAUM)}</h1><div class="sub">{E(KUNDE)}</div></div>
<div class="foot"><span>{E(STAND)}</span><span>Haurer Media · business@haurer.de</span></div>
</div>
<div class="page">
<h2>{E(TITEL)} · {E(ZEITRAUM)} · MonBerg</h2>
<h3>Legende</h3>{kv(LEGENDE)}
<h3>Regeln</h3>{kv([(k, v, "raw") for k, v in REGELN])}
<h3>{E(KAL_TITEL)}</h3>{cal()}
</div></body></html>'''
open(sys.argv[2], 'w').write(out)
