"""Hey Bones Drehskripte im Schema der ProOffice-Kundenfassung (hb_render.py)."""
import os, re, runpy
_A = runpy.run_path(os.path.join(os.path.dirname(__file__), 'auswahl_data.py'))

KOPF = 'Hey Bones · Dreh · Praxis Murat · Kundenfassung'
FUSS = 'Hey Bones · Drehskripte · Kundenfassung · Haurer Media'
TITEL = 'Hey Bones · Drehskripte'
UNTER = 'KUNDENFASSUNG · PRODUKTIONS- & ABLAUFPLAN · PRAXIS MURAT'

INTRO = [
    ('Absicht des Drehs',
     'Murat so, wie er in der Praxis wirkt: als Chiropraktiker und Gründer, direkt, ehrlich, mit eigener Meinung. Jedes Video startet mit einem provokanten Hook, '
     'nennt ein Zeichen, das jeder Halter kennt, erklärt es aus der Praxis und zeigt Hey Bones als tägliche Routine. Die Sätze stehen wörtlich da, Murat darf sie in seine Worte übersetzen.'),
    ('Drehort', 'Murats Praxis: Behandlungsraum, Greenscreen, vor der Praxis am Auto. Für Murats Geschichte ein ruhiger Raum. Von Haurer am Set: Harun.'),
    ('Format & Ziellänge', 'Finaler Reel-Cut ca. 25–35 Sekunden, Murats Geschichte bis ca. 45 Sekunden. Verdichtet wird im Schnitt.'),
    ('Für alle Videos',
     'Murat stellt sich nicht jedes Mal vor. Nennt er seinen Beruf, dann Chiropraktiker. Dosierung immer: ein Löffel pro 10 Kilo übers Futter. '
     'Keine Heilversprechen: „unterstützen“, nie „heilt“ oder „weg“. Der CTA wird zwei Mal aufgenommen: 90 Tage für den Onlineshop, 14 Tage für TikTok.'),
]
LOOKS = [
    ('Look 1 · Praxis', 'Praxiskleidung, wie Murat auch Hunde behandelt', 'Block 1 bis 3 · Skripte 01–12'),
    ('Look 2 · privat', 'Ruhig, eigene Kleidung', 'Block 4 · Murats Geschichte 13 und 14'),
]
LOOK_HINWEIS = 'Requisiten: Dosen Magen-Darm und Gelenk, Löffel, Napf mit Futter, Plätzchenteller (04), zwei Futtersäcke (03), Fotos von Murats Hund (13, 14).'
REIHENFOLGE_TEXT = ''
REIHE_H = ('BLOCK', 'SKRIPTE', 'LOOK')
REIHENFOLGE = [
    ('Block 1 · Greenscreen', '09 Gras fressen & Schmatzen · 10 Gelber Schaum am Morgen · 11 Steif nach dem Aufstehen · 12 Zögert an Treppe & Kofferraum', 'Look 1 · Praxis'),
    ('5 Min. Pause', 'Umbau in den Behandlungsraum.', ''),
    ('Block 2 · Behandlungsraum', '01 Drei Fragen · 02 Er schlingt · 03 Mythos Abwechslung · 04 Festtage · 05 Wie er aufsteht · 06 Glatte Böden · 08 Nach der Behandlung', 'Look 1 · Praxis'),
    ('Block 3 · Am Auto', '07 Kalter Kofferraum, solange es hell ist', 'Look 1 · Praxis'),
    ('Outfitwechsel + 5 Min. Pause', 'Ruhiger Raum, gedämpftes Licht, Fotos bereitlegen.', ''),
    ('Block 4 · Murats Geschichte', '13 Warum es Hey Bones gibt · 14 Das Foto', 'Look 2 · privat'),
]
KLAEREN = []

BANNER = {
    'Magen-Darm': ('MAGEN-DARM · BEHANDLUNGSRAUM', 'Look 1 · Praxis · Block 2 · Skripte 01–04. Alle gehen ohne Hund, mit Hund wirken sie stärker.'),
    'Gelenk': ('GELENK · BEHANDLUNGSRAUM UND AUTO', 'Look 1 · Praxis · Block 2 und 3 · Skripte 05–08. 07 vor der Praxis am Auto, solange es hell ist.'),
    'Greenscreen': ('GREENSCREEN · 2 × MAGEN-DARM, 2 × GELENK', 'Look 1 · Praxis · Block 1 · Skripte 09–12. Zuerst drehen, solange der Greenscreen steht. Die Hintergründe kommen im Schnitt dazu.'),
    'Murats Geschichte': ('MURATS GESCHICHTE · EMOTIONAL', 'Look 2 · privat · Block 4 · Skripte 13 und 14. Ruhig, gedämpftes Licht, echte Fotos seines Hundes. Alles in eckigen Klammern sagt Murat mit seinen echten Worten.'),
}

_KAM_WEG = re.compile(r'^(Halbnah|Nah|Von oben|Bodennah)(, ?|$)')


def _regie(kam):
    k = kam.split(' · HG: ')[0]
    k = _KAM_WEG.sub('', k).strip()
    k = re.sub(r'^Murat (sitzt im Behandlungsraum, nah, )?', 'Murat ', k) if k.startswith('Murat') else k
    return k


BLOECKE = []
nr = 0
for btitel, _btext, videos in _A['BLOECKE']:
    sk = []
    for v in videos:
        nr += 1
        takes = v['takes']
        gs = btitel == 'Greenscreen'
        zeilen = ['Murat spricht direkt in die Kamera, ein Satz pro Take.' + (' Hinter ihm läuft im Schnitt der jeweils genannte Clip.' if gs else '')]
        for kam, satz in takes[:-1]:
            gesagt = v['hooks'][0] if satz == 'HOOK' else satz
            if gs and ' · HG: ' in kam:
                zeilen.append(f'**Hintergrund: {kam.split(" · HG: ")[1]}.** Murat: „{gesagt}“')
                continue
            rg = _regie(kam)
            if rg.startswith('Murat') or 'Löffel' in rg or 'Dose' in rg:
                zeilen.append(f'{rg[0].upper() + rg[1:]}. Murat: „{gesagt}“'.replace('. Murat: „', ': „') if rg.startswith('Murat') else f'{rg}. Murat: „{gesagt}“')
            else:
                zeilen.append(f'Murat: „{gesagt}“')
        cta = takes[-1][1]
        vb = []
        if gs:
            vb.append('Stativ, halbnah vor dem Greenscreen, Murat zeigt bei Hintergrundwechseln mit dem Daumen nach hinten')
        if v.get('ort'):
            vb.append(v['ort'])
        ohne = [k for k, _ in takes if 'Ohne Hund' in k]
        if ohne:
            vb.append('Ohne Hund: ' + ohne[0].split('Ohne Hund:')[1].strip().rstrip('.'))
        if any('Löffel' in k for k, _ in takes):
            vb.append('Löffel übers Futter von oben, Handkamera, Napf vorbereiten')
        vb.append('Reserve-Hooks, direkt nach dem ersten aufnehmen: ' + ' · '.join(f'„{h}“' for h in v['hooks'][1:]))
        vb.append('CTA zwei Mal: 90 Tage für den Onlineshop, 14 Tage für TikTok')
        sk.append(dict(
            nr=f'{nr:02d}', titel=v['titel'],
            tags=f'{v["produkt"]} · Murat · {v["laenge"]}',
            kern=v['warum'],
            hook=f'Murat: „{v["hooks"][0]}“',
            ablauf=zeilen,
            ending=f'Onlineshop: „{cta}“ · TikTok: „{cta.replace("90 Tage", "14 Tage")}“',
            alt=None, vorb=vb, ad=None))
    if btitel == 'Murats Geschichte':
        sk[-1]['vorb'].insert(0, 'Vorgespräch vor dem Dreh: ' + ' · '.join(_A['VORGESPRAECH']))
    b, t = BANNER[btitel]
    BLOECKE.append(dict(banner=b, text=t, skripte=sk))
