# PowerShell Startup Script for StudyBuddy AI
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "   AI REGIONAL-LANGUAGE PERSONAL TUTOR (StudyBuddy AI)" -ForegroundColor Yellow
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting FastAPI Backend Server on http://127.0.0.1:8000..." -ForegroundColor Green
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path "$ScriptDir\backend"

# Launch default browser with frontend index.html after short delay
Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "$using:ScriptDir\frontend\index.html"
} | Out-Null

# Run Uvicorn server
python -m uvicorn app.main:app --reload --port 8000
