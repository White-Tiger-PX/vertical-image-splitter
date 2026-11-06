@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if not errorlevel 1 (
  set "BCS_PY=py"
  goto ready
)
where python >nul 2>&1
if not errorlevel 1 (
  set "BCS_PY=python"
  goto ready
)
echo Python 3.10+ not found. Install Python from python.org.
pause
exit /b 1
:ready
"%BCS_PY%" -c "import sys; assert sys.version_info >= (3,10); import tkinter" >nul 2>&1
if errorlevel 1 (
  echo Python 3.10+ with Tkinter is required.
  pause
  exit /b 1
)
"%BCS_PY%" -c "from PIL import Image, ImageTk" >nul 2>&1
if not errorlevel 1 goto run
"%BCS_PY%" -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 (
  echo Could not install Pillow.
  pause
  exit /b 1
)
:run
"%BCS_PY%" "%~dp0cover_splitter.py"
if errorlevel 1 pause
