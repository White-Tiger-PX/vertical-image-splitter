# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

**画像を縦方向に2分割**できるデスクトップアプリです。書籍の表紙と背表紙は用途の一例にすぎず、出力名は自由に設定できます。

![Vertical Image Splitter のスクリーンショット](interface-illustration.png)

## 機能

- ピクセル単位で分割：X座標を入力するか、プレビューの赤い線をドラッグ。
- ファイルやフォルダーを一括追加。**Ctrl+クリック**で複数行を選び、**選択項目を保存**。
- ドラッグで並べ替え、共通の幅比率を適用した後に各画像を微調整。
- 元形式のまま、または PNG・TIFF・JPEG・WebP・BMP・GIF で保存。
- シリーズ名や巻番号は任意。未設定なら元のファイル名を使用。
- 元画像は変更せず、既存の出力を上書きする前にバックアップ。

## インストールと起動

**Windows：** Tkinter付きPython 3.10以降をインストールし、`start.bat` を起動します。必要ならPillowを自動でインストールします。

**Linux/macOS：** Python 3.10以降とTkinter（Linuxでは `python3-tk` が必要な場合あり）をインストールし、次を実行：

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## 使い方

1. **ファイル → 画像を追加…** または **フォルダーを追加…** を選択。
2. **ファイル → 保存先フォルダー…** で出力先を指定。
3. 左右の名前を入力（日本語での初期例：**表紙**、**背表紙**）。
4. 出力形式を選択。初期設定は **元画像と同じ**。
5. 必要に応じて **名前** メニューからシリーズ名と巻番号を設定。
6. 元画像のX座標を入力するか赤い線を移動し、±1 pxで調整。
7. Ctrlで複数行（Shiftで範囲）を選択し、**選択項目を保存** または **すべて再作成**。

## 出力ファイル

シリーズなしの `example.png` の出力例（英語の初期名）：

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

シリーズ名を指定すると、英語表示では `My Series. Vol. 1/` のように巻ごとのフォルダーが作られます。両方の名前は変更可能です。

## 画像処理

拡大縮小するのはプレビューだけで、出力は元画像のピクセル位置で切り取ります。JPEGは品質100、WebPとTIFFは可逆圧縮です。対応形式では複数ページのTIFFやアニメーションも処理します。変換によって色モード、パレット、メタデータが変わる場合があります。

## 言語と設定

初回起動時はOSの言語に関係なく**英語**です。**言語**メニューで即座に切り替えられ、選択内容は `settings.json` に保存されます。カスタム名は変更されません。自動言語判定やオンライン翻訳は使いません。

## プライバシーとバックアップ

すべてローカルで処理し、画像をアップロードしません。元画像も変更しません。出力を上書きする前に `Previous images/` の日付付きフォルダーへ退避します。ローカルパスを含む `settings.json` は `.gitignore` で除外されます。
