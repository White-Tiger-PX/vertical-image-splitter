# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

**Herhangi bir resmi dikey olarak iki parçaya ayıran** masaüstü uygulaması. Kitap kapağı ve sırtı yalnızca bir örnektir; her iki çıktı adını da siz belirlersiniz.

![Vertical Image Splitter ekran görüntüsü](interface-illustration.png)

## Özellikler

- Piksel hassasiyetinde kesim: X koordinatı girin veya kırmızı çizgiyi sürükleyin.
- Dosyaları veya klasörleri toplu işleyin. **Ctrl+tıklama** ile çoklu seçim yapıp **Seçilenleri kaydet** kullanın.
- Satırları sürükleyerek sıralayın; aynı oranı tümüne uygulayın ve tek tek düzeltin.
- Kaynak biçimi koruyun veya PNG, TIFF, JPEG, WebP, BMP, GIF olarak kaydedin.
- İsteğe bağlı seri adı ve cilt numaraları.
- Kaynak dosyalar değişmez; üzerine yazılan sonuçlar yedeklenir.

## Kurulum ve başlatma

**Windows:** Tkinter içeren Python 3.10+ kurun, `start.bat` çalıştırın. Gerekirse Pillow yüklenir.

**Linux/macOS:** Python 3.10+ ve Tkinter (Linux’ta bazen `python3-tk`) kurun, ardından:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## Kullanım

1. **Dosya → Resim ekle…** veya **Klasör ekle…** seçin.
2. **Dosya → Çıktı klasörü…** ile hedefi belirleyin.
3. Sol ve sağ kısımların adını yazın (Türkçe varsayılan örnekler: **Kapak**, **Sırt**).
4. Biçimi seçin; varsayılan **Kaynakla aynı**.
5. İsterseniz **Adlar** menüsünden seri ve ilk cilt numarası ekleyin.
6. X değerini kaynak piksel cinsinden girin veya kırmızı çizgiyi sürükleyin; ±1 px ile ayarlayın.
7. Ctrl ile birden fazla satır seçip (Shift ile aralık), **Seçilenleri kaydet** veya **Tümünü yeniden oluştur** kullanın.

## Çıktı dosyaları

Seri olmadan `example.png` için İngilizce varsayılan isimli örnek:

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

Seri seçilirse her cilt için `My Series. Vol. 1/` (İngilizce) gibi ayrı klasör oluşturulur. Her iki ad da değiştirilebilir.

## Resim işleme

Yalnızca önizleme ölçeklenir; çıktı tam kaynak pikselinden kesilir. JPEG kalite 100, WebP ve TIFF kayıpsızdır. Desteklenen formatlarda çok sayfalı TIFF ve animasyonlar işlenir. Biçim dönüşümü renk modu, palet veya meta verileri değiştirebilir.

## Diller ve ayarlar

İlk açılışta sistem dili ne olursa olsun **İngilizce** kullanılır. **Dil** menüsünden anında değiştirilebilir ve seçim `settings.json` içinde saklanır. Özel adlar korunur. Otomatik dil algılama veya çevrimiçi çeviri yoktur.

## Gizlilik ve yedekler

Tüm işlemler yereldir; resimler yüklenmez, kaynaklar değiştirilmez. Mevcut çıktılar üzerine yazılmadan önce tarihli `Previous images/` klasörüne yedeklenir. Yerel yolları içeren `settings.json`, `.gitignore` ile hariç tutulur.
