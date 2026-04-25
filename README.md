# Simple Issue Tracker Backend

A lightweight backend service made with FastAPI and SQLAlchemy for managing and tracking issues.

## 🚀 Features
- **Create Issue**: Add a new issue with a title, description, and status.
- **List Issues**: Retrieve all recorded issues, with optional status filtering.
- **Update Status**: Change the status of an existing issue.
- **Persistent Storage**: Uses SQLite for data persistence.

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

## 📖 API Documentation

### 🔗 Base URL
`http://127.0.0.1:8000`

### 📌 Endpoints Summary
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/issues` | Create a new issue |
| `GET` | `/issues` | Retrieve all issues |
| `PUT` | `/issues/{id}/status` | Update issue status |

### 🛠️ Endpoint Details

#### 1. Create Issue (`POST /issues`)
- **Description**: Adds a new issue.
- **Request Body Example**:
  ```json
  {
    "title": "Fix Login Page CSS",
    "description": "The login button is misaligned on mobile devices.",
    "status": "Open"
  }
  ```
- **Response (201 Created)**:
  ```json
  {
    "id": 1,
    "title": "Fix Login Page CSS",
    "description": "The login button is misaligned on mobile devices.",
    "status": "Open"
  }
  ```

#### 2. Get All Issues (`GET /issues`)
- **Description**: Returns all issues in the database. You can optionally filter by status.
- **Example Request**: `/issues?status=Open`
- **Response (200 OK)**:
  ```json
  [
    {
      "id": 1,
      "title": "Fix Login Page CSS",
      "description": "The login button is misaligned on mobile devices.",
      "status": "Open"
    }
  ]
  ```

#### 3. Update Status (`PUT /issues/{id}/status`)
- **Description**: Updates the status of an issue using its ID.
- **Example Request**: `/issues/1/status?status=In Progress`
- **Response (200 OK)**:
  ```json
  {
    "id": 1,
    "title": "Fix Login Page CSS",
    "description": "The login button is misaligned on mobile devices.",
    "status": "In Progress"
  }
  ```

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
