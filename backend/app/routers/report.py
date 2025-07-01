from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, datetime

from app.schemas.doctor import DoctorSummaryRequest, DoctorSummaryResponse
from app.db.database import get_db
from app.models.appointments import Appointment

router = APIRouter(tags=["Doctor Reports"])

@router.post("/summary", response_model=DoctorSummaryResponse)
def get_doctor_summary(payload: DoctorSummaryRequest, db: Session = Depends(get_db)):
    target_date = payload.date or date.today()

    # Find appointments for that doctor and date
    appointments = db.query(Appointment).filter(
        Appointment.doctor_id == payload.doctor_id,
        Appointment.start_time >= datetime.combine(target_date, datetime.min.time()),
        Appointment.start_time <= datetime.combine(target_date, datetime.max.time()),
    ).all()

    # Count total and fever cases
    total = len(appointments)
    fever_cases = sum(1 for a in appointments if a.reason and "fever" in a.reason.lower())

    return DoctorSummaryResponse(
        doctor_id=payload.doctor_id,
        date=target_date,
        total_appointments=total,
        fever_cases=fever_cases,
    )