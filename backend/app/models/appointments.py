from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4

from app.db.base import Base  # ✅ consistent Base import

class Appointment(Base):
    __tablename__ = "appointments"  # 📌 Use plural for table name (recommended convention)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    
    status = Column(String, default="scheduled")     # scheduled, cancelled, rescheduled
    reason = Column(String, nullable=True)           # Optional LLM-parsed reason
    source = Column(String, default="dashboard")     # "dashboard" or "booked_via_llm"

    created_at = Column(DateTime, default=datetime.utcnow)

    # ✅ Relationships (assumes Doctor and Patient models exist with proper tablenames)
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.id}, doctor_id={self.doctor_id}, start={self.start_time})>"
