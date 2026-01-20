# PowerShell script to activate virtual environment and run Django server
# Usage: .\run_server.ps1

Write-Host "Activating virtual environment..." -ForegroundColor Green
& ".\.venv\Scripts\Activate.ps1"

Write-Host "Changing to FRONTEND directory..." -ForegroundColor Green
Set-Location -Path ".\FRONTEND"

Write-Host "Starting Django development server..." -ForegroundColor Green
Write-Host "Server will be available at: http://127.0.0.1:8000/" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python manage.py runserver
