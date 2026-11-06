"""Built-in UI translations; no network connection or extra packages required.

English is the first-run default. The selected language is stored in settings.json.
"""
from __future__ import annotations

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
    'es': 'Español',
    'de': 'Deutsch',
    'fr': 'Français',
    'pt_BR': 'Português (Brasil)',
    'it': 'Italiano',
    'zh_CN': '简体中文',
    'ja': '日本語',
    'ko': '한국어',
    'tr': 'Türkçe',
    'pl': 'Polski',
}

# All user-facing strings, including core validation errors, share stable keys.
EN = {
    'window_title': 'Vertical Image Splitter',
    'menu_file': 'File', 'menu_add_files': 'Add images…', 'menu_add_folder': 'Add folder…',
    'menu_output': 'Output folder…', 'menu_remove': 'Remove selected',
    'menu_clear': 'Clear list', 'menu_exit': 'Exit',
    'menu_names': 'Names', 'menu_series': 'Series name…',
    'menu_number': 'First volume number…', 'menu_language': 'Language',
    'intro': 'File → Add images → set split X in pixels or drag the red line → save.',
    'output_at': 'Output folder: {path}', 'output_missing': 'Output folder not selected',
    'left_part': 'Left part:', 'right_part': 'Right part:',
    'output_format': 'Save format:', 'as_source': 'Same as source',
    'col_no': 'No.', 'col_title': 'Name', 'col_source': 'Source',
    'col_x': 'X', 'col_right': 'Right, px',
    'remove_btn': 'Remove',
    'hint': 'Drag rows to change order.\nX is measured from the source image’s left edge.\nLeft part: before the line; right part: after it.',
    'split_x': 'Split X:', 'apply_ratio': 'Apply ratio to all',
    'save_selected': 'Save selected', 'recreate_all': 'Recreate all',
    'ready_status': 'Split settings are saved automatically.',
    'choose_images': 'Select images', 'image_files': 'Images', 'all_files': 'All files',
    'choose_folder': 'Folder with source images', 'choose_output': 'Select output folder',
    'series_title': 'Series name',
    'series_prompt': 'Series name (leave empty to use original filenames):',
    'number_title': 'Numbering', 'number_prompt': 'First volume number:',
    'files_added': '{count} images. Drag rows to reorder them.',
    'order_changed': 'Order saved. Series numbering updated; splits stayed with their images.',
    'list_cleared': 'List cleared. No files on disk were changed.',
    'missing_source': 'Source image unavailable', 'add_first': 'Add images via the File menu',
    'no_files': 'No files',
    'image_info': 'Source {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}',
    'ratio_applied': 'Applied {percent:.4f}% of width to every image. Actual X values are in the table.',
    'save_title': 'Save', 'choose_rows': 'Select one or more images in the list.',
    'split_title': 'Split position',
    'invalid_split': 'Enter an integer X between 1 and the image width minus 1.',
    'labels_title': 'Part names', 'destination_title': 'Output folder',
    'drive_missing': 'Drive unavailable: {path}', 'titles_title': 'Names',
    'duplicate_names': 'Duplicate output names. Set a series name in Names so files receive unique numbers.',
    'saved_status': 'Processed {done} images, wrote {files} files. Folder: {path}',
    'skipped_title': 'Skipped files', 'done_title': 'Done',
    'saved_message': 'Saved {files} files in\n{path}',
    'volume_format': '{series}. Vol. {number}',
    'default_left': 'Cover', 'default_right': 'Spine',
    'core_width': 'Image width must be at least 2 pixels.',
    'core_fraction': 'The split ratio must be between 0 and 1.',
    'core_empty_name': 'The filename must not be empty.',
    'core_same_labels': 'The left and right part names must be different.',
    'core_unknown_format': 'Unknown output format: {format}',
    'core_unsupported_format': 'Source format {format} cannot be saved. Choose another output format.',
    'core_multi_frame': 'Source has multiple frames/pages. Use the source format, TIFF, PNG, WebP or GIF.',
    'core_var_width': 'Pages have different widths. Split them into separate source files.',
}

# The translated rows follow these keys exactly. A validation check below prevents
# missing or mismatched translations. Literal \\n becomes an actual line break.
KEYS = list(EN)
RAW = {
'ru': r'''Vertical Image Splitter
Файл
Добавить изображения…
Добавить папку…
Папка сохранения…
Убрать выбранное
Очистить список
Выход
Названия
Название серии…
Номер первого тома…
Язык
Файл → Добавить изображения → задай X в пикселях или перетащи красную линию → сохрани.
Сохранение: {path}
Папка сохранения не выбрана
Левая часть:
Правая часть:
Формат сохранения:
Как у исходника
№
Название
Исходник
X
Правая, пикс.
Убрать
Перетаскивай строки для изменения порядка.\nX — от левого края исходника.\nЛевая часть — до линии, правая — после.
Разрез X:
Применить долю ко всем
Сохранить выбранное
Пересоздать все
Настройки разреза сохраняются автоматически.
Выбери изображения
Изображения
Все файлы
Папка с исходными изображениями
Выбери папку сохранения
Название серии
Название серии (пусто — имена исходных файлов):
Нумерация
Номер первого тома:
Изображений: {count}. Порядок можно менять перетаскиванием строк мышью.
Порядок сохранён. Нумерация обновлена, разрезы остались у своих изображений.
Список очищен. Файлы на диске не изменены.
Исходник недоступен
Добавь изображения через меню «Файл»
Нет файлов
Исходник {w}×{h}  |  X = {x} пикс.  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
Ко всем изображениям применено {percent:.4f}% ширины. Значения X показаны в таблице.
Сохранение
Выбери одно или несколько изображений в списке.
Разрез
Введи целое число X от 1 до ширины изображения минус 1.
Названия частей
Папка сохранения
Диск недоступен: {path}
Названия
Одинаковые имена результатов. Задай название серии, чтобы файлы получили разные номера.
Обработано {done} изображений, сохранено {files} файлов. Папка: {path}
Пропущенные файлы
Готово
Сохранено {files} файлов в\n{path}
{series}. Том {number}
Обложка
Корешок
Ширина изображения должна быть не меньше двух пикселей.
Доля ширины должна быть между 0 и 1.
Название файла не должно быть пустым.
Названия левой и правой частей должны различаться.
Неизвестный формат сохранения: {format}
Сохранение в исходный формат {format} не поддерживается. Выбери другой формат.
В исходнике несколько кадров/страниц. Выбери исходный формат, TIFF, PNG, WebP или GIF.
У страниц разная ширина. Раздели их на отдельные исходники.''',
'es': r'''Vertical Image Splitter
Archivo
Añadir imágenes…
Añadir carpeta…
Carpeta de destino…
Quitar selección
Vaciar lista
Salir
Nombres
Nombre de la serie…
Número del primer volumen…
Idioma
Archivo → Añadir imágenes → ajusta X en píxeles o arrastra la línea roja → guarda.
Carpeta de destino: {path}
No se ha elegido una carpeta de destino
Parte izquierda:
Parte derecha:
Formato de salida:
Igual que el original
N.º
Nombre
Original
X
Derecha, px
Quitar
Arrastra las filas para reordenarlas.\nX se mide desde el borde izquierdo.\nLa parte izquierda queda antes de la línea y la derecha después.
Corte X:
Aplicar proporción a todas
Guardar selección
Recrear todas
Los ajustes de corte se guardan automáticamente.
Seleccionar imágenes
Imágenes
Todos los archivos
Carpeta con imágenes originales
Seleccionar carpeta de destino
Nombre de la serie
Nombre de la serie (vacío: nombres originales):
Numeración
Número del primer volumen:
{count} imágenes. Arrastra las filas para cambiar el orden.
Orden guardado. Se actualizó la numeración y se conservaron los cortes.
Lista vaciada. Los archivos del disco no se han modificado.
Imagen original no disponible
Añade imágenes desde Archivo
Sin archivos
Original {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
Se aplicó el {percent:.4f}% del ancho a todas las imágenes. Los valores X están en la tabla.
Guardar
Selecciona una o varias imágenes de la lista.
Posición de corte
Introduce un X entero entre 1 y el ancho de la imagen menos 1.
Nombres de las partes
Carpeta de destino
Unidad no disponible: {path}
Nombres
Hay nombres de salida duplicados. Define una serie para usar números únicos.
Procesadas {done} imágenes; {files} archivos guardados. Carpeta: {path}
Archivos omitidos
Listo
Se guardaron {files} archivos en\n{path}
{series}. Vol. {number}
Portada
Lomo
La imagen debe tener al menos 2 píxeles de ancho.
La proporción de corte debe estar entre 0 y 1.
El nombre del archivo no puede estar vacío.
Los nombres de las partes deben ser distintos.
Formato de salida desconocido: {format}
No se puede guardar el formato original {format}. Elige otro formato.
El original tiene varias páginas/fotogramas. Usa el formato original, TIFF, PNG, WebP o GIF.
Las páginas tienen anchuras distintas. Sepáralas en archivos individuales.''',
'de': r'''Vertical Image Splitter
Datei
Bilder hinzufügen…
Ordner hinzufügen…
Ausgabeordner…
Auswahl entfernen
Liste leeren
Beenden
Namen
Reihenname…
Nummer des ersten Bandes…
Sprache
Datei → Bilder hinzufügen → X in Pixeln festlegen oder rote Linie ziehen → speichern.
Ausgabeordner: {path}
Kein Ausgabeordner ausgewählt
Linker Teil:
Rechter Teil:
Ausgabeformat:
Wie Original
Nr.
Name
Original
X
Rechts, px
Entfernen
Zeilen ziehen, um sie zu sortieren.\nX wird vom linken Bildrand gemessen.\nLinks liegt vor der Linie, rechts dahinter.
Trennlinie X:
Anteil auf alle anwenden
Auswahl speichern
Alle neu erstellen
Trenneinstellungen werden automatisch gespeichert.
Bilder auswählen
Bilder
Alle Dateien
Ordner mit Quellbildern
Ausgabeordner auswählen
Reihenname
Reihenname (leer: Originaldateinamen verwenden):
Nummerierung
Nummer des ersten Bandes:
{count} Bilder. Zeilen zum Sortieren ziehen.
Reihenfolge gespeichert. Bandnummerierung aktualisiert; Schnittpositionen beibehalten.
Liste geleert. Dateien auf dem Datenträger bleiben unverändert.
Quellbild nicht verfügbar
Bilder über Datei hinzufügen
Keine Dateien
Original {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
{percent:.4f}% der Breite auf alle Bilder angewendet. Die X-Werte stehen in der Tabelle.
Speichern
Ein oder mehrere Bilder in der Liste auswählen.
Trennposition
Eine ganze Zahl X zwischen 1 und Bildbreite minus 1 eingeben.
Teilnamen
Ausgabeordner
Laufwerk nicht verfügbar: {path}
Namen
Doppelte Ausgabenamen. Eine Reihe angeben, um eindeutige Nummern zu erhalten.
{done} Bilder verarbeitet, {files} Dateien gespeichert. Ordner: {path}
Übersprungene Dateien
Fertig
{files} Dateien gespeichert in\n{path}
{series}. Bd. {number}
Cover
Buchrücken
Das Bild muss mindestens 2 Pixel breit sein.
Der Schnittanteil muss zwischen 0 und 1 liegen.
Der Dateiname darf nicht leer sein.
Die Teilnamen müssen unterschiedlich sein.
Unbekanntes Ausgabeformat: {format}
Quellformat {format} kann nicht gespeichert werden. Anderes Format wählen.
Mehrere Seiten/Frames vorhanden. Quellformat, TIFF, PNG, WebP oder GIF wählen.
Seiten haben unterschiedliche Breiten. Als einzelne Dateien aufteilen.''',
'fr': r'''Vertical Image Splitter
Fichier
Ajouter des images…
Ajouter un dossier…
Dossier de sortie…
Retirer la sélection
Vider la liste
Quitter
Noms
Nom de la série…
Numéro du premier tome…
Langue
Fichier → Ajouter des images → régler X en pixels ou déplacer la ligne rouge → enregistrer.
Dossier de sortie : {path}
Aucun dossier de sortie sélectionné
Partie gauche :
Partie droite :
Format de sortie :
Identique à la source
N°
Nom
Source
X
Droite, px
Retirer
Faites glisser les lignes pour changer leur ordre.\nX se mesure depuis le bord gauche.\nLa partie gauche est avant la ligne, la droite après.
Coupe X :
Appliquer le ratio à toutes
Enregistrer la sélection
Tout recréer
Les positions de coupe sont enregistrées automatiquement.
Choisir des images
Images
Tous les fichiers
Dossier des images source
Choisir le dossier de sortie
Nom de la série
Nom de la série (vide : noms des fichiers source) :
Numérotation
Numéro du premier tome :
{count} images. Faites glisser les lignes pour les réordonner.
Ordre enregistré. Numérotation actualisée ; coupes conservées.
Liste vidée. Aucun fichier sur le disque n'a été modifié.
Image source indisponible
Ajoutez des images avec le menu Fichier
Aucun fichier
Source {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
{percent:.4f} % de la largeur appliqués à toutes les images. Les valeurs X sont dans le tableau.
Enregistrement
Sélectionnez une ou plusieurs images dans la liste.
Position de coupe
Saisissez un entier X de 1 à largeur de l'image moins 1.
Noms des parties
Dossier de sortie
Lecteur indisponible : {path}
Noms
Noms de sortie identiques. Définissez une série pour attribuer des numéros distincts.
{done} images traitées, {files} fichiers enregistrés. Dossier : {path}
Fichiers ignorés
Terminé
{files} fichiers enregistrés dans\n{path}
{series}. T. {number}
Couverture
Dos
La largeur de l'image doit être d'au moins 2 pixels.
Le ratio de coupe doit être entre 0 et 1.
Le nom du fichier ne peut pas être vide.
Les noms des deux parties doivent être différents.
Format de sortie inconnu : {format}
Le format source {format} ne peut être enregistré. Choisissez un autre format.
Source multipage/animée. Utilisez le format source, TIFF, PNG, WebP ou GIF.
Les pages ont des largeurs différentes. Séparez les fichiers source.''',
'pt_BR': r'''Vertical Image Splitter
Arquivo
Adicionar imagens…
Adicionar pasta…
Pasta de saída…
Remover selecionados
Limpar lista
Sair
Nomes
Nome da série…
Número do primeiro volume…
Idioma
Arquivo → Adicionar imagens → defina X em pixels ou arraste a linha vermelha → salve.
Pasta de saída: {path}
Nenhuma pasta de saída selecionada
Parte esquerda:
Parte direita:
Formato de saída:
Igual ao original
Nº
Nome
Original
X
Direita, px
Remover
Arraste as linhas para reordenar.\nX é medido a partir da borda esquerda.\nA parte esquerda fica antes da linha e a direita depois.
Corte X:
Aplicar proporção a todas
Salvar selecionados
Recriar todos
As configurações de corte são salvas automaticamente.
Selecionar imagens
Imagens
Todos os arquivos
Pasta com imagens originais
Selecionar pasta de saída
Nome da série
Nome da série (vazio: nomes dos arquivos originais):
Numeração
Número do primeiro volume:
{count} imagens. Arraste as linhas para reordenar.
Ordem salva. Numeração atualizada; cortes preservados.
Lista limpa. Os arquivos no disco não foram alterados.
Imagem original indisponível
Adicione imagens pelo menu Arquivo
Nenhum arquivo
Original {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
{percent:.4f}% da largura aplicado a todas as imagens. Os valores X estão na tabela.
Salvar
Selecione uma ou mais imagens na lista.
Posição do corte
Digite um X inteiro entre 1 e a largura da imagem menos 1.
Nomes das partes
Pasta de saída
Unidade indisponível: {path}
Nomes
Nomes de saída repetidos. Defina uma série para gerar números diferentes.
{done} imagens processadas, {files} arquivos salvos. Pasta: {path}
Arquivos ignorados
Concluído
{files} arquivos salvos em\n{path}
{series}. Vol. {number}
Capa
Lombada
A imagem deve ter pelo menos 2 pixels de largura.
A proporção do corte deve estar entre 0 e 1.
O nome do arquivo não pode ficar vazio.
Os nomes das partes devem ser diferentes.
Formato de saída desconhecido: {format}
O formato original {format} não pode ser salvo. Escolha outro formato.
A origem tem várias páginas/quadros. Use o formato original, TIFF, PNG, WebP ou GIF.
As páginas têm larguras diferentes. Separe em arquivos individuais.''',
'it': r'''Vertical Image Splitter
File
Aggiungi immagini…
Aggiungi cartella…
Cartella di destinazione…
Rimuovi selezionate
Svuota elenco
Esci
Nomi
Nome della serie…
Numero del primo volume…
Lingua
File → Aggiungi immagini → imposta X in pixel o trascina la linea rossa → salva.
Cartella di destinazione: {path}
Nessuna cartella di destinazione selezionata
Parte sinistra:
Parte destra:
Formato di salvataggio:
Come originale
N.
Nome
Originale
X
Destra, px
Rimuovi
Trascina le righe per riordinarle.\nX è misurata dal bordo sinistro.\nLa parte sinistra è prima della linea, la destra dopo.
Taglio X:
Applica proporzione a tutte
Salva selezionate
Ricrea tutte
Le impostazioni di taglio vengono salvate automaticamente.
Seleziona immagini
Immagini
Tutti i file
Cartella delle immagini originali
Seleziona cartella di destinazione
Nome della serie
Nome della serie (vuoto: nomi dei file originali):
Numerazione
Numero del primo volume:
{count} immagini. Trascina le righe per riordinarle.
Ordine salvato. Numerazione aggiornata; tagli invariati.
Elenco svuotato. Nessun file sul disco è stato modificato.
Immagine originale non disponibile
Aggiungi immagini dal menu File
Nessun file
Originale {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
Applicato il {percent:.4f}% della larghezza a tutte le immagini. I valori X sono nella tabella.
Salva
Seleziona una o più immagini nell'elenco.
Posizione di taglio
Inserisci un X intero tra 1 e larghezza dell'immagine meno 1.
Nomi delle parti
Cartella di destinazione
Unità non disponibile: {path}
Nomi
Nomi di output duplicati. Imposta una serie per ottenere numeri univoci.
Elaborate {done} immagini, salvati {files} file. Cartella: {path}
File saltati
Fatto
Salvati {files} file in\n{path}
{series}. Vol. {number}
Copertina
Dorso
L'immagine deve essere larga almeno 2 pixel.
La proporzione deve essere compresa tra 0 e 1.
Il nome del file non può essere vuoto.
I nomi delle due parti devono essere diversi.
Formato di salvataggio sconosciuto: {format}
Impossibile salvare il formato originale {format}. Scegli un altro formato.
La sorgente ha più pagine/fotogrammi. Usa il formato originale, TIFF, PNG, WebP o GIF.
Le pagine hanno larghezze diverse. Separale in file individuali.''',
'zh_CN': r'''Vertical Image Splitter
文件
添加图片…
添加文件夹…
输出文件夹…
移除所选
清空列表
退出
命名
系列名称…
首卷编号…
语言
文件 → 添加图片 → 输入像素位置 X 或拖动红线 → 保存。
输出文件夹：{path}
尚未选择输出文件夹
左侧部分：
右侧部分：
保存格式：
与原图相同
序号
名称
原图
X
右侧，像素
移除
拖动行可调整顺序。\nX 从原图左边缘开始计算。\n左侧为线前部分，右侧为线后部分。
切割位置 X：
将比例应用到全部
保存所选
重新生成全部
切割设置会自动保存。
选择图片
图片
所有文件
原图所在文件夹
选择输出文件夹
系列名称
系列名称（留空使用原文件名）：
编号
首卷编号：
共 {count} 张图片。拖动行可调整顺序。
顺序已保存。卷号已更新，切割位置保持不变。
列表已清空。磁盘文件未修改。
无法访问原图
请从“文件”菜单添加图片
没有文件
原图 {w}×{h}  |  X = {x} 像素  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
已将宽度比例 {percent:.4f}% 应用于所有图片。实际 X 值见列表。
保存
请在列表中选择一张或多张图片。
切割位置
请输入 1 到图像宽度减 1 之间的整数 X。
部分名称
输出文件夹
驱动器不可用：{path}
命名
输出名称重复。请设置系列名称，以生成不同的编号。
已处理 {done} 张图片，保存 {files} 个文件。文件夹：{path}
跳过的文件
完成
已将 {files} 个文件保存到\n{path}
{series} 第{number}卷
封面
书脊
图片宽度至少为 2 像素。
切割比例必须在 0 和 1 之间。
文件名不能为空。
左右部分名称不能相同。
未知输出格式：{format}
无法保存原始格式 {format}。请选择其他格式。
原图含多个页面/帧。请使用原始格式、TIFF、PNG、WebP 或 GIF。
页面宽度不同。请将其拆为单独文件。''',
'ja': r'''Vertical Image Splitter
ファイル
画像を追加…
フォルダーを追加…
保存先フォルダー…
選択項目を削除
一覧をクリア
終了
名前
シリーズ名…
開始巻番号…
言語
ファイル → 画像を追加 → X 座標を入力するか赤い線をドラッグ → 保存。
保存先：{path}
保存先フォルダーが未選択です
左側：
右側：
保存形式：
元画像と同じ
番号
名前
元画像
X
右側、px
削除
行をドラッグして並べ替えます。\nX は元画像の左端からの距離です。\n線より左が左側、右が右側です。
分割 X：
比率をすべてに適用
選択項目を保存
すべて再作成
分割設定は自動保存されます。
画像を選択
画像
すべてのファイル
元画像のフォルダー
保存先フォルダーを選択
シリーズ名
シリーズ名（空欄の場合は元のファイル名）：
巻番号
開始巻番号：
画像 {count} 件。行をドラッグして並べ替えられます。
順序を保存しました。巻番号が更新され、分割位置は維持されます。
一覧をクリアしました。ディスク上のファイルは変更されません。
元画像を開けません
ファイルメニューから画像を追加してください
ファイルがありません
元画像 {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
幅の {percent:.4f}% をすべての画像に適用しました。X 値は一覧に表示されます。
保存
一覧から画像を1つ以上選択してください。
分割位置
X には 1 以上、画像幅未満の整数を入力してください。
部分名
保存先フォルダー
ドライブを利用できません：{path}
名前
保存名が重複しています。シリーズ名を指定して番号を分けてください。
{done} 件を処理し、{files} ファイルを保存しました。保存先：{path}
スキップしたファイル
完了
{files} ファイルを保存しました：\n{path}
{series} 第{number}巻
表紙
背表紙
画像の幅は2ピクセル以上必要です。
分割比率は0より大きく1未満にしてください。
ファイル名は空にできません。
左右の部分名は異なる必要があります。
不明な保存形式：{format}
元の形式 {format} では保存できません。別の形式を選択してください。
元画像は複数ページ/フレームです。元の形式、TIFF、PNG、WebP、GIFを使用してください。
ページごとに幅が異なります。別々のファイルに分けてください。''',
'ko': r'''Vertical Image Splitter
파일
이미지 추가…
폴더 추가…
저장 폴더…
선택 항목 제거
목록 비우기
종료
이름
시리즈 이름…
첫 번째 권 번호…
언어
파일 → 이미지 추가 → 픽셀 X를 지정하거나 빨간 선을 드래그 → 저장.
저장 폴더: {path}
저장 폴더를 선택하지 않았습니다
왼쪽 부분:
오른쪽 부분:
저장 형식:
원본과 동일
번호
이름
원본
X
오른쪽, px
제거
행을 드래그하여 순서를 바꿉니다.\nX는 원본 이미지 왼쪽 끝을 기준으로 합니다.\n선 왼쪽과 오른쪽으로 분할됩니다.
분할 X:
모든 이미지에 비율 적용
선택 항목 저장
모두 다시 생성
분할 설정은 자동으로 저장됩니다.
이미지 선택
이미지
모든 파일
원본 이미지 폴더
저장 폴더 선택
시리즈 이름
시리즈 이름(비우면 원본 파일 이름 사용):
번호 지정
첫 번째 권 번호:
이미지 {count}개. 행을 드래그해 순서를 바꿀 수 있습니다.
순서 저장됨. 권 번호가 갱신되었고 분할 위치는 유지됩니다.
목록이 비워졌습니다. 디스크의 파일은 변경되지 않았습니다.
원본 이미지를 사용할 수 없습니다
파일 메뉴에서 이미지를 추가하세요
파일 없음
원본 {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
너비의 {percent:.4f}%를 모든 이미지에 적용했습니다. X 값은 표에 표시됩니다.
저장
목록에서 이미지를 하나 이상 선택하세요.
분할 위치
1 이상 이미지 너비 미만의 정수 X를 입력하세요.
부분 이름
저장 폴더
드라이브를 사용할 수 없습니다: {path}
이름
저장 이름이 중복됩니다. 시리즈 이름을 지정해 번호를 구분하세요.
이미지 {done}개 처리, 파일 {files}개 저장. 폴더: {path}
건너뛴 파일
완료
파일 {files}개를 저장했습니다:\n{path}
{series}. {number}권
표지
책등
이미지 너비는 최소 2픽셀이어야 합니다.
분할 비율은 0과 1 사이여야 합니다.
파일 이름은 비워둘 수 없습니다.
왼쪽과 오른쪽 부분 이름은 달라야 합니다.
알 수 없는 출력 형식: {format}
원본 형식 {format}은 저장할 수 없습니다. 다른 형식을 선택하세요.
원본에 페이지/프레임이 여러 개 있습니다. 원본 형식, TIFF, PNG, WebP 또는 GIF를 사용하세요.
페이지 너비가 서로 다릅니다. 별도 파일로 나누세요.''',
'tr': r'''Vertical Image Splitter
Dosya
Resim ekle…
Klasör ekle…
Çıktı klasörü…
Seçilenleri kaldır
Listeyi temizle
Çıkış
Adlar
Seri adı…
İlk cilt numarası…
Dil
Dosya → Resim ekle → X konumunu piksel olarak ayarla veya kırmızı çizgiyi sürükle → kaydet.
Çıktı klasörü: {path}
Çıktı klasörü seçilmedi
Sol parça:
Sağ parça:
Kayıt biçimi:
Kaynakla aynı
No.
Ad
Kaynak
X
Sağ, piksel
Kaldır
Sıralamak için satırları sürükleyin.\nX, kaynak resmin sol kenarından ölçülür.\nSol parça çizgiden önce, sağ parça sonradır.
Kesim X:
Oranı tümüne uygula
Seçilenleri kaydet
Tümünü yeniden oluştur
Kesim ayarları otomatik kaydedilir.
Resim seç
Resimler
Tüm dosyalar
Kaynak resimlerin klasörü
Çıktı klasörü seç
Seri adı
Seri adı (boş bırakılırsa kaynak dosya adları kullanılır):
Numaralandırma
İlk cilt numarası:
{count} resim. Sıralamak için satırları sürükleyin.
Sıra kaydedildi. Cilt numaraları güncellendi; kesimler korundu.
Liste temizlendi. Diskteki dosyalar değiştirilmedi.
Kaynak resim kullanılamıyor
Dosya menüsünden resim ekleyin
Dosya yok
Kaynak {w}×{h}  |  X = {x} piksel  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
Genişliğin %{percent:.4f} kadarı tüm resimlere uygulandı. X değerleri tabloda.
Kaydet
Listeden bir veya daha fazla resim seçin.
Kesim konumu
1 ile resim genişliğinin bir eksiği arasında tam sayı X girin.
Parça adları
Çıktı klasörü
Sürücü kullanılamıyor: {path}
Adlar
Yinelenen çıktı adları var. Benzersiz numaralar için seri adı girin.
{done} resim işlendi, {files} dosya kaydedildi. Klasör: {path}
Atlanan dosyalar
Tamamlandı
{files} dosya kaydedildi:\n{path}
{series}. Cilt {number}
Kapak
Sırt
Resim genişliği en az 2 piksel olmalıdır.
Kesim oranı 0 ile 1 arasında olmalıdır.
Dosya adı boş olamaz.
Sol ve sağ parça adları farklı olmalıdır.
Bilinmeyen çıktı biçimi: {format}
Kaynak biçim {format} kaydedilemiyor. Başka biçim seçin.
Kaynakta birden çok sayfa/kare var. Kaynak biçimi, TIFF, PNG, WebP veya GIF kullanın.
Sayfaların genişlikleri farklı. Ayrı kaynak dosyalara ayırın.''',
'pl': r'''Vertical Image Splitter
Plik
Dodaj obrazy…
Dodaj folder…
Folder wyjściowy…
Usuń zaznaczone
Wyczyść listę
Zakończ
Nazwy
Nazwa serii…
Numer pierwszego tomu…
Język
Plik → Dodaj obrazy → ustaw X w pikselach lub przeciągnij czerwoną linię → zapisz.
Folder wyjściowy: {path}
Nie wybrano folderu wyjściowego
Lewa część:
Prawa część:
Format zapisu:
Jak w oryginale
Nr
Nazwa
Źródło
X
Prawa, px
Usuń
Przeciągaj wiersze, aby zmieniać kolejność.\nX mierzy się od lewej krawędzi obrazu.\nLewa część jest przed linią, prawa za nią.
Podział X:
Zastosuj proporcję do wszystkich
Zapisz zaznaczone
Utwórz wszystkie ponownie
Ustawienia podziału są zapisywane automatycznie.
Wybierz obrazy
Obrazy
Wszystkie pliki
Folder z obrazami źródłowymi
Wybierz folder wyjściowy
Nazwa serii
Nazwa serii (puste: oryginalne nazwy plików):
Numeracja
Numer pierwszego tomu:
Obrazy: {count}. Przeciągnij wiersze, aby zmienić kolejność.
Kolejność zapisana. Numeracja zaktualizowana; podziały zachowane.
Lista wyczyszczona. Nie zmieniono plików na dysku.
Obraz źródłowy niedostępny
Dodaj obrazy z menu Plik
Brak plików
Źródło {w}×{h}  |  X = {x} px  |  {left} {left_w}×{h}  |  {right} {right_w}×{h}
Zastosowano {percent:.4f}% szerokości do wszystkich obrazów. Wartości X są w tabeli.
Zapisz
Wybierz co najmniej jeden obraz z listy.
Pozycja podziału
Wprowadź całkowite X od 1 do szerokości obrazu minus 1.
Nazwy części
Folder wyjściowy
Dysk niedostępny: {path}
Nazwy
Zduplikowane nazwy plików. Ustaw nazwę serii, aby numery były unikalne.
Przetworzono {done} obrazów, zapisano {files} plików. Folder: {path}
Pominięte pliki
Gotowe
Zapisano {files} plików w\n{path}
{series}. Tom {number}
Okładka
Grzbiet
Obraz musi mieć co najmniej 2 piksele szerokości.
Proporcja podziału musi być między 0 a 1.
Nazwa pliku nie może być pusta.
Nazwy lewej i prawej części muszą się różnić.
Nieznany format wyjściowy: {format}
Nie można zapisać formatu źródłowego {format}. Wybierz inny format.
Źródło ma wiele stron/klatek. Użyj formatu źródłowego, TIFF, PNG, WebP lub GIF.
Strony mają różne szerokości. Rozdziel je na osobne pliki.''',
}

TRANSLATIONS = {'en': EN}
for code, content in RAW.items():
    lines = [line.replace(r'\n', '\n') for line in content.strip().splitlines()]
    if len(lines) != len(KEYS):
        raise RuntimeError(f'{code}: {len(lines)} translations, expected {len(KEYS)}')
    TRANSLATIONS[code] = dict(zip(KEYS, lines))


def tr(language: str, key: str, **values) -> str:
    text = TRANSLATIONS.get(language, EN).get(key, EN[key])
    return text.format(**values) if values else text


class LocalizedError(ValueError):
    def __init__(self, key: str, **values):
        self.key = key
        self.values = values
        super().__init__(tr('en', key, **values))

    def translated(self, language: str) -> str:
        return tr(language, self.key, **self.values)


def error_text(error: Exception, language: str) -> str:
    return error.translated(language) if isinstance(error, LocalizedError) else str(error)


def default_part_names(language: str) -> list[str]:
    return [tr(language, 'default_left'), tr(language, 'default_right')]
