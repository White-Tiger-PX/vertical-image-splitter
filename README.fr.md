# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

Application de bureau permettant de découper **toute image en deux parties verticales**. La couverture et le dos d’un livre ne sont qu’un exemple : vous pouvez nommer librement les deux fichiers.

![Capture d’écran de Vertical Image Splitter](interface-illustration.png)

## Fonctionnalités

- Découpe au pixel près : saisir X ou déplacer la ligne rouge dans l’aperçu.
- Traitement par lots de fichiers ou de dossiers : **Ctrl+clic** pour sélectionner plusieurs lignes et **Enregistrer la sélection**.
- Réorganiser les lignes, appliquer la même proportion à toutes les images, puis ajuster chaque image.
- Conserver le format original ou choisir PNG, TIFF, JPEG, WebP, BMP ou GIF.
- Nom de série et numérotation des tomes facultatifs.
- Aucune modification des originaux ; sauvegarde des résultats remplacés.

## Installation et lancement

**Windows :** installez Python 3.10+ avec Tkinter, puis lancez `start.bat`. Pillow est installé automatiquement si nécessaire.

**Linux/macOS :** installez Python 3.10+ et Tkinter (souvent `python3-tk` sous Linux), puis :

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## Utilisation

1. Choisissez **Fichier → Ajouter des images…** ou **Ajouter un dossier…**.
2. Sélectionnez **Fichier → Dossier de sortie…**.
3. Nommez les parties gauche et droite (par défaut : **Couverture**, **Dos**).
4. Choisissez le format : **Identique à la source** par défaut.
5. Définissez éventuellement le nom de la série et le premier tome dans **Noms**.
6. Saisissez X en pixels source ou déplacez la ligne rouge ; ajustez de ±1 px.
7. Sélectionnez plusieurs lignes avec Ctrl (Maj pour une plage), puis **Enregistrer la sélection** ou **Tout recréer**.

## Fichiers générés

Pour `example.png`, sans série, exemple avec les noms anglais :

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

Une série crée un sous-dossier par tome, par exemple `My Series. Vol. 1/` en anglais. Les deux noms sont modifiables.

## Traitement des images

Seul l’aperçu est redimensionné ; les résultats sont découpés aux pixels exacts de la source. JPEG : qualité 100 ; WebP et TIFF : compression sans perte. Les TIFF multipages et les animations sont traités entièrement si le format de sortie le permet. La conversion peut modifier palette, couleurs et métadonnées.

## Langues et paramètres

Au premier lancement, l’interface est **en anglais**, quelle que soit la langue du système. Le menu **Langue** change immédiatement la langue et enregistre le choix dans `settings.json`. Les noms personnalisés sont conservés. Pas de détection automatique ni de traduction en ligne.

## Confidentialité et sauvegardes

Tout fonctionne en local, sans téléverser vos images. Les originaux restent intacts. Avant de remplacer un résultat, l’ancien fichier est copié dans un sous-dossier daté `Previous images/`. Les chemins de `settings.json` sont exclus de Git grâce à `.gitignore`.
