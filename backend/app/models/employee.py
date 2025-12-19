from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column,Integer,String,Date
from app.core.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    department: Mapped[str] = mapped_column(String(50), index=True)
    designation: Mapped[str] = mapped_column(String(50))
    date_of_joining: Mapped[Date] = mapped_column(Date)
