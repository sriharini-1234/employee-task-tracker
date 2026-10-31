import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import get_db
from models import Employee, Task
from routers import employees, tasks

app = FastAPI(
    title="Employee Task Tracker API",
    description="REST API for employee and task management.",
    version="1.0.0",
)

origins = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Employee Task Tracker API is running"}


@app.get("/api/dashboard")
def dashboard(db: Session = __import__("fastapi").Depends(get_db)):
    total_employees = db.query(func.count(Employee.id)).scalar() or 0
    total_tasks = db.query(func.count(Task.id)).scalar() or 0
    completed = db.query(func.count(Task.id)).filter(Task.status == "Completed").scalar() or 0
    pending = db.query(func.count(Task.id)).filter(Task.status == "Pending").scalar() or 0
    in_progress = db.query(func.count(Task.id)).filter(Task.status == "In Progress").scalar() or 0
    return {
        "total_employees": total_employees,
        "total_tasks": total_tasks,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "in_progress_tasks": in_progress,
    }
