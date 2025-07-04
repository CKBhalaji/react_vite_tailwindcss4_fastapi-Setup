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
    git clone [https://github.com/your-username/reactvite-tailwind-fastapi.git](https://github.com/your-username/reactvite-tailwind-fastapi.git)
    cd reactvite-tailwind-fastapi
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