# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import Session
# from database import get_db
# from models import Employee, Task
# from schemas import EmployeeCreate, EmployeeOut

# router = APIRouter(prefix="/api/employees", tags=["Employees"])


# @router.post("/", response_model=EmployeeOut, status_code=status.HTTP_201_CREATED)
# def create_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
#     employee = Employee(**payload.model_dump())
#     db.add(employee)
#     try:
#         db.commit()
#         db.refresh(employee)
#     except IntegrityError:
#         db.rollback()
#         raise HTTPException(status_code=409, detail="An employee with this email already exists.")
#     return employee


# @router.get("/", response_model=list[EmployeeOut])
# def list_employees(search: str | None = None, db: Session = Depends(get_db)):
#     query = db.query(Employee)
#     if search:
#         query = query.filter(Employee.name.ilike(f"%{search}%"))
#     return query.order_by(Employee.id.desc()).all()


# @router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_employee(employee_id: int, db: Session = Depends(get_db)):
#     employee = db.query(Employee).filter(Employee.id == employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found.")
#     # Keep assigned tasks; make them unassigned instead of deleting task history.
#     db.query(Task).filter(Task.employee_id == employee_id).update(
#         {Task.employee_id: None}, synchronize_session=False
#     )
#     db.delete(employee)
#     db.commit()
#     return None

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db
from models import Employee, Task
from schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate


router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)


# CREATE EMPLOYEE
@router.post(
    "/",
    response_model=EmployeeOut,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    payload: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employee = Employee(**payload.model_dump())
    db.add(employee)

    try:
        db.commit()
        db.refresh(employee)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="An employee with this email already exists."
        )

    return employee


# GET ALL EMPLOYEES / SEARCH EMPLOYEES
@router.get("/", response_model=list[EmployeeOut])
def list_employees(
    search: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Employee)

    if search:
        query = query.filter(
            Employee.name.ilike(f"%{search}%")
        )

    return query.order_by(Employee.id.desc()).all()


# UPDATE EMPLOYEE
@router.put("/{employee_id}", response_model=EmployeeOut)
def update_employee(
    employee_id: int,
    payload: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if value is not None:
            setattr(employee, field, value)

    try:
        db.commit()
        db.refresh(employee)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="An employee with this email already exists."
        )

    return employee


# DELETE EMPLOYEE
@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    # Preserve assigned tasks by making them unassigned.
    db.query(Task).filter(
        Task.employee_id == employee_id
    ).update(
        {Task.employee_id: None},
        synchronize_session=False
    )

    db.delete(employee)
    db.commit()

    return None
