from pydantic import BaseModel, EmailStr
from datetime import date

class EmployeeBase(BaseModel):
  name:str
  email:EmailStr
  department: str | None = None
  designation: str | None = None
  date_of_joining: date | None = None

class EmployeeResponse(EmployeeBase):
  id:int

  class Config:
    orm_mode = True
    