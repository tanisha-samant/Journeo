@echo off
chcp 65001 >nul
echo 🚀 Starting Journeo - AI-Powered Travel Planner
echo ================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.11+ first.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 18+ first.
    pause
    exit /b 1
)

REM Check if npm is installed
npm --version >nul 2>&1
if errorlevel 1 (
    echo ❌ npm is not installed. Please install npm first.
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed

echo.
echo Choose an option:
echo 1) Start Backend only
echo 2) Start Frontend only
echo 3) Start Both servers
echo 4) Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto start_backend
if "%choice%"=="2" goto start_frontend
if "%choice%"=="3" goto start_both
if "%choice%"=="4" goto exit
echo ❌ Invalid choice. Please run the script again.
pause
exit /b 1

:start_backend
echo 🐍 Starting Backend Server...
cd backend

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if requirements.txt exists
if exist "requirements.txt" (
    echo 📦 Installing Python dependencies...
    pip install -r requirements.txt
)

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️  Warning: .env file not found. Please create one from env.example
    echo    Copy env.example to .env and add your API keys
)

echo 🚀 Starting FastAPI server on http://localhost:8000
echo 📚 API Documentation: http://localhost:8000/docs
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
goto end

:start_frontend
echo ⚛️  Starting Frontend Server...
cd frontend

REM Install dependencies if package.json exists
if exist "package.json" (
    echo 📦 Installing Node.js dependencies...
    npm install
)

echo 🚀 Starting Next.js server on http://localhost:3000
npm run dev
goto end

:start_both
echo 🔄 Starting both servers...
echo.
echo This will open two command windows - one for backend and one for frontend.
echo Close both windows to stop the servers.
echo.
pause

REM Start backend in new window
start "Journeo Backend" cmd /k "cd backend && if not exist venv python -m venv venv && call venv\Scripts\activate.bat && if exist requirements.txt pip install -r requirements.txt && echo 🚀 Starting FastAPI server on http://localhost:8000 && echo 📚 API Documentation: http://localhost:8000/docs && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend in new window
start "Journeo Frontend" cmd /k "cd frontend && if exist package.json npm install && echo 🚀 Starting Next.js server on http://localhost:3000 && npm run dev"

echo ✅ Both servers started!
echo 🌐 Frontend: http://localhost:3000
echo 🔧 Backend: http://localhost:8000
echo 📚 API Docs: http://localhost:8000/docs
echo.
echo Close the command windows to stop the servers.
pause
goto end

:exit
echo 👋 Goodbye!
pause
exit /b 0

:end
pause 