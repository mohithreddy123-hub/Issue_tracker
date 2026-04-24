# Simple Issue Tracker Backend

A lightweight backend service made with FastAPI and SQLAlchemy that helps keep track of and fix problems.

## 🚀 Features
- **Create Issue**: Add a new issue with a title, description, and status.
- **List Issues**: Get a list of all the issues that have been recorded.
- **Update Status**: Change the status of an issue that is already open, in progress, or closed.
- **Persistent Storage**: Uses SQLite to keep data safe.

---

## 🛠️ Setup Instructions

### 1. Clone or Extract the Project
Ensure you are in the project root directory.

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ How to Run
Start the application using Uvicorn:
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## 📖 API Documentation

### Interactive Docs
Once the server is running, you can access the interactive Swagger documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/issues` | Create a new issue |
| `GET` | `/issues` | Get all issues |
| `PUT` | `/issues/{issue_id}/status` | Update issue status |

---

## 💡 Example API Requests

### 1. Create an Issue
**Request:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/issues' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Fix Login Bug",
  "description": "Users are unable to login using Google OAuth.",
  "status": "Open"
}'
```

### 2. Get All Issues
**Request:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/issues'
```

### 3. Update Issue Status
**Request:**
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/issues/1/status?status=In Progress'
```

---

## 📦 Data Schema

### Issue Object
- `id`: Unique Integer (Auto-generated)
- `title`: String
- `description`: String
- `status`: Enum (Open, In Progress, Closed)
