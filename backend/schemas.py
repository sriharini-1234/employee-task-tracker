from datetime import date, datetime
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2)
    email: Optional[EmailStr] = None
    department: Optional[str] = None


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    department: str = Field(min_length=2, max_length=100)


class EmployeeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    department: str
    created_at: Optional[datetime] = None


class TaskCreate(BaseModel):
    title: str = Field(min_length=2, max_length=180)
    description: Optional[str] = None
    priority: Literal["Low", "Medium", "High"] = "Medium"
    due_date: date
    employee_id: int


class TaskStatusUpdate(BaseModel):
    status: Literal["Pending", "In Progress", "Completed"]
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2)
    description: str | None = None
    priority: Literal["Low", "Medium", "High"] | None = None
    due_date: date | None = None
    employee_id: int | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: str
    due_date: date
    status: str
    employee_id: Optional[int] = None
    employee_name: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
