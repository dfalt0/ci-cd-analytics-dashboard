# Run backend + frontend together in PowerShell
# Usage: .\dev.ps1

# Start backend
Write-Output "Starting backend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "
    cd backend;
    .\venv\Scripts\Activate.ps1;
    uvicorn main:app --reload
" -PassThru -WindowStyle Hidden | ForEach-Object { $backendPID = $_.Id }

# Start frontend
Write-Output "Starting frontend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "
    cd frontend;
    npm run dev
" -PassThru -WindowStyle Hidden | ForEach-Object { $frontendPID = $_.Id }

# Trap Ctrl+C to kill processes
Register-EngineEvent PowerShell.Exiting -Action {
    Write-Output "Stopping backend ($backendPID) and frontend ($frontendPID)..."
    Stop-Process -Id $backendPID -Force
    Stop-Process -Id $frontendPID -Force
}

# Keep script alive until user closes it
Write-Output "Backend + Frontend running. Press Ctrl+C to stop."
Wait-Event
