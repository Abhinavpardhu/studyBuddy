# StudyBuddy AI — Multi-Lingual Regional Personal Tutor for School Children 🎓

**StudyBuddy AI** is an interactive, regional-language personal tutoring platform designed specifically for school children (Classes 1–10, ages 8–16). It guides students step-by-step through their school subjects in **Telugu**, **Hindi**, and **English** using Socratic guidance, textbook RAG notes, voice interaction, practice exam generation, and progress tracking.

---

## 🌟 Key Features

- **🎙️ Voice Tutor Session**: Ask doubts aloud in Telugu, Hindi, or English and listen to clear spoken explanations via Text-To-Speech (TTS).
- **📚 Textbook & Notes RAG**: Upload school textbook PDFs or revision notes to ask direct questions grounded strictly in your school syllabus.
- **📝 AI Practice Exam Generator**: Automatically generate custom mock tests (MCQ / Subjective) with auto-grading, rubric scoring, and detailed solution feedback.
- **🏆 Progress & Analytics**: Track subject performance, questions asked, exam scores, and automated study recommendations.
- **🎓 Child-Friendly Visual Experience**: Vibrant glassmorphism UI designed with colorful badges, school avatars, accessible typography, and intuitive navigation.

---

## 🛠️ Tech Stack & Architecture

- **Backend**: Python 3.12+, FastAPI, Uvicorn, SQLAlchemy (SQLite), Pydantic v2, Python-Jose (JWT), Bcrypt.
- **AI Integrations**: Google Gemini API pool (`google-genai` / `langchain-google-genai`), PyMuPDF / PyPDF for PDF RAG context extraction.
- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, FontAwesome 6, Web Speech API (TTS & Speech Recognition).

---

## 🚀 Quick Start Guide

### 1. Installation
Clone the repository and install backend dependencies:
```bash
cd "study buddy/backend"
pip install -r requirements.txt
```

### 2. Launching the Platform

#### Windows (Command Prompt / Batch):
Double-click `run.bat` or run in terminal:
```cmd
run.bat
```

#### Windows (PowerShell):
```powershell
.\run.ps1
```

#### Linux / macOS:
```bash
chmod +x run.sh
./run.sh
```

The script will automatically:
1. Start the FastAPI backend server on `http://127.0.0.1:8000`.
2. Open `frontend/index.html` in your default web browser.

---

## ⚙️ Environment Configuration

Copy `backend/.env.example` to `backend/.env`:
```env
PROJECT_NAME="AI Regional-Language Personal Tutor (StudyBuddy AI)"
DATABASE_URL="sqlite:///./app.db"
JWT_SECRET_KEY="your_secure_random_jwt_secret_key"
GEMINI_API_KEY_1="your_gemini_api_key_1"
```

---

## 🔒 Authentication & API Endpoints

- `POST /api/auth/register` — Register a new student profile (Name, Email, Password, Class/Grade, Preferred Language).
- `POST /api/auth/login` — Login with student credentials & receive JWT token.
- `GET /api/auth/me` — Fetch current authenticated student profile.
- `PUT /api/auth/profile` — Update student profile settings.
- `POST /api/auth/logout` — Client-side session clearing.
- `GET /api/documents` / `POST /api/documents/upload` — Manage PDF RAG textbooks & study materials.
- `POST /api/chat` — Send doubt prompt to Socratic AI Tutor.
- `POST /api/exams/generate` — Generate custom practice exams.
- `GET /api/progress` — Retrieve student learning analytics.

---

## 📜 License
Built for Hackathon Excellence & Educational Progress.