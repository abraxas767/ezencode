# ezencode
_easy - encode_ 

### Ein simples Datenkomprimierungs-Projekt.

Als Abgabe für _Clean Code Development_ habe ich mich etwas hinreißen lassen und
mich für Datenkomprimierung entschieden. Letztendlich habe ich die Komplexität
eines Huffman Trees in Python allerdings unterschätzt und doch einige Stunden
für die Implementierung gebraucht. Vor allem die Rekursion hat mir an vielen Stellen 
Kopfschmerzen bereitet.

Dieses Projekt implementiert bisher zwei Arten von Codierung/Kompression:
- Huffman Encoding (https://de.wikipedia.org/wiki/Huffman-Kodierung)
- Morse (https://de.wikipedia.org/wiki/Morsecode)

### Zur Ausführung auf Unix basierten System:

```bash
cd ./ezencode/module
python3 index.py
```

### Warum ist das hier meines Erachtens Clean Code?

