from app.models import Doctor, Patient
from app.db.database import SessionLocal
import uuid
from datetime import datetime

# Create DB session
db = SessionLocal()

# Dummy Doctors
doctors = [
    Doctor(
        id=uuid.uuid4(),
        name="Dr. Ahuja",
        email="ahuja@example.com",
        specialization="General Physician",
        timezone="Asia/Kolkata"
    ),
    Doctor(
        id=uuid.uuid4(),
        name="Dr. Meera Sharma",
        email="meera.sharma@example.com",
        specialization="Cardiologist",
        timezone="Asia/Kolkata"
    )
]

# Dummy Patients
patients = [
    Patient(
        id=uuid.uuid4(),
        name="Raj Malhotra",
        email="raj.malhotra@example.com",
        created_at=datetime.utcnow()
    ),
    Patient(
        id=uuid.uuid4(),
        name="Anjali Sinha",
        email="anjali.sinha@example.com",
        created_at=datetime.utcnow()
    )
]

# Insert into DB
db.add_all(doctors + patients)
db.commit()

# Print inserted IDs
print("\n✅ Dummy Data Inserted:")
for doctor in doctors:
    print(f"Doctor: {doctor.name} → {doctor.id}")

for patient in patients:
    print(f"Patient: {patient.name} → {patient.id}")

# Close session
db.close()