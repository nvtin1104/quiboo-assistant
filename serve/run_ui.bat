@echo off
echo ===============================
echo 🚀 Starting Personal AI Assistant (UI)
echo ===============================

REM Kích hoạt venv
call venv\Scripts\activate

REM Chạy Gradio UI
python -m app.ui

pause
