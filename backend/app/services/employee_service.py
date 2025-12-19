from sqlalchemy.orm import Session
from app.repositories.employee_repo import EmployeeRepository

class EmployeeService:


  @staticmethod
  def search_employees(db:Session, search:str):
    if not search or not search.strip():
      raise ValueError("Search term cannot be empty...")

    search = search.strip()

    return EmployeeRepository.search_employees(db,search)