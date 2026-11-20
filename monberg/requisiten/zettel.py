"""Anfragezettel (Requisite Skript 07). Aufruf: python3 -I zettel.py out.html [logo-datei]"""
import base64, mimetypes, sys

logo = ''
if len(sys.argv) > 2:
    mt = mimetypes.guess_type(sys.argv[2])[0] or 'image/png'
    logo = f'<img class="logo" src="data:{mt};base64,{base64.b64encode(open(sys.argv[2], "rb").read()).decode()}">'
else:
    logo = '<div class="logo platz">LOGO</div>'

page = f'''<section>
<header>{logo}<div class="titel"><span>Anfrage</span><b>Firmenfeier</b></div></header>
<div class="linie"></div>
<div class="zeile"><div class="k">Firma</div><div class="f"></div></div>
<div class="zeile"><div class="k">Datum</div><div class="f"></div></div>
<div class="row">
<div class="box"><div class="lab"><i>01</i>Gäste</div><div class="feld"></div></div>
<div class="box"><div class="lab"><i>02</i>Ende</div><div class="feld"></div></div>
</div>
<div class="lab n"><i>03</i>Notizen</div><div class="notiz"></div>
<footer><span>Eventlocation</span><span>Monheim am Rhein</span></footer>
</section>'''

css = '''@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;color:#141414;-webkit-print-color-adjust:exact;print-color-adjust:exact}
section{width:210mm;height:297mm;padding:0 0 12mm;break-after:page;display:flex;flex-direction:column;position:relative}
section:last-child{break-after:auto}
header{background:#111;color:#fff;height:58mm;padding:0 16mm;display:flex;align-items:center;justify-content:space-between}
.logo{max-height:30mm;max-width:80mm}
.logo.platz{width:62mm;height:26mm;border:1.2pt dashed #777;color:#888;font-size:10pt;letter-spacing:.3em;display:flex;align-items:center;justify-content:center}
.titel{text-align:right;line-height:1}
.titel span{display:block;font-size:10pt;letter-spacing:.45em;text-transform:uppercase;color:#d6a64f;margin-bottom:3mm}
.titel b{font-size:30pt;font-weight:800;letter-spacing:-.01em}
.linie{height:2.2mm;background:linear-gradient(90deg,#d6a64f,#f0d08a,#d6a64f)}
.zeile{display:flex;align-items:flex-end;margin:0 16mm;height:15mm;border-bottom:1pt solid #c9c3b8}
.zeile:first-of-type{margin-top:8mm}
.k{width:30mm;font-size:8.5pt;letter-spacing:.3em;text-transform:uppercase;color:#8a7f6e;padding-bottom:2mm}
.row{display:flex;gap:8mm;margin:10mm 16mm 0}
.box{flex:1}
.lab{font-size:11pt;font-weight:800;letter-spacing:.22em;text-transform:uppercase;margin-bottom:3mm;display:flex;align-items:center;gap:3mm}
.lab i{font-style:normal;font-size:8pt;color:#fff;background:#111;border-radius:50%;width:7mm;height:7mm;display:inline-flex;align-items:center;justify-content:center;letter-spacing:0}
.feld{height:72mm;border:2.8pt solid #111;border-radius:4mm;position:relative;background:#fff}
.feld:after{content:"";position:absolute;left:-2.8pt;top:-2.8pt;width:14mm;height:14mm;border-left:2.8pt solid #d6a64f;border-top:2.8pt solid #d6a64f;border-top-left-radius:4mm}
.n{margin:9mm 16mm 2mm}
.notiz{flex:1;margin:0 16mm;background:repeating-linear-gradient(#fff 0 12mm,#d9d3c8 12mm 12.3mm)}
footer{margin:4mm 16mm 0;display:flex;justify-content:space-between;font-size:7.5pt;letter-spacing:.35em;text-transform:uppercase;color:#8a7f6e;border-top:1pt solid #d6a64f;padding-top:3mm}
'''
open(sys.argv[1], 'w').write(f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Anfrage Firmenfeier</title><style>{css}</style></head><body>{page * 3}</body></html>')
