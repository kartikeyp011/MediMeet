from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class AppointmentCreate(BaseModel):
    doctor_id: UUID
    patient_id: UUID
    start_time: datetime
    end_time: datetime
    reason: Optional[str] = None
    source: Optional[str] = "llm"


class AppointmentResponse(BaseModel):
    id: UUID
    doctor_id: UUID
    patient_id: UUID
    start_time: datetime
    end_time: datetime
    status: str
    reason: Optional[str] = None
    source: Optional[str] = "llm"
    created_at: datetime

    class Config:
        orm_mode = True