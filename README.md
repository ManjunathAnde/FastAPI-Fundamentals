# FastAPI Backend Engineering
A hands-on progression from FastAPI fundamentals to production-oriented backend architecture covering REST APIs, validation, persistence, ORM design, dependency injection, and full-stack integration.

This repository documents my practical journey into modern backend engineering with FastAPI. Rather than treating FastAPI as a collection of tutorials, I'm using the project to progressively build and refactor backend systems using patterns that scale beyond a single script or demo application.

The focus is on understanding why backend systems are structured the way they are, while continuously improving implementation quality as the project evolves.

---

## ⚡ What This Repository Demonstrates

**API Design**
- RESTful CRUD endpoints using GET, POST, PUT, and DELETE
- Path and query parameter handling
- Structured request and response models

**Validation & Data Modeling**
- Pydantic schemas with explicit type validation
- Separation between API schemas and database models
- Automatic serialization and response validation

**Persistence & ORM**
- SQLAlchemy-based database integration
- Engine, session, and model configuration
- Transition from in-memory state to persistent storage
- Programmatic database initialization and seeding

**Backend Architecture**
- FastAPI dependency injection with Depends
- Safe session lifecycle management using try/yield/finally
- Separation of API, validation, and persistence concerns
- Reusable database-session patterns

**Full-Stack Integration**
- React frontend consuming the FastAPI backend
- CORS middleware configuration for browser-based requests
- End-to-end CRUD operations from UI to database

---

## 📦 Project Phases

### Phase 01 - API Fundamentals
**Status: Completed**

Built the foundation of a REST API and developed an understanding of how HTTP requests move through a FastAPI application.

- Implemented complete CRUD workflows
- Designed routes using path and query parameters
- Created structured request models with Pydantic
- Added validation at the API boundary
- Worked with FastAPI's automatic API documentation

### Phase 02 - Persistence & ORM
**Status: Completed**

Moved beyond transient in-memory data toward a persistent MySQL backend.

- Integrated SQLAlchemy as the ORM layer
- Configured database engines and sessions
- Defined database models and table structures
- Introduced programmatic database initialization
- Refactored all CRUD operations around persistent data

### Phase 03 - Backend Architecture
**Status: Completed**

Focused on writing backend code that remains understandable and maintainable as complexity increases.

- FastAPI dependency injection with Depends
- Reusable database-session management using try/yield/finally
- Cleaner separation of API and persistence concerns
- Transaction-aware CRUD operations with explicit commits
- Full-stack integration with a React frontend

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| FastAPI | REST API framework and application layer |
| Python | Backend implementation |
| Pydantic | Request validation and data schemas |
| SQLAlchemy | ORM and database interaction |
| MySQL | Persistent relational database |
| Uvicorn | ASGI application server |
| React | Frontend UI consuming the API |
| Axios | HTTP client for frontend-backend communication |
| Git / GitHub | Version control and project progression |

---

## 🔍 Engineering Principles

**Learn → Implement → Refactor**

Each stage is an opportunity to understand the underlying mechanism, implement it, identify architectural limitations, and improve the design in the next iteration.

**Explicit Data Contracts**

Pydantic models are used to make request and response structures explicit rather than relying on loosely structured dictionaries or implicit assumptions.

**Separation of Concerns**

API routing, validation, database access, and application logic are progressively separated as the project grows. The goal is to make individual components easier to understand, test, replace, and extend.

**Build for Understanding**

The repository intentionally shows the progression from simpler implementations to more structured ones. Intermediate implementations are part of the learning process rather than being hidden behind a polished final state.

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/ManjunathAnde/FASTAPI-Project
cd fastapi-project
```

### 2. Create and activate a virtual environment
```bash
# Windows PowerShell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database

Update the connection string in `database.py` to point to your local MySQL instance:
```python
db_url = "mysql+pymysql://your_user:your_password@127.0.0.1:3306/fastapi_db"
```

Create the schema in MySQL first:
```sql
CREATE DATABASE fastapi_db;
```

### 5. Start the backend
```bash
uvicorn main:app --reload
```

### 6. Start the frontend
```bash
cd frontend
npm install
npm start
```

---

## 📖 Explore the API

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 👋 Why This Repository Exists

I'm using this repository to turn backend concepts into working systems, document what I learn, and progressively raise the engineering standard of the code.

Built with Python, FastAPI, and a bias toward learning by building.
