"""MonBerg-Drehplan im Haurer-Stil der ProOffice-Kundenfassung. Aufruf: python3 -I mb_render.py mb_data.py out.html"""
import html, runpy, sys

E = html.escape
D = runpy.run_path(sys.argv[1])

CSS = r'''
@page { size: A4; margin: 21mm 0 15mm 0;
  @top-left { content: url("logo.svg"); background: #0b0b0d; vertical-align: middle; padding-left: 15mm; width: 60mm; }
  @top-center { content: ""; background: #0b0b0d; }
  @top-right { content: "KOPFZEILE"; background: #0b0b0d; color: #fff; font: 600 7.4pt Helvetica, Arial, sans-serif; vertical-align: middle; padding-right: 15mm; text-align: right; width: 120mm; }
  @bottom-left { content: "HAURER.MEDIA — VIDEO & SOCIAL MEDIA"; font: 7pt Helvetica, Arial, sans-serif; letter-spacing: .04em; color: #8d877c; padding-left: 15mm; vertical-align: top; padding-top: 2mm; }
  @bottom-right { content: "Seite " counter(page); font: 7pt Helvetica, Arial, sans-serif; color: #8d877c; padding-right: 15mm; vertical-align: top; padding-top: 2mm; }
}
* { box-sizing: border-box; }
body { margin: 0; padding: 0 15mm; font-family: Helvetica, "Helvetica Neue", Arial, sans-serif; font-size: 9.3pt; line-height: 1.38; color: #2a2620; background: #fff; }
h1 { font-size: 21pt; margin: 4mm 0 1mm; color: #111; }
.unter { color: #c9963e; font-weight: 700; font-size: 10.5pt; letter-spacing: .02em; margin: 0 0 3mm; }
h2 { font-size: 12.5pt; margin: 3mm 0 1.2mm; color: #111; }
p { margin: 0 0 2mm; }
table.t { width: 100%; border-collapse: collapse; margin: 1mm 0 1.5mm; font-size: 8.6pt; }
table.t td { padding: 1.4mm 2.4mm; border-bottom: .6pt solid #e5e0d6; vertical-align: top; }
table.t td.k { background: #f3f1ec; font-weight: 700; width: 28%; }
table.r { width: 100%; border-collapse: collapse; font-size: 8.3pt; margin-top: 1mm; }
table.r th { color: #c9963e; text-align: left; font-size: 7.4pt; letter-spacing: .03em; padding: 1.5mm 2mm; border-bottom: 1pt solid #c9963e; }
table.r td { padding: 1.1mm 2mm; border-bottom: .6pt solid #e5e0d6; vertical-align: top; }
table.r td:first-child { font-weight: 700; width: 27%; }
.hint { color: #8d877c; font-size: 8.4pt; }
ul.k { margin: 1mm 0 0; padding-left: 4.5mm; font-size: 8.6pt; } ul.k li { margin-bottom: 1mm; }
.banner { background: #0b0b0d; color: #fff; border-left: 2.2mm solid #db9838; padding: 3mm 4mm; margin: 2mm 0 3mm; break-after: avoid; }
.banner b { display: block; color: #db9838; font-size: 11.5pt; letter-spacing: .02em; margin-bottom: 1mm; }
.banner span { font-size: 8.6pt; }
section.s { break-before: page; }
section.s.first { break-before: avoid; }
.blockstart { break-before: page; }
.sn { color: #db9838; font-weight: 700; margin-right: 2mm; }
h3 { font-size: 15.5pt; margin: 2mm 0 .5mm; color: #111; line-height: 1.15; }
.tags { color: #948e84; font-size: 8pt; margin-bottom: 3mm; }
.lab { color: #b8862b; font-weight: 700; font-size: 7.3pt; letter-spacing: .04em; margin: 2.5mm 0 1mm; text-transform: uppercase; }
.hook { background: #0b0b0d; color: #fff; font-weight: 700; font-size: 12pt; padding: 3.5mm 4.5mm; line-height: 1.3; }
.ablauf { background: #faf6ee; padding: 3mm 4mm; }
.ablauf p { margin: 0 0 1.6mm; }
.ending { border: .8pt solid #e1dbd1; background: #fffaf0; display: flex; font-size: 8.8pt; }
.ending div { padding: 2mm 3mm; }
.ending .e1 { font-weight: 700; background: #f6efe1; width: 22mm; }
.vorb { border: .8pt solid #e8e3d9; padding: 3mm 4mm; font-size: 8.8pt; }
.adbox { border: 1pt solid #c9963e; background: #fff8ea; padding: 2.4mm 3.5mm; margin: 0 0 1mm; font-size: 8.6pt; }
.adbox b { color: #b8862b; font-size: 7.6pt; letter-spacing: .05em; display: block; margin-bottom: 1mm; }
.adbox p { margin: 0 0 1mm; } .adk { font-weight: 700; }
.adline { font-size: 8.2pt; color: #6d675d; border-left: 1.5mm solid #e1dbd1; padding: 1mm 2.5mm; margin: 0 0 1mm; }
.offen { color: #b8862b; font-weight: 700; }
'''


def fmt(s):
    s = E(s)
    return s.replace('Offen:', '<span class="offen">Offen:</span>')


def adbox(k):
    a = k.get('ad')
    if not a:
        return ''
    stufe, warum, fassung = a
    if fassung:
        return (f'<div class="adbox"><b>AD · ADPOTENZIAL {E(stufe.upper())}</b><p>{fmt(warum)}</p>'
                f'<p><span class="adk">Ad-Fassung:</span> {fmt(fassung)}</p></div>')
    return f'<div class="adline">Adpotenzial {E(stufe)}: {fmt(warum)}</div>'


def skript(k, first):
    abl = ''.join(f'<p>{fmt(x)}</p>' for x in k['ablauf'])
    alt = f'<div class="ending"><div class="e1">Alternativ</div><div>{fmt(k["alt"])}</div></div>' if k.get('alt') else ''
    return f'''<section class="s{' first' if first else ''}">
<h3><span class="sn">{E(k["nr"])}</span>{E(k["titel"])}</h3>
<div class="tags">{E(k["tags"])}</div>{adbox(k)}
<div class="lab">Hook</div><div class="hook">{fmt(k["hook"])}</div>
<div class="lab">{E(D.get("ABLAUF_LAB", "Beispiel-Sprechtext / Ablauf"))}</div><div class="ablauf">{abl}</div>
<div class="lab">Ending / CTA</div><div class="ending"><div class="e1">Ending</div><div>{fmt(k["ending"])}</div></div>{alt}
<div class="lab">Drehvorbereitung</div><div class="vorb">{fmt(k["vorb"])}</div>
</section>'''


def block(b):
    out = [f'<div class="blockstart"></div>']
    for i, k in enumerate(b['skripte']):
        if i == 0:
            out.append(f'<section class="s first" style="break-before: page"><div class="banner"><b>{E(b["banner"])}</b><span>{E(b["text"])}</span></div>'
                       + skript(k, True)[len('<section class="s first">'):])
        else:
            out.append(skript(k, False))
    return '\n'.join(out[1:])


intro = ''.join(f'<h2>{E(t)}</h2><p>{E(x)}</p>' for t, x in D['INTRO'])
looks = ''.join(f'<tr><td class="k">{E(a)}</td><td>{E(b)}<br><span class="hint">{E(c)}</span></td></tr>' for a, b, c in D['LOOKS'])
reihe = ''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in D['REIHENFOLGE'])
klaeren = ''.join(f'<li>{E(x)}</li>' for x in D['KLAEREN'])

page1 = f'''<h1>{E(D["TITEL"])}</h1><div class="unter">{E(D["UNTER"])}</div>
{intro}
<h2>Outfits</h2><table class="t">{looks}</table><p class="hint">{E(D["LOOK_HINWEIS"])}</p>
<h2>Empfohlene Drehreihenfolge</h2><p>{E(D["REIHENFOLGE_TEXT"])}</p>
<table class="r"><thead><tr>{"".join(f"<th>{E(h)}</th>" for h in D.get("REIHE_H", ("BLOCK", "SKRIPTE", "LOOK")))}</tr></thead><tbody>{reihe}</tbody></table>
'''

css = CSS.replace('KOPFZEILE', D['KOPF'].replace('"', '\\"'))
out = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{E(D["TITEL"])}</title><style>{css}</style></head><body>
{page1}
{''.join(block(b) for b in D["BLOECKE"])}
</body></html>'''
open(sys.argv[2], 'w').write(out)
