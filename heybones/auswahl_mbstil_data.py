"""Hey Bones Auswahl im Stil des MonBerg-Drehplans (mb_render.py)."""
import os, runpy
_A = runpy.run_path(os.path.join(os.path.dirname(__file__), 'auswahl_data.py'))


def _tc(sek):
    s = int(round(sek))
    return f'{s // 60}:{s % 60:02d}'


def _dauer(text):
    return max(1.5, len(text.split()) / 2.6 + 0.4)


KOPF = 'Hey Bones · Drehskripte · Stand 23.11. · 2026-1123-HB-D'
TITEL = 'Hey Bones · Drehskripte'
UNTER = 'AUSWAHL · 14 SKRIPTE SATZ FÜR SATZ · STAND 23.11.2026'
ABLAUF_LAB = 'Sprechtext Satz für Satz'
REIHE_H = ('BLOCK', 'SKRIPTE', 'ORT')

INTRO = [
    ('Absicht des Drehs',
     'Murat spricht als Chiropraktiker und Gründer direkt in die Kamera. Jedes Video folgt derselben Mechanik: ein provokanter Hook, ein Zeichen, das jeder Halter kennt, '
     'die Erklärung aus der Praxis, dann Hey Bones als tägliche Routine und der CTA. Die Sätze stehen wörtlich da und werden einzeln aufgenommen.'),
    ('Format & Ziellänge',
     'Hochkant 9:16. Sprechzeit je Video ca. 28–33 Sekunden, Greenscreen ca. 34–39 Sekunden, Murats Geschichte bis ca. 45 Sekunden.'),
    ('Für alle Videos',
     'Murat stellt sich nicht jedes Mal vor. Nennt er seinen Beruf, dann Chiropraktiker. Dosierung immer: ein Löffel pro 10 Kilo übers Futter. '
     'Keine Heilversprechen: „unterstützen“, nie „heilt“ oder „weg“. Der CTA wird zwei Mal aufgenommen: 90 Tage für den Onlineshop, 14 Tage für TikTok.'),
]

LOOKS = [
    ('Murat', 'Praxiskleidung, wie er auch Hunde behandelt', 'In allen Videos gleich. Für Murats Geschichte gern privater, ruhiger.'),
    ('Requisiten', 'Dosen Magen-Darm und Gelenk, Löffel, Napf mit Futter, Plätzchenteller (04), zwei Futtersäcke (03), Fotos von Murats Hund (13, 14)', 'Den Napf für die Löffel-Einstellung von oben vorbereiten.'),
]
LOOK_HINWEIS = 'Mit Hund wirken die Videos stärker, alle gehen aber auch ohne Hund. Hinweise dazu stehen jeweils in der Drehvorbereitung.'

REIHENFOLGE_TEXT = 'Erst der Greenscreen, solange er steht. Dann die Praxis, dann das Auto, solange es hell ist. Murats Geschichte zum Schluss, in Ruhe.'
REIHENFOLGE = [
    ('Block 1 · Greenscreen', '09 Gras fressen · 10 Gelber Schaum · 11 Steif nach dem Aufstehen · 12 Treppe & Kofferraum', 'Praxis, Greenscreen'),
    ('Block 2 · Praxis', '01 Drei Fragen · 02 Schlingen · 03 Mythos Abwechslung · 04 Festtage · 05 Wie er aufsteht · 06 Glatte Böden · 08 Nach der Behandlung', 'Behandlungsraum'),
    ('Block 3 · Am Auto', '07 Kalter Kofferraum', 'Vor der Praxis, bei Tageslicht'),
    ('Block 4 · Murats Geschichte', '13 Warum es Hey Bones gibt · 14 Das Foto', 'Ruhiger Raum, gedämpftes Licht'),
]
KLAEREN = []

BANNER = {
    'Magen-Darm': 'MAGEN-DARM · PRAXIS',
    'Gelenk': 'GELENK · PRAXIS UND AUTO',
    'Greenscreen': 'GREENSCREEN · 2 × MAGEN-DARM, 2 × GELENK',
    'Murats Geschichte': 'MURATS GESCHICHTE · EMOTIONAL',
}

BLOECKE = []
nr = 0
for btitel, btext, videos in _A['BLOECKE']:
    sk = []
    for v in videos:
        nr += 1
        zeit = 0.0
        zeilen = []
        takes = v['takes']
        for i, (kam, satz) in enumerate(takes):
            gesagt = v['hooks'][0] if satz == 'HOOK' else satz
            hg = ''
            if ' · HG: ' in kam:
                kam, hg = kam.split(' · HG: ', 1)
                hg = f' · Hintergrund: {hg}'
            bis = zeit + _dauer(gesagt)
            if i < len(takes) - 1:
                zeilen.append(f'Murat: „{gesagt}“ ({kam}{hg})')
                zeit = bis
        letzter = takes[-1][1]
        ende = _tc(zeit + _dauer(letzter))
        vorb = (v['warum'] + ' Kamera beim CTA: ' + takes[-1][0] + '. '
                'Alternative Hooks, direkt nach dem ersten Hook aufnehmen: '
                + ' · '.join(f'„{h}“' for h in v['hooks'][1:]) + '.')
        if v.get('ort'):
            vorb = v['ort'] + '. ' + vorb
        sk.append(dict(
            nr=f'{nr:02d}', titel=v['titel'],
            tags=f'{v["produkt"]} · Sprechzeit ca. {int(round(zeit + _dauer(letzter)))} s · Murat',
            hook=f'Murat: „{v["hooks"][0]}“',
            ablauf=zeilen,
            ending=f'Onlineshop: „{letzter}“',
            alt=f'TikTok-Fassung, gleich danach aufnehmen: „{letzter.replace("90 Tage", "14 Tage")}“',
            vorb=vorb, ad=None))
    text = btext
    if btitel == 'Murats Geschichte':
        text += ' Vorgespräch vor dem Dreh: ' + ' · '.join(_A['VORGESPRAECH'])
    BLOECKE.append(dict(banner=BANNER[btitel], text=text, skripte=sk))
