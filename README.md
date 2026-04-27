# Simple Issue Tracker Backend

A lightweight backend service made with FastAPI and SQLAlchemy for managing and tracking issues.

## 🚀 Features
- **Create Issue**: Add a new issue with a title, description, and status.
- **List Issues**: Retrieve all recorded issues, with optional status filtering.
- **Update Status**: Change the status of an existing issue.
- **Persistent Storage**: Uses SQLite for data persistence.

## 📁 Project Structure
```text
Issue_tracker/
├── main.py          # FastAPI application routes
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic data validation schemas
├── crud.py          # Database CRUD logic
├── database.py      # Database connection and session setup
├── requirements.txt # Project dependencies
├── issues.db        # SQLite database (auto-generated)
├── SAMPLE_INPUTS.txt# Example JSON bodies for testing
└── README.md        # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Create a Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Steps to Run the Application
Start the server using Uvicorn:
```bash
uvicorn main:app --reload
```
The application will be live at `http://127.0.0.1:8000`.

---

## 💡 Example CLI Commands
Use these commands to test the API from your terminal:

**Create Issue:**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/issues' -H 'Content-Type: application/json' -d '{"title": "Fix Login Page CSS", "description": "Misaligned button on mobile.", "status": "Open"}'
```

**Get All Issues:**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/issues'
# Example with filtering:
# curl -X 'GET' 'http://127.0.0.1:8000/issues?status=Open'
```

**Update Status:**
```bash
curl -X 'PUT' 'http://127.0.0.1:8000/issues/1/status?status=Closed'
```
