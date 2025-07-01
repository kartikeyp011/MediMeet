# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.db.base import Base

# Optional: create tables here if you don’t want a separate init_db.py
# Base.metadata.create_all(bind=engine)

# Import your routers
from app.routers import appointment, report

app = FastAPI(
    title="MediMeet AI Backend",
    description="LLM-powered doctor appointment & reporting assistant",
    version="1.0.0"
)

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])
app.include_router(report.router, prefix="/reports", tags=["Reports"])