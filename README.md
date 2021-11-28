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

### Scope

Momentan ist das Programm noch nicht sonderlich nützlich. Die eher lustig
gemeinte Morse-Codierung außen vor gelassen, fehlen noch einige essentielle
Funktionen, insbesondere bei der Huffman-Codierung. Die generierte Prefix
Tabelle wird beispielsweise nicht an den fertig komprimierten Bitstring
angefügt und geht bei Beenden des Programmes verloren. Daher kann bisher 
nur in der gleichen Session encoded und decoded werden (was nicht viel bringt).

Zur Veranschaulichung dass Komprimierungs- und Dekomprimierungslogik jedoch
schon funktioniert kann ein von Ihnen gegebener Input komprimiert und gleich
wieder dekomprimiert werden.

### Warum ist das hier meines Erachtens Clean Code?

_Einhaltung von Struktur-Konventionen_

_Einhaltung von Naming conventions_

_OOP_

_Nutzung des abc - module_

_Nutzung von Rekursion und klar definierten Funktionen_
