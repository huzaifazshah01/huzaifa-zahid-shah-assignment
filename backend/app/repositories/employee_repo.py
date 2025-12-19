from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.employee import Employee

class EmployeeRepository:
  @staticmethod
  def search_employees(db:Session, query:str):
    return (
      db.query(Employee).filter(
      or_(
        Employee.name.ilike(f"%{query}%"),
        Employee.department.ilike(f"%{query}%")
      )
    ).all()
  )
