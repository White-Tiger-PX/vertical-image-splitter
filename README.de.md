# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

Desktop-Anwendung zum Teilen **beliebiger Bilder in zwei vertikale Teile**. Buchcover und Buchrücken sind nur ein Beispiel; beide Dateinamen lassen sich frei wählen.

![Bildschirmfoto von Vertical Image Splitter](interface-illustration.png)

## Funktionen

- Pixelgenau: X-Koordinate eingeben oder rote Linie im Vorschaubild ziehen.
- Stapelverarbeitung von Dateien und Ordnern. Mit **Strg+Klick** mehrere Zeilen auswählen und **Auswahl speichern** drücken.
- Zeilen ziehen, einen proportionalen Schnitt auf alle anwenden und jedes Bild einzeln nachstellen.
- Originalformat beibehalten oder PNG, TIFF, JPEG, WebP, BMP bzw. GIF wählen.
- Optionaler Reihenname und Bandnummern.
- Quelldateien werden nicht verändert; ersetzte Ergebnisse werden gesichert.

## Installation und Start

**Windows:** Python 3.10+ mit Tkinter installieren und `start.bat` ausführen. Pillow wird bei Bedarf per pip installiert.

**Linux/macOS:** Python 3.10+ und Tkinter installieren (unter Linux oft `python3-tk`), danach:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## Bedienung

1. **Datei → Bilder hinzufügen…** oder **Ordner hinzufügen…** wählen.
2. Unter **Datei → Ausgabeordner…** den Zielordner auswählen.
3. Linken und rechten Teil benennen (Beispiel: **Cover**, **Buchrücken**).
4. Ausgabeformat auswählen; standardmäßig **Wie Original**.
5. Optional Reihenname und Bandnummer unter **Namen** festlegen.
6. X in Originalpixeln eingeben oder rote Linie ziehen; ±1 px zur Feinjustierung.
7. Mit Strg mehrere Zeilen wählen (mit Umschalt einen Bereich) und **Auswahl speichern** oder **Alle neu erstellen** klicken.

## Ergebnisdateien

Für `example.png` ohne Reihe ergibt sich das folgende Beispiel mit englischen Teilnamen:

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

Mit Reihenname entsteht pro Band ein eigener Ordner, z. B. `My Series. Vol. 1/` auf Englisch. Beide Namen sind frei editierbar.

## Bildverarbeitung

Nur die Vorschau wird skaliert, die Ausgabe exakt bei X Originalpixeln zugeschnitten. JPEG wird mit Qualität 100 gespeichert, WebP und TIFF verlustfrei. Mehrseitige TIFFs und Animationen werden bei kompatiblen Formaten vollständig verarbeitet. Formatwechsel können Farbmodus, Palette und Metadaten ändern.

## Sprachen und Einstellungen

Beim ersten Start ist die Oberfläche **Englisch**, unabhängig von Windows. Über **Sprache** kann sofort gewechselt werden. Die Auswahl wird zusammen mit Einstellungen und lokalen Pfaden in `settings.json` gespeichert. Eigene Teilnamen bleiben erhalten. Keine automatische Spracherkennung oder Onlineübersetzung.

## Datenschutz und Sicherungen

Die Verarbeitung erfolgt ausschließlich lokal. Originale bleiben unverändert; vorherige Ergebnisse werden vor dem Ersetzen im datierten Unterordner `Previous images/` gesichert. `settings.json` enthält lokale Pfade und wird per `.gitignore` ausgeschlossen.
