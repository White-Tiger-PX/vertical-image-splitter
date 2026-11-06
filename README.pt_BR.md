# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

Aplicativo para dividir **qualquer imagem em duas partes verticais**. Capas e lombadas de livros são apenas um exemplo; os dois nomes podem ser personalizados.

![Captura de tela do Vertical Image Splitter](interface-illustration.png)

## Recursos

- Corte preciso: informe X em pixels ou arraste a linha vermelha na prévia.
- Processamento em lote de arquivos e pastas. Use **Ctrl+clique** para selecionar várias linhas e **Salvar selecionados**.
- Reordene arrastando linhas; aplique a mesma proporção a todas e ajuste cada imagem.
- Salve no formato original ou em PNG, TIFF, JPEG, WebP, BMP ou GIF.
- Nome de série e numeração de volumes opcionais.
- Os arquivos originais não são alterados; resultados substituídos recebem backup.

## Instalação e execução

**Windows:** instale Python 3.10+ com Tkinter e execute `start.bat`. O iniciador instala Pillow caso necessário.

**Linux/macOS:** instale Python 3.10+ e Tkinter (`python3-tk` em muitas distribuições Linux) e execute:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## Como usar

1. Abra **Arquivo → Adicionar imagens…** ou **Adicionar pasta…**.
2. Escolha **Arquivo → Pasta de saída…**.
3. Defina os nomes das partes esquerda e direita (padrão: **Capa**, **Lombada**).
4. Escolha o formato; o padrão é **Igual ao original**.
5. Opcionalmente, configure série e primeiro volume em **Nomes**.
6. Digite X em pixels do original ou arraste a linha vermelha; ajuste com ±1 px.
7. Selecione várias linhas com Ctrl (Shift para intervalo) e clique em **Salvar selecionados** ou **Recriar todos**.

## Arquivos gerados

Para `example.png`, sem série, exemplo com nomes em inglês:

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

Com uma série, cada volume ganha sua própria pasta, como `My Series. Vol. 1/` em inglês. Ambos os nomes são editáveis.

## Processamento de imagem

Somente a prévia é redimensionada; o recorte salvo usa os pixels exatos. JPEG usa qualidade 100; WebP e TIFF usam compressão sem perdas. TIFF com várias páginas e animações são tratados quadro a quadro se o formato escolhido permitir. A conversão pode alterar paleta, cores e metadados.

## Idiomas e configurações

Na primeira execução, o idioma é **inglês**, independentemente do sistema. O menu **Idioma** altera a interface imediatamente e salva a escolha em `settings.json`. Nomes personalizados são preservados. Não há detecção automática nem tradução online.

## Privacidade e backups

Todo o processamento é local, sem enviar imagens. Os originais não são modificados. Antes de sobrescrever resultados, os anteriores são copiados para uma subpasta datada `Previous images/`. `settings.json` armazena caminhos locais e está no `.gitignore`.
