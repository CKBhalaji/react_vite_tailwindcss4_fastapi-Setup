from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file in the current directory (backend/)
load_dotenv()

# Get the database URL from environment variables
# Default to SQLite if DATABASE_URL is not set (for quick local setup)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

# --- Database Engine Setup ---
# echo=True will make SQLAlchemy log all the SQL statements it executes.
# This is very useful for debugging! Set to False for production.
engine = create_engine(DATABASE_URL, echo=True)

# --- Session Management ---
# Dependency to get a database session.
# This function yields a session, ensuring it's closed after the request.
def get_session():
    """
    Dependency function to get a database session.

    This function opens a new database session, yields it for use in a FastAPI route,
    and then ensures the session is closed after the request is finished.
    """
    with Session(engine) as session:
        yield session

# You can also have a function to create tables, which is called on app startup
# This is handled in main.py's @app.on_event("startup")
def create_db_and_tables():
    """
    Creates all database tables defined by SQLModel metadata.
    This is typically called once on application startup.
    """
    SQLModel.metadata.create_all(engine)

"""
--- Database Connection Notes ---

* **SQLite:** `DATABASE_URL="sqlite:///./sql_app.db"`
    -   Creates a file-based database named `sql_app.db` in the `backend/` directory.
    -   Good for local development, quick prototyping, and testing.

* **PostgreSQL:** `DATABASE_URL="postgresql://user:password@host:port/dbname"`
    -   Requires a running PostgreSQL server.
    -   Example: `DATABASE_URL="postgresql://postgres:mysecretpassword@localhost:5432/fastapidb"`
    -   Make sure you have `psycopg2-binary` installed in your `requirements.txt`.

* **MySQL:** `DATABASE_URL="mysql+pymysql://user:password@host:port/dbname"`
    -   Requires `pymysql` (or `mysqlclient`) to be installed (`pip install pymysql`).

* **Other Databases:**
    -   SQLAlchemy supports many other databases. You'll typically need to install the appropriate database driver (e.g., `aiomysql` for async MySQL, `asyncpg` for async PostgreSQL) and adjust the `DATABASE_URL` format accordingly.
    -   The `create_engine` parameters might need adjustments based on the database and driver (e.g., `pool_pre_ping=True` for some databases to handle lost connections).

* **Environment Variables:**
    -   It's best practice to store sensitive information like database credentials in environment variables (e.g., in a `.env` file for local development, or via your deployment platform's secrets management).
    -   `python-dotenv` (used here) helps load these variables during local development.
"""