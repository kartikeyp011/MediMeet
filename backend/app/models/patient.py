from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

from app.db.base import Base

class Patient(Base):
    __tablename__ = "patients"  # 📌 Use plural for consistency

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔄 One-to-many relationship with appointments
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete")

    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.name})>"