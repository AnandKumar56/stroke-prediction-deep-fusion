# PowerShell script for initial setup
# Usage: .\setup.ps1

Write-Host "Setting up project environment..." -ForegroundColor Green

# Check if virtual environment exists
if (-Not (Test-Path ".\.venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Green
& ".\.venv\Scripts\Activate.ps1"

Write-Host "Installing requirements..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Changing to FRONTEND directory..." -ForegroundColor Green
Set-Location -Path ".\FRONTEND"

Write-Host "Running database migrations..." -ForegroundColor Green
python manage.py migrate

Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "Run '.\run_server.ps1' to start the Django server" -ForegroundColor Yellow
