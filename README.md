# Simple Auth App

A minimal, production-ready full-stack authentication system. This project demonstrates secure user registration, login, and session management using a FastAPI backend and a React frontend, strictly enforcing **HttpOnly cookies** to prevent XSS attacks.

## ✨ Features

- **Secure Authentication:** JWT-based sessions stored exclusively in `HttpOnly`, `SameSite=Lax` cookies.
- **Modern Backend:** Built with FastAPI (Python), utilizing Pydantic for strict payload validation and SQLAlchemy for database ORM.
- **Robust Cryptography:** Passwords are mathematically hashed and salted using `bcrypt`.
- **Containerized Infrastructure:** Instant local setup using Docker and PostgreSQL.
- **Isolated Testing:** Comprehensive `pytest` suite running on a high-speed, in-memory SQLite database to protect local development data.
- **React Frontend:** Feature-Sliced Design (FSD) architecture using Axios interceptors and a global React Context for seamless state management.

---

## 📂 Project Structure

This project uses a hybrid Feature-Sliced Design (FSD) to cleanly separate technical infrastructure from business logic.

```text
simple-auth-app/
├── docker-compose.yml
├── .env.example
│
├── backend/src/               # FastAPI Python Backend
│   ├── main.py
│   ├── core/                  # Shared technical infrastructure
│   │   ├── database.py
│   │   └── security.py
│   └── features/              # Business logic domains
│       └── auth/
│           ├── router.py
│           ├── schemas.py
│           └── service.py
│
└── frontend/src/              # React Frontend
    ├── App.tsx
    ├── core/                  # Global providers & API clients
    │   ├── api.ts
    │   └── AuthContext.tsx
    └── features/              # Domain-specific UI & components
        └── auth/
            ├── AuthPage.tsx
            └── Dashboard.tsx
```

## 🚀 Getting Started

### Prerequisites

- **Python (v3.12+)**
- **UV Package manager**
- **Docker & Docker Compose**
- **Node.js** (v18+)
- **pnpm** (`npm install -g pnpm`)

### How to Run? (Docker)

1. **Clone the repository** and navigate to the root folder.
2. Spin up containers via Docker Compose.
   ```bash
   docker compose up -d --build
   ```
3. Hosts for backend and frontend:
   - API: http://localhost:8080
   - Swagger docs: http://localhost:8080/docs
   - Web App: http://localhost:3000

### How to Test?

Execute the automated suite inside the running container to verify the security and logic:
`bash
    uv run pytest
    `
