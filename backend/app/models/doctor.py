from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.db.base import Base

class Doctor(Base):
    __tablename__ = "doctors"  # 📌 Use plural form for table names

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    specialization = Column(String, nullable=True)
    timezone = Column(String, nullable=True)
    is_available = Column(Boolean, default=True)

    # 🔄 One-to-many relationship with appointments
    appointments = relationship("Appointment", back_populates="doctor", cascade="all, delete")

    def __repr__(self):
        return f"<Doctor(id={self.id}, name={self.name})>"