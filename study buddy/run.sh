#!/usr/bin/env bash
# Bash Startup Script for StudyBuddy AI

echo "================================================================"
echo "   AI REGIONAL-LANGUAGE PERSONAL TUTOR (StudyBuddy AI)"
echo "================================================================"
echo ""
echo "Starting FastAPI Backend Server on http://127.0.0.1:8000..."
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/backend" || exit

# Run Uvicorn server
python3 -m uvicorn app.main:app --reload --port 8000
