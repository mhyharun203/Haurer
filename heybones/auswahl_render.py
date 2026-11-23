"""Hey Bones Auswahl als Diktier-PDF. Aufruf: python3 -I auswahl_render.py auswahl_data.py out.html"""
import html, runpy, sys
E = html.escape
D = runpy.run_path(sys.argv[1])

CSS = '''
@page { size: A4; margin: 13mm 15mm 13mm; @bottom-right { content: "Seite " counter(page) " von " counter(pages); font: 8pt Helvetica, Arial, sans-serif; color: #888; } }
body { font-family: Helvetica, Arial, sans-serif; color: #111; margin: 0; }
h1 { font-size: 22pt; margin: 0 0 2mm; }
.sub { color: #555; font-size: 10pt; margin-bottom: 5mm; line-height: 1.4; }
.ov h2 { font-size: 12pt; margin: 5mm 0 1.5mm; color: #b8862b; }
.ov ol { margin: 0; padding-left: 7mm; font-size: 10pt; } .ov li { margin-bottom: .8mm; }
.ov .bt { font-size: 9pt; color: #666; margin-bottom: 1mm; }
.regeln { font-size: 9.3pt; background: #f6f2ea; padding: 3mm 4mm; margin-top: 5mm; line-height: 1.45; }
.block { break-before: page; background: #111; color: #fff; padding: 4.5mm 6mm; margin-bottom: 3mm; }
.block b { display: block; color: #e0a640; font-size: 15pt; margin-bottom: 2mm; } .block span { font-size: 10.5pt; line-height: 1.4; }
.block ol { margin: 3mm 0 0; padding-left: 6mm; font-size: 10pt; color: #ddd; }
section { break-before: page; } section.first { break-before: avoid; }
.kopf { font-size: 8.5pt; color: #b8862b; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
h3 { font-size: 18pt; margin: .5mm 0 .5mm; }
.var { font-size: 10pt; color: #555; margin-bottom: 2mm; }
.warum { font-size: 9.3pt; color: #444; border-bottom: 1.2pt solid #111; padding-bottom: 2.5mm; margin-bottom: 4mm; font-style: italic; }
.zeile { display: flex; gap: 2.5mm; break-inside: avoid; }
.tc { width: 11mm; flex: none; font-size: 8.6pt; font-weight: 700; color: #111; text-align: right; padding-top: .3mm; line-height: 1.25; font-variant-numeric: tabular-nums; }
.take { flex: 1; break-inside: avoid; margin: 0 0 1.7mm; padding-left: 4mm; border-left: 2.5pt solid #b8862b; }
.take.hook { border-left-color: #111; background: #f6f2ea; padding: 2mm 3mm 2mm 4mm; }
.take.tiktok { border-left-color: #111; border-left-style: dashed; }
.tn { font-size: 8.3pt; font-weight: 700; color: #b8862b; letter-spacing: .05em; }
.kam { font-size: 8.8pt; color: #666; margin: .3mm 0 .2mm; }
.hg { font-size: 8.8pt; color: #2b6e3f; margin: 0 0 1.2mm; font-weight: 700; }
.satz { font-size: 12pt; line-height: 1.25; font-weight: 700; margin-top: .8mm; }
h4 { font-size: 10.5pt; margin: 3mm 0 1.5mm; border-top: 1pt solid #ddd; padding-top: 3mm; break-after: avoid; }
.ex { font-size: 11pt; font-weight: 700; margin: 0 0 1.8mm; padding-left: 4mm; border-left: 2.5pt solid #ccc; }
'''

nr = 0
ov, body = [], []
for btitel, btext, videos in D['BLOECKE']:
    items = []
    extra = ''
    body.append(f'<div class="block"><b>{E(btitel)}</b><span>{E(btext)}</span>{extra}</div>')
    first = True
    for v in videos:
        nr += 1
        items.append(f'<li value="{nr}">{E(v["titel"])} <span style="color:#999">· {E(v["produkt"])} · {E(v["laenge"])}</span></li>')
        t = []
        n = 0
        zeit = 0.0
        def tc(sek):
            return f'{int(sek)//60}:{int(round(sek))%60:02d}' if sek < 60 else f'{int(sek)//60}:{int(round(sek))%60:02d}'
        def dauer(text):
            return max(1.5, len(text.split()) / 2.6 + 0.4)
        for kam, satz in v['takes']:
            n += 1
            gesagt = v['hooks'][0] if satz == 'HOOK' else satz
            von, bis = zeit, zeit + dauer(gesagt)
            if n < len(v['takes']):
                zeit = bis
            zc = f'<div class="tc">{tc(von)}<br>–{tc(bis)}</div>'
            hg = ''
            if ' · HG: ' in kam:
                kam, hg = kam.split(' · HG: ', 1)
                hg = f'<div class="hg">Hintergrund: {E(hg)}</div>'
            if satz == 'HOOK':
                t.append(f'<div class="zeile">{zc}<div class="take hook"><div class="tn">TAKE {n} · HOOK · MURAT</div><div class="kam">Kamera: {E(kam)}</div>{hg}<div class="satz">„{E(v["hooks"][0])}“</div></div></div>')
            else:
                t.append(f'<div class="zeile">{zc}<div class="take"><div class="tn">TAKE {n} · MURAT</div><div class="kam">Kamera: {E(kam)}</div>{hg}<div class="satz">„{E(satz)}“</div></div></div>')
        last_kam, last_satz = v['takes'][-1]
        tt = last_satz.replace('90 Tage', '14 Tage')
        t.append(f'<div class="zeile"><div class="tc">statt<br>Take {n}</div><div class="take tiktok"><div class="tn">TAKE {n} B · CTA · TIKTOK-FASSUNG</div><div class="kam">Kamera: wie Take {n}, gleich danach aufnehmen</div><div class="satz">„{E(tt)}“</div></div></div>')
        gesamt = f'{int(round(bis))} s'
        alt = ''.join(f'<div class="ex">„{E(h)}“</div>' for h in v['hooks'][1:])
        ort = f' · {E(v["ort"])}' if v.get('ort') else ''
        vg = ''
        if v is videos[-1] and btitel == 'Murats Geschichte':
            vg = '<h4>Vorgespräch mit Murat, vor dem Dreh · beantwortet die Lücken in eckigen Klammern</h4><ol style="font-size:10.5pt;margin:0;padding-left:6mm">' + ''.join(f'<li style="margin-bottom:1mm">{E(q)}</li>' for q in D['VORGESPRAECH']) + '</ol>'
        cls = 'first' if first else ''
        first = False
        body.append(f'<section class="{cls}"><div class="kopf">Video {nr:02d} · {E(btitel)}</div><h3>{E(v["titel"])}</h3>'
                    f'<div class="var">{E(v["produkt"])} · Sprechzeit ca. {gesamt}{ort}</div><div class="warum">{E(v["warum"])}</div>{"".join(t)}'
                    f'<h4>Alternative Hooks · zusätzlich aufnehmen, ersetzen Take 1</h4>{alt}{vg}</section>')
    ov.append(f'<h2>{E(btitel)}</h2><div class="bt">{E(btext)}</div><ol>{"".join(items)}</ol>')

out = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Hey Bones Auswahl</title><style>{CSS}</style></head><body>
<div class="ov"><h1>Hey Bones · Auswahl · {nr} Skripte</h1>
<div class="sub">Die besten Skripte aus der Drehtag-Fassung, Satz für Satz. Links steht für jeden Satz die Sekunde von bis im fertigen Video, gerechnet mit ruhigem Sprechtempo. Pro Take eine Kamera-Zeile und Murats Satz wörtlich. Murat liest einen Satz, spricht ihn in die Kamera, dann der nächste. Bei den Greenscreen-Videos steht unter jedem Satz der Clip, der im Schnitt dahinter läuft.</div>
{"".join(ov)}
<div class="regeln"><b>Für alle Videos:</b> Murat stellt sich nicht jedes Mal vor. Nennt er seinen Beruf, dann Chiropraktiker. Dosierung immer: ein Löffel pro 10 Kilo übers Futter. Keine Heilversprechen: Murat sagt „unterstützen“, nie „heilt“ oder „weg“. Jeder Hook wird drei Mal aufgenommen, die Alternativen gleich danach. Der CTA kommt immer wörtlich, und zwar zwei Mal: einmal mit 90 Tagen für den Onlineshop, einmal mit 14 Tagen für TikTok (Take B). TikTok-Fassungen nur mit Take B schneiden.</div></div>
{"".join(body)}
</body></html>'''
open(sys.argv[2], 'w').write(out)
print(nr)
