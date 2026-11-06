# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

Applicazione desktop per dividere **qualsiasi immagine in due parti verticali**. Copertina e dorso di un libro sono solo un esempio: puoi assegnare qualsiasi nome ai due risultati.

![Schermata di Vertical Image Splitter](interface-illustration.png)

## Funzioni

- Taglio preciso: inserisci la coordinata X o trascina la linea rossa nell’anteprima.
- Elaborazione in serie di file e cartelle; con **Ctrl+clic** selezioni più righe e usi **Salva selezionate**.
- Riordina trascinando le righe, applica la stessa proporzione a tutte e regola ogni immagine.
- Mantieni il formato originale oppure usa PNG, TIFF, JPEG, WebP, BMP o GIF.
- Serie e numerazione dei volumi facoltative.
- Originali intatti e backup dei risultati sovrascritti.

## Installazione e avvio

**Windows:** installa Python 3.10+ con Tkinter, poi avvia `start.bat`. Pillow viene installato se necessario.

**Linux/macOS:** installa Python 3.10+ e Tkinter (spesso `python3-tk` su Linux), poi:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## Utilizzo

1. Apri **File → Aggiungi immagini…** o **Aggiungi cartella…**.
2. Seleziona **File → Cartella di destinazione…**.
3. Imposta i nomi delle parti sinistra e destra (predefiniti: **Copertina**, **Dorso**).
4. Scegli il formato: **Come originale** è quello iniziale.
5. Facoltativamente imposta serie e primo volume in **Nomi**.
6. Inserisci X in pixel o sposta la linea rossa, usando ±1 px per la precisione.
7. Seleziona più righe con Ctrl (Shift per un intervallo), poi **Salva selezionate** o **Ricrea tutte**.

## File generati

Per `example.png`, senza serie, esempio con nomi inglesi:

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

Con una serie, ogni volume riceve una cartella dedicata, ad esempio `My Series. Vol. 1/` in inglese. Entrambi i nomi sono modificabili.

## Gestione delle immagini

Solo l’anteprima viene ridimensionata; i file vengono ritagliati sui pixel originali. JPEG a qualità 100, WebP e TIFF senza perdita. TIFF multipagina e animazioni sono elaborati se il formato di output lo permette. La conversione può modificare tavolozza, colore e metadati.

## Lingue e impostazioni

Al primo avvio la lingua è **inglese**, a prescindere dal sistema. Il menu **Lingua** cambia subito la lingua e la salva in `settings.json`. I nomi personalizzati non vengono sovrascritti. Nessun rilevamento automatico o servizio online.

## Privacy e backup

Tutto avviene offline, senza caricare immagini. Gli originali restano invariati. Prima di sovrascrivere un risultato, viene salvata una copia in una sottocartella datata `Previous images/`. `settings.json` contiene percorsi locali ed è escluso da Git.
