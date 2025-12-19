from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.employee_service import EmployeeService
from app.schemas.employee import EmployeeResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[EmployeeResponse],
    summary="Search employees",
    description="Search employees by name or department"
)
def search_employees(
    search: str = Query(..., min_length=1, description="Search keyword"),
    db: Session = Depends(get_db)
):
    try:
        return EmployeeService.search_employees(db, search)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
