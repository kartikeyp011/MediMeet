from sqlalchemy import Column, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

from app.db.base import Base

class VisitLog(Base):
    __tablename__ = "visit_logs"  # 📌 Use plural for consistency

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    appointment_id = Column(UUID(as_uuid=True), ForeignKey("appointments.id"), nullable=False)

    symptoms = Column(Text, nullable=True)   # Optional field (if parsed by LLM)
    summary = Column(Text, nullable=False)   # Doctor or AI-generated notes
    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔄 Relationship to Appointment
    appointment = relationship("Appointment", backref="visit_log")

    def __repr__(self):
        return f"<VisitLog(id={self.id}, appointment_id={self.appointment_id})>"