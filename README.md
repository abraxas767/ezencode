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

Das gesamte Projekt wurde unter Beachtung von allgemein akzeptierten
Konventionen initialisiert. Da keine externen Module genutzt werden, fallen
Dinge wie requirements.txt oder setup.txt selbstverständlich raus.

_Einhaltung von Naming conventions_

Wie in PEP 8, Python styleguide, vorgegeben ist, werden Filenames, Funktionen und Variablen 
im snake_case gehalten.
private Funktionen und Variablen werden in folgendem Format angegeben:
```py
__name = "example"
def __func_name():
    print("example")
```
Konstante Variablen werden im UPPER_SNAKE_CASE gehalten:
```py
FINALE_VARIABLE = 1
```

_Nutzung des abc - module_

Python bietet zwar von sich aus keine Möglichkeit abstrakte Klassen und Interfaces einzubinden,
mit Hilfe des abc-modules ist das aber kein Problem. Dieses wurde hier verwendet um eine abstrakte
Klasse "Encoding" einzuführen, welche mindestens die Methode "encode" und "decode" implementieren
muss. 

_Nutzung von Rekursion und klar definierten Funktionen_

Um Redundanz im Code zu verhindern wurde in diesem Code an mehreren Stellen das Prinzip der Rekursion
angewendet. Insbesondere wenn es darum geht den Huffman Tree zu erstellen.
Desweiteren wurde versucht den Code so gut wie möglich aufzuteilen in prägnante Methoden mit klar 
definierter Aufgabe.

_Kommentare_


