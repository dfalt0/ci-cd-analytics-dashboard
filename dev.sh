#!/bin/bash
# Run backend + frontend together

# Start backend
cd backend
source venv/bin/activate
uvicorn main:app --reload &
BACKEND_PID=$!
cd ..

# Start frontend
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Trap exit signals and kill background processes
trap "kill $BACKEND_PID $FRONTEND_PID" EXIT

# Wait for both processes to finish
wait
