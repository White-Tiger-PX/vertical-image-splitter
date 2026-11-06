# Vertical Image Splitter

**[English](README.md)** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt_BR.md) · [Italiano](README.it.md) · [简体中文](README.zh_CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Polski](README.pl.md)

**모든 이미지를 세로로 두 부분으로 나누는** 데스크톱 앱입니다. 책 표지와 책등은 예시일 뿐이며 두 결과의 이름은 자유롭게 지정할 수 있습니다.

![Vertical Image Splitter 스크린샷](interface-illustration.png)

## 기능

- 픽셀 단위 분할: X 좌표 입력 또는 미리보기의 빨간 선 드래그.
- 파일/폴더 일괄 처리: **Ctrl+클릭**으로 여러 행을 선택한 뒤 **선택 항목 저장**.
- 행 드래그로 순서 변경, 공통 비율 적용, 이미지별 미세 조정.
- 원본 형식 유지 또는 PNG, TIFF, JPEG, WebP, BMP, GIF로 저장.
- 시리즈 이름과 권 번호 선택 사항. 없으면 원본 파일 이름 사용.
- 원본은 변경하지 않고 기존 결과를 덮어쓰기 전에 백업.

## 설치 및 실행

**Windows:** Tkinter가 포함된 Python 3.10+ 설치 후 `start.bat` 실행. Pillow가 없으면 설치를 시도합니다.

**Linux/macOS:** Python 3.10+ 및 Tkinter 설치(Linux에서는 `python3-tk`가 필요할 수 있음) 후 실행:

```sh
python3 -m pip install -r requirements.txt
python3 cover_splitter.py
```

## 사용 방법

1. **파일 → 이미지 추가…** 또는 **폴더 추가…** 선택.
2. **파일 → 저장 폴더…** 에서 대상 폴더 선택.
3. 왼쪽/오른쪽 이름 지정(한국어 기본 예시: **표지**, **책등**).
4. 저장 형식 선택. 기본은 **원본과 동일**.
5. 필요하면 **이름** 메뉴에서 시리즈 이름과 첫 권 번호 지정.
6. 원본 이미지의 X 좌표를 입력하거나 빨간 선 이동; ±1 px로 조절.
7. Ctrl로 여러 행 선택(Shift로 범위 선택) 후 **선택 항목 저장** 또는 **모두 다시 생성**.

## 출력 파일

시리즈 없는 `example.png`의 결과 예시(영어 기본 이름):

```text
output/
  example/
    example - Cover.png
    example - Spine.png
```

시리즈를 설정하면 권마다 폴더가 생성됩니다. 영어 UI 예: `My Series. Vol. 1/`. 두 이름 모두 변경 가능합니다.

## 이미지 처리

미리보기만 축소·확대되며 결과는 원본 픽셀 기준으로 정확히 잘립니다. JPEG 품질 100, WebP와 TIFF는 무손실 압축입니다. 지원 형식에서는 여러 페이지 TIFF와 애니메이션을 처리합니다. 변환 시 색상 모드, 팔레트, 메타데이터가 달라질 수 있습니다.

## 언어 및 설정

첫 실행 시 OS와 관계없이 **영어**로 시작합니다. **언어** 메뉴에서 즉시 변경하고, 선택한 언어와 이미지 목록·분할 위치 등은 `settings.json`에 저장됩니다. 직접 입력한 이름은 유지됩니다. 자동 언어 감지나 온라인 번역은 없습니다.

## 개인정보 및 백업

이미지는 로컬에서만 처리하며 업로드하거나 원본을 변경하지 않습니다. 기존 결과를 교체하기 전에 날짜별 `Previous images/` 폴더에 백업합니다. 로컬 경로가 포함된 `settings.json`은 `.gitignore`로 제외됩니다.
