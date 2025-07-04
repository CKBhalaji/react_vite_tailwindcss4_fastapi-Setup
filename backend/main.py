from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel
from dotenv import load_dotenv
from sqlalchemy import text
import os

from .database import engine, get_session # Change back to relative import
from .models import Base, Item as DBItem, User as DBUser # Import SQLAlchemy models, possibly aliased
from .schemas import Item, ItemCreate # Import Pydantic schemas

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Full-Stack AI Starter Backend",
    description="FastAPI backend for a React Vite Tailwind starter kit.",
    version="0.1.0",
)

# --- CORS Middleware ---
# This is crucial for allowing your frontend (running on a different port/origin)
# to make requests to your backend API.
origins = [
    "http://localhost",
    "http://localhost:5173", # Default Vite development server port
    # Add other origins where your frontend might be hosted in production
    # "https://your-production-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Allows all headers
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("Database tables created (if they didn't exist).")

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/database-status")
async def get_db_status(db: Session = Depends(get_session)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Database connection successful!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": "Database connection failed", "error": str(e)})


# Example of how to use the Pydantic schemas for your Item routes:

# Create an Item
@app.post("/api/items/", response_model=Item) # Use Pydantic Item for response
def create_item(item: ItemCreate, db: Session = Depends(get_session)): # Use ItemCreate for request body
    db_item = DBItem(**item.model_dump()) # Create SQLAlchemy model from Pydantic data
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get all Items
@app.get("/api/items/", response_model=list[Item]) # Use Pydantic Item for response list
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    items = db.query(DBItem).offset(skip).limit(limit).all()
    return items

# Get a single Item
@app.get("/api/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_session)):
    item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item