# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

轻量级桌面工具，可将**任意图片沿竖线分为两部分**。书籍封面与书脊只是示例，两部分的名称可自由设置。

![Vertical Image Splitter 软件界面截图](interface-illustration.png)

## 功能

- 精确到像素：输入 X 坐标，或在预览中拖动红色分割线。
- 批量添加文件或文件夹；按住 **Ctrl** 多选行，再单击“保存所选”。
- 拖动行调整顺序，将相同比例应用到全部图片，并逐张微调。
- 保留源文件格式，或输出 PNG、TIFF、JPEG、WebP、BMP、GIF。
- 可选系列名称和卷号；不设置时使用源文件名。
- 不修改源文件；覆盖旧结果前自动备份。

## 安装与运行

**Windows：** 安装带 Tkinter 的 Python 3.10+，双击 `start.bat`。缺少 Pillow 时，启动脚本会尝试安装。

**Linux/macOS：** 安装 Python 3.10+ 和 Tkinter（Linux 可能需要 `python3-tk`），执行：

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## 操作说明

1. 选择 **文件 → 添加图片…** 或 **添加文件夹…**。
2. 在 **文件 → 输出文件夹…** 中选择保存位置。
3. 设置左右两部分名称（中文默认示例：**封面**、**书脊**）。
4. 选择格式：默认 **与原图相同**。
5. 可在 **命名** 菜单中设置系列名称及首卷编号。
6. 输入源图像素 X 坐标或拖动红线；可用 ±1 px 精调。
7. 按 Ctrl 多选行（Shift 连续选择），点击 **保存所选** 或 **重新生成全部**。

## 输出文件

不设置系列时，`example.png` 的输出示例（使用英文默认名称）：

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

设置系列后，每卷有独立文件夹，例如英文界面中的 `My Series. Vol. 1/`。两部分名称均可修改。

## 图像处理

只有预览图会缩放，输出按原图像素精确裁剪。JPEG 质量为 100，WebP 和 TIFF 使用无损压缩。选择兼容格式时，可处理多页 TIFF 和动画帧。格式转换可能改变调色板、颜色模式或元数据。

## 语言与设置

首次启动**默认英语**，不读取操作系统语言。通过 **语言** 菜单即时切换，并将选择与文件列表、分割位置等保存在 `settings.json`。手动输入的名称不会因切换语言而丢失。无需在线翻译。

## 隐私与备份

所有处理均在本地完成，不上传图片，也不修改源文件。覆盖结果前，旧文件会备份到带日期的 `Previous images/` 子文件夹。包含本地路径的 `settings.json` 已列入 `.gitignore`。
