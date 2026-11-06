"""Image splitting, editable names, and format-aware saving."""
from __future__ import annotations
from datetime import datetime
from pathlib import Path
import re
import shutil
from PIL import Image, ImageOps
from i18n import LocalizedError

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tif', '.tiff', '.gif'}
OUTPUT_FORMATS = {
    'SOURCE': 'As source',
    'PNG': 'PNG', 'TIFF': 'TIFF', 'JPEG': 'JPEG',
    'WEBP': 'WebP', 'BMP': 'BMP', 'GIF': 'GIF',
}
EXTENSIONS = {'JPEG': '.jpg', 'PNG': '.png', 'TIFF': '.tiff',
              'WEBP': '.webp', 'BMP': '.bmp', 'GIF': '.gif'}

def split_pixel(width: int, fraction: float) -> int:
    if width < 2:
        raise LocalizedError('core_width')
    if not 0 < float(fraction) < 1:
        raise LocalizedError('core_fraction')
    return max(1, min(width - 1, round(width * float(fraction))))

def load_source(path: Path) -> Image.Image:
    with Image.open(path) as original:
        return ImageOps.exif_transpose(original).copy()

def safe_name(value: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', value).strip(' .')
    if not name:
        raise LocalizedError('core_empty_name')
    reserved = {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)), *(f'LPT{i}' for i in range(1, 10))}
    if name.split('.')[0].upper() in reserved:
        name = '_' + name
    return name

def natural_key(value: str) -> list:
    return [int(piece) if piece.isdigit() else piece.casefold()
            for piece in re.split(r'(\d+)', value)]

def settings_path() -> Path:
    return Path(__file__).resolve().parent / 'settings.json'

def part_names(left: str = 'Cover', right: str = 'Spine') -> tuple[str, str]:
    left = safe_name(str(left).strip() or 'Cover')
    right = safe_name(str(right).strip() or 'Spine')
    if left.casefold() == right.casefold():
        raise LocalizedError('core_same_labels')
    return left, right

def resolve_format(source: Path, original_format: str, chosen: str) -> tuple[str, str]:
    chosen = chosen.upper()
    if chosen not in OUTPUT_FORMATS:
        raise LocalizedError('core_unknown_format', format=chosen)
    target = original_format.upper() if chosen == 'SOURCE' else chosen
    if target == 'MPO':
        target = 'JPEG'
    if target not in EXTENSIONS:
        raise LocalizedError('core_unsupported_format', format=target)
    extension = EXTENSIONS[target]
    if chosen == 'SOURCE' and source.suffix.lower() in IMAGE_EXTENSIONS:
        extension = source.suffix.lower()
    return target, extension

def prepare_frame(image: Image.Image, target: str) -> Image.Image:
    if target in ('JPEG', 'BMP'):
        if image.mode in ('RGBA', 'LA') or 'transparency' in image.info:
            rgba = image.convert('RGBA')
            background = Image.new('RGBA', image.size, 'white')
            return Image.alpha_composite(background, rgba).convert('RGB')
        if image.mode not in ('RGB', 'L', 'CMYK') or (target == 'BMP' and image.mode == 'CMYK'):
            return image.convert('RGB')
    elif target in ('PNG', 'WEBP') and image.mode == 'CMYK':
        return image.convert('RGB')
    return image

def save_parts(source: Path, output: Path, title: str, fraction: float,
               stamp: str | None = None, *, left_label: str = 'Cover',
               right_label: str = 'Spine', output_format: str = 'SOURCE') -> tuple[int, int, int]:
    left_label, right_label = part_names(left_label, right_label)
    source = Path(source)
    frames = []
    durations = []
    with Image.open(source) as original:
        target, extension = resolve_format(source, original.format or '', output_format)
        metadata = {key: original.info[key] for key in ('icc_profile', 'dpi') if key in original.info}
        loop = original.info.get('loop', 0)
        count = getattr(original, 'n_frames', 1)
        if count > 1 and target not in ('TIFF', 'GIF', 'WEBP', 'PNG'):
            raise LocalizedError('core_multi_frame')
        for index in range(count):
            original.seek(index)
            frame = ImageOps.exif_transpose(original).copy()
            frames.append(frame)
            durations.append(original.info.get('duration', 100))
    width, height = frames[0].size
    x = split_pixel(width, fraction)
    if any(frame.width != width for frame in frames):
        raise LocalizedError('core_var_width')
    title = safe_name(title)
    folder = Path(output) / title
    folder.mkdir(parents=True, exist_ok=True)
    stamp = stamp or datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')
    staged = []
    try:
        for label, left, right in [(left_label, 0, x), (right_label, x, width)]:
            pieces = [prepare_frame(frame.crop((left, 0, right, frame.height)), target) for frame in frames]
            destination = folder / f'{title} - {label}{extension}'
            temporary = destination.with_name(destination.name + '.tmp')
            staged.append((temporary, destination))
            options = dict(metadata)
            if target == 'JPEG':
                options.update(quality=100, subsampling=0)
            elif target == 'WEBP':
                options.update(lossless=True, quality=100)
            elif target == 'TIFF':
                options.update(compression='tiff_deflate')
            if len(pieces) > 1:
                options.update(save_all=True, append_images=pieces[1:])
                if target in ('PNG', 'GIF', 'WEBP'):
                    options.update(duration=durations, loop=loop)
                if target == 'GIF':
                    options['disposal'] = 2
            pieces[0].save(temporary, format=target, **options)
        for _, destination in staged:
            if destination.exists():
                backup = folder / 'Previous images' / stamp / destination.name
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(destination, backup)
        for temporary, destination in staged:
            temporary.replace(destination)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)
    return width, height, x
