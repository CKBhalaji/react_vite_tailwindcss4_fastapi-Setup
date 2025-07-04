# react vite tailwind and fastapi starter kit

This project is a comprehensive starter kit for building full-stack web applications, featuring:

-   **Frontend:** React (latest) with Vite (latest) and Tailwind CSS 4 (latest)
-   **Backend:** FastAPI (latest) with Python
-   **Database:** SQLAlchemy/SQLModel boilerplate with examples for SQLite and PostgreSQL.

## Features

-   **⚡️ Blazing Fast Frontend:** Developed with Vite for incredibly fast cold starts and HMR.
-   **🎨 Modern Styling:** Configured with Tailwind CSS 4 for utility-first styling.
-   **🚀 Robust Backend:** Built with FastAPI for high-performance APIs.
-   **📊 Database Ready:** Includes boilerplate for SQLite (local) and PostgreSQL (production-ready).
-   **🤝 Seamless Communication:** Frontend proxying to backend API during development.
-   **📦 NPM Package Structure:** Designed as a template for easy setup and future publishing.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Make sure you have the following installed:

-   **Node.js & npm:** [Download Node.js](https://nodejs.org/en/download/) (npm is included with Node.js)
-   **Python 3.8+:** [Download Python](https://www.python.org/downloads/)
-   **pip:** Python's package installer (comes with Python)

### Installation

1.  **Clone the repository (or extract the NPM package contents):**
    ```bash
    git clone https://github.com/CKBhalaji/react_vite_tailwindcss4_fastapi-Setup
    cd react_vite_tailwindcss4_fastapi-Setup
    ```
    (If this was an actual NPM package, you'd run `npm install reactvite-tailwind-fastapi` and then `npx reactvite-tailwind-fastapi init my-app` or similar if it were a CLI tool.)

2.  **Install all dependencies (frontend & backend):**
    This command will run all necessary installation steps for both parts of the application.
    ```bash
    npm run install-all
    ```
    *This might take a few minutes.*

### Configuration

#### Database Setup

1.  **Create `.env` file:**
    Navigate to the `backend/` directory and create a file named `.env`.
    ```bash
    cd backend
    cp .env.example .env
    ```
2.  **Edit `.env`:**
    Open the newly created `.env` file and set your `DATABASE_URL`.
    -   **For Local Development (SQLite):**
        ```
        DATABASE_URL="sqlite:///./sql_app.db"
        SECRET_KEY="your-super-secret-jwt-key" # Change this to a strong, random key
        ```
        This will create a `sql_app.db` file in your `backend/` directory.
    -   **For Production (PostgreSQL Example):**
        ```
        # DATABASE_URL="postgresql://user:password@host:port/dbname"
        # Example with common defaults:
        DATABASE_URL="postgresql://postgres:mysecretpassword@localhost:5432/fastapidb"
        SECRET_KEY="your-super-secret-jwt-key" # Change this to a strong, random key
        ```
        *Remember to uncomment the PostgreSQL line and replace with your actual credentials.*

### Running the Application

You can run the frontend and backend simultaneously or individually.

#### Running Both (Development Mode)

From the root directory of the project:
```bash
npm run start-dev

```

This command will start the backend (FastAPI) and then the frontend (Vite) development servers concurrently. You'll see output from both.

Frontend (Vite): Accessible at http://localhost:5173/ (or another port if 5173 is busy).

Backend (FastAPI): Accessible at http://localhost:8000/

Open http://localhost:8000/docs for FastAPI's interactive API documentation (Swagger UI).

The frontend will proxy API calls from /api/* to http://localhost:8000/*.

### Running Frontend Only (Development)
From the root directory:

```bash
npm run dev-frontend
```
### Running Backend Only (Development)
From the root directory:

```bash
npm run dev-backend
```

### Building for Production
To create a production-ready build of the frontend:
```bash
npm run build-frontend
```
This will generate optimized static assets in the frontend/dist/ directory. You can then serve these static files using a web server or integrate them into your backend.

### Project Structure
fullstack-ai-starter/
├── .gitignore
├── package.json
├── README.md
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx
│       ├── index.css
│       └── main.jsx
└── backend/
    ├── .env.example
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── requirements.txt
    └── venv/ (This will be created when you run `python -m venv venv`)
