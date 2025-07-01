```markdown
# 🧠 MediMeet – LLM-Powered Doctor Appointment & Reporting Assistant

MediMeet is a full-stack AI-powered assistant that enables patients to book appointments via natural language prompts and helps doctors receive smart summaries of their schedules. It integrates FastAPI, PostgreSQL, Gemini API, Google Calendar, and Gmail.

---

## ✨ Features

👤 Patients:

- Book appointments using natural language like:
  > “Book me with Dr. Ahuja tomorrow at 10 AM”
- View doctor availability
- Get email confirmations
- (Bonus) Track prompt history

👨‍⚕️ Doctors:

- View daily summaries: “How many patients today?”
- Trigger reports via dashboard or prompts
- (Bonus) Receive notifications via Slack/FCM

---

## 📐 Architecture

```

React (Vite) Frontend
↓
FastAPI Backend (MCP Tool System)
↓
PostgreSQL + SQLAlchemy
↓
Google Calendar & Gmail APIs + Gemini 1.5

```

---

## 🛠️ Tech Stack

| Layer        | Technology                                |
|--------------|--------------------------------------------|
| Frontend     | React (Vite), Tailwind CSS, Axios          |
| Backend      | FastAPI, Python 3.11+, SQLAlchemy, Pydantic|
| Database     | PostgreSQL                                 |
| AI/LLM       | Gemini 1.5 API                             |
| External APIs| Google Calendar API, Gmail API, Slack/FCM  |

---

## 🗂️ Project Structure

```

backend/
│
├── app/
│   ├── db/               # DB session & config
│   ├── models/           # ORM models: Doctor, Patient, etc.
│   ├── schemas/          # Pydantic request/response models
│   ├── routers/          # API route handlers
│   ├── llm/              # Gemini prompt logic
│   ├── tools/            # MCP tool logic
│   ├── utils/            # Helper functions (email, calendar)
│   └── core/             # MCP tool registry
│
├── database.py           # DB connection
├── init\_db.py            # DB table creation
├── seed\_data.py          # Dummy doctor/patient/appointment seeder
├── requirements.txt
└── .env                  # Secrets & DB config

````

---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/medi-meet.git
cd medi-meet/backend
````

### 2️⃣ Create & Activate Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Create PostgreSQL Database

Make sure PostgreSQL is installed and running.

Then create a database named:

```
medimeet_db
```

### 5️⃣ Create .env File

Create a .env file inside backend/ with:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=medimeet_db
DB_USER=postgres
DB_PASSWORD=postgres1234
```

(Replace with your actual credentials)

---

## 🧱 Initialize Database & Seed Data

Run the following commands from project root:

```bash
# Create tables
python backend/init_db.py

# Seed sample doctors and patients
python backend/seed_data.py
```

💡 Note: You will see generated UUIDs for each seeded doctor and patient.

---

## 🟢 Run the Server

```bash
uvicorn app.main:app --reload
```

Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📬 Sample Prompts (for LLM)

🧍 Patient:

* “Book me with Dr. Ahuja tomorrow morning.”
* “Find a slot with Dr. Sharma on Friday.”
* “Schedule appointment for next Monday afternoon.”

👨‍⚕️ Doctor:

* “How many appointments do I have today?”
* “Summarize this week’s patient visits.”
* “Show me patients with flu symptoms.”

---

## 📑 API Usage Summary

| Endpoint                             | Method | Description                                  |
| ------------------------------------ | ------ | -------------------------------------------- |
| /appointments/book                   | POST   | Book appointment (requires doctor\_id, etc.) |
| /appointments/available/{doctor\_id} | GET    | Get available slots for doctor               |
| /reports/summary                     | POST   | Get daily/weekly summary for a doctor        |

🧪 Example: POST /reports/summary

Request Body:

```json
{
  "doctor_id": "28efbd9a-236f-4f4a-a644-5afe20c91b10",
  "date": "2025-07-01"
}
```

Response:

```json
{
  "doctor_id": "28efbd9a-236f-4f4a-a644-5afe20c91b10",
  "date": "2025-07-01",
  "total_appointments": 3,
  "fever_cases": 1
}
```

---

## 🧠 Tooling & MCP Layer (Model-Context Protocol)

| Tool Name           | Function                                  |
| ------------------- | ----------------------------------------- |
| check\_availability | Verifies doctor availability from DB      |
| book\_appointment   | Books new appointment & saves to Calendar |
| send\_email         | Sends appointment confirmation via Gmail  |
| get\_summary        | Generates summary for doctor from DB      |
| notify\_doctor      | Sends notification (Slack/FCM)            |

---

## 📷 Screenshots (Add Manually)

* Swagger docs with sample inputs
* Appointment success response
* Summary report output

---

## 🌐 Frontend (Next Step)

This README focuses on backend setup.

Frontend is built with:

* React (Vite)
* Tailwind CSS
* Axios
* Context API for session

(Setup instructions coming soon)

---

## 📜 License

MIT License. Free to use and modify.

---

## ✍️ Author

Developed by Kartikey Narain Prajapati
📫 [kartikeyp011@gmail.com](mailto:kartikeyp011@gmail.com) | 🌍 New Delhi, India
GitHub: [https://github.com/kartikeyp011](https://github.com/kartikeyp011)

---