from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import date


class DoctorSummaryRequest(BaseModel):
    doctor_id: UUID
    date: Optional[date] = None  # Defaults to today if not provided


class DoctorSummaryResponse(BaseModel):
    doctor_id: UUID
    date: date
    total_appointments: int
    fever_cases: Optional[int] = 0  # Optional bonus field