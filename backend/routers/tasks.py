# from fastapi import APIRouter, Depends, HTTPException, Query, status
# from sqlalchemy.orm import Session, joinedload
# from database import get_db
# from models import Employee, Task
# from schemas import TaskCreate, TaskOut, TaskStatusUpdate

# router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


# def serialize_task(task: Task) -> dict:
#     return {
#         "id": task.id,
#         "title": task.title,
#         "description": task.description,
#         "priority": task.priority,
#         "due_date": task.due_date,
#         "status": task.status,
#         "employee_id": task.employee_id,
#         "employee_name": task.employee.name if task.employee else None,
#         "created_at": task.created_at,
#     }


# @router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
# def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
#     employee = db.query(Employee).filter(Employee.id == payload.employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=404, detail="Selected employee does not exist.")
#     task = Task(**payload.model_dump())
#     db.add(task)
#     db.commit()
#     db.refresh(task)
#     return serialize_task(task)


# @router.get("/", response_model=list[TaskOut])
# def list_tasks(
#     status_filter: str | None = Query(default=None, alias="status"),
#     search: str | None = None,
#     db: Session = Depends(get_db),
# ):
#     query = db.query(Task).options(joinedload(Task.employee))
#     if status_filter:
#         allowed = {"Pending", "In Progress", "Completed"}
#         if status_filter not in allowed:
#             raise HTTPException(status_code=400, detail="Invalid task status.")
#         query = query.filter(Task.status == status_filter)
#     if search:
#         query = query.filter(Task.title.ilike(f"%{search}%"))
#     return [serialize_task(task) for task in query.order_by(Task.id.desc()).all()]


# @router.patch("/{task_id}/status", response_model=TaskOut)
# def update_task_status(task_id: int, payload: TaskStatusUpdate, db: Session = Depends(get_db)):
#     task = db.query(Task).options(joinedload(Task.employee)).filter(Task.id == task_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found.")
#     task.status = payload.status
#     db.commit()
#     db.refresh(task)
#     return serialize_task(task)


# @router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found.")
#     db.delete(task)
#     db.commit()
#     return None


from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session, joinedload

from database import get_db
from models import Employee, Task
from schemas import TaskCreate, TaskOut, TaskStatusUpdate, TaskUpdate

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


def serialize_task(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "due_date": task.due_date,
        "status": task.status,
        "employee_id": task.employee_id,
        "employee_name": task.employee.name if task.employee else None,
        "created_at": task.created_at,
    }


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(
        Employee.id == payload.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Selected employee does not exist."
        )

    task = Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return serialize_task(task)


@router.get("/", response_model=list[TaskOut])
def list_tasks(
    status_filter: str | None = Query(default=None, alias="status"),
    search: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Task).options(joinedload(Task.employee))

    if status_filter:
        allowed = {"Pending", "In Progress", "Completed"}

        if status_filter not in allowed:
            raise HTTPException(
                status_code=400,
                detail="Invalid task status."
            )

        query = query.filter(Task.status == status_filter)

    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))

    tasks = query.order_by(Task.id.desc()).all()

    return [serialize_task(task) for task in tasks]


# NEW: Edit task details
@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    update_data = payload.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    # Validate the employee if a new employee is assigned
    if "employee_id" in update_data:
        employee = db.query(Employee).filter(
            Employee.id == update_data["employee_id"]
        ).first()

        if not employee:
            raise HTTPException(
                status_code=404,
                detail="Selected employee does not exist."
            )

    # Update only the supplied fields.
    # Task status remains unchanged.
    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()

    # Fetch again to get the latest employee relationship
    updated_task = (
        db.query(Task)
        .options(joinedload(Task.employee))
        .filter(Task.id == task_id)
        .first()
    )

    return serialize_task(updated_task)


@router.patch("/{task_id}/status", response_model=TaskOut)
def update_task_status(
    task_id: int,
    payload: TaskStatusUpdate,
    db: Session = Depends(get_db)
):
    task = (
        db.query(Task)
        .options(joinedload(Task.employee))
        .filter(Task.id == task_id)
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    task.status = payload.status
    db.commit()

    db.refresh(task)

    return serialize_task(task)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    db.delete(task)
    db.commit()

    return None
