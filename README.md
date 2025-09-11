![CI](https://github.com/dfalt0/ci-cd-analytics-dashboard/actions/workflows/ci.yml/badge.svg)


# Backend
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend
npm install
npm run dev


------------------

# Which to use?

Makefile → best if you’re on Linux/Mac or Windows with Git Bash/WSL.

dev.sh → simpler and portable if you just want one script.

dev.ps1 → for use on Windows in PowerShell


# Makefile Usage

## 1. Install dependencies (first time only):

make backend-install
make frontend-install


## 2. Run everything (backend API + frontend UI) at once:

make dev


## 3. Just backend:

make backend-serve


## 4. Just frontend:

make frontend-dev



# Bash install (Instead of Makefile)

chmod +x dev.sh

## Run backend + frontend simultaneously
./dev.sh



# PowerShell install 

## Backend
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Frontend
cd ..\frontend
npm install



