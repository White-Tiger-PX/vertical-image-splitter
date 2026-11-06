# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

Aplikacja desktopowa do dzielenia **dowolnego obrazu na dwie pionowe części**. Okładka i grzbiet książki to tylko przykład; nazwy obu wyników można zmieniać.

![Zrzut ekranu Vertical Image Splitter](interface-illustration.png)

## Funkcje

- Precyzja co do piksela: wpisz współrzędną X lub przeciągnij czerwoną linię na podglądzie.
- Przetwarzanie plików i folderów wsadowo. **Ctrl+kliknięcie** zaznacza wiele wierszy dla **Zapisz zaznaczone**.
- Przeciąganie wierszy, stosowanie wspólnej proporcji i indywidualna korekta każdego obrazu.
- Zachowaj oryginalny format lub użyj PNG, TIFF, JPEG, WebP, BMP albo GIF.
- Opcjonalna nazwa serii i numeracja tomów.
- Oryginały pozostają nienaruszone, a nadpisywane wyniki są archiwizowane.

## Instalacja i uruchomienie

**Windows:** zainstaluj Python 3.10+ z Tkinter i uruchom `start.bat`. Pillow zostanie doinstalowany, jeśli go brakuje.

**Linux/macOS:** zainstaluj Python 3.10+ i Tkinter (w Linux często `python3-tk`), a potem:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## Użytkowanie

1. Wybierz **Plik → Dodaj obrazy…** lub **Dodaj folder…**.
2. Wybierz **Plik → Folder wyjściowy…**.
3. Nadaj nazwy części lewej i prawej (przykład po polsku: **Okładka**, **Grzbiet**).
4. Wybierz format, domyślnie **Jak w oryginale**.
5. Opcjonalnie ustaw serię i pierwszy tom w menu **Nazwy**.
6. Wpisz X w pikselach źródła lub przesuń czerwoną linię; dopasuj przyciskami ±1 px.
7. Zaznacz wiele wierszy przez Ctrl (Shift dla zakresu), następnie **Zapisz zaznaczone** lub **Utwórz wszystkie ponownie**.

## Pliki wynikowe

Przykład dla `example.png` bez serii (angielskie nazwy domyślne):

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

Nazwa serii powoduje utworzenie folderu dla każdego tomu, np. `My Series. Vol. 1/` w języku angielskim. Obie nazwy można zmienić.

## Obsługa obrazów

Skalowany jest tylko podgląd; wyniki są wycinane dokładnie w pikselach źródła. JPEG zapisuje się z jakością 100, WebP i TIFF bezstratnie. Wielostronicowe TIFF i animacje są obsługiwane przy zgodnych formatach. Konwersja może zmienić paletę, tryb kolorów i metadane.

## Języki i ustawienia

Przy pierwszym uruchomieniu interfejs jest **angielski**, niezależnie od systemu. Zmiana w menu **Język** działa od razu i zapisuje się w `settings.json` wraz z pozostałymi ustawieniami. Własne nazwy pozostają bez zmian. Nie ma automatycznego wykrywania języka ani tłumaczenia online.

## Prywatność i kopie zapasowe

Całe przetwarzanie odbywa się lokalnie, bez wysyłania obrazów. Oryginały nie są zmieniane; nadpisywane wyniki są kopiowane do datowanego podfolderu `Previous images/`. `settings.json` zawiera lokalne ścieżki i jest wykluczony przez `.gitignore`.
