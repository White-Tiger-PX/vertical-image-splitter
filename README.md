# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

A lightweight desktop application for splitting any image into **two vertical parts**. Book covers and spines are just one example: you choose the names of both resulting images.

![Screenshot of Vertical Image Splitter](interface-illustration.png)

## Features

- Pixel-precise split: enter the X coordinate or drag a red line in the preview.
- Batch workflow: add individual files or an entire folder. Use **Ctrl+click** to select multiple rows and **Save selected** to export only those.
- Reorder images by dragging rows. Apply the same **relative split position** to the whole batch, then fine-tune each image.
- Choose the original image format or convert to PNG, TIFF, JPEG, WebP, BMP or GIF.
- Optional series naming and numbered volumes; otherwise the original filename is used.
- Originals are never modified. Existing output files are backed up before replacement.

## Install and run

**Windows:** install Python 3.10+ with Tkinter, then double-click `start.bat`. The launcher checks for Pillow and installs it if necessary.

**Linux/macOS:** install Python 3.10+ and Tkinter (on many Linux distributions: `python3-tk`), then run:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## How to use

1. Select **File → Add images…** or **Add folder…**.
2. Choose **File → Output folder…**.
3. Enter your own labels for the **left** and **right** parts. The initial example names are **Cover** and **Spine**.
4. Choose the output format: **Same as source** (default), PNG, TIFF, JPEG, WebP, BMP or GIF.
5. Optionally set a series name and first volume number under **Names**.
6. Set the split X in actual source-image pixels or drag the red line. Use **±1 px** for fine adjustments.
7. Select one or more rows using Ctrl (Shift for a range) and click **Save selected**, or use **Recreate all**.

## Output files

For a file named `example.png` without a series, the default settings create:

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

With a series name, each source file gets a numbered subfolder, for example `My Series. Vol. 1/`. You can rename **either** part, e.g. “Back cover” and “Spine”.

## Image handling

Only the preview is scaled; exported parts are cropped at the exact source pixel coordinate. JPEG is saved at quality 100, WebP losslessly, and TIFF with lossless compression. Multi-page TIFF and animated images are processed frame by frame when the chosen format supports it. Changing formats can change color mode, palette, metadata or compression; “Same as source” keeps the file format, not byte-for-byte identical encoding.

## Languages and settings

The app **starts in English** on first launch, regardless of the operating system language. Select any language from the **Language** menu. Your choice is applied immediately and kept in `settings.json` along with selected files, split positions, names and output preferences. Custom part names are never overwritten when switching languages. No automatic language detection, online translation or extra dependency is used.

## Privacy and backups

Processing runs locally. No images are uploaded. Source files are never edited; before replacing existing results, the old results are copied to a dated `Previous images/` subfolder. `settings.json` contains local paths and should not be committed (it is included in `.gitignore`). The application directory must be writable.
