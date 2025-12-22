from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from flask import app
from app.routers.employee_router import router as employee_router
from app.core.database import Base, engine

def create_application() -> FastAPI:
  app = FastAPI(
    title = "Employee Directory",
    description = "For managing and searching employee records",
    version = "1.0.0"
  )
  app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
  app.include_router(employee_router,prefix="/employees",tags = ["Employees"])

  return app

app = create_application()

@app.on_event("startup")
def on_startup():
  Base.metadata.create_all(bind=engine)
