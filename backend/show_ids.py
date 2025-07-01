from app.db.database import SessionLocal
from app.models import Doctor, Patient

db = SessionLocal()

doctors = db.query(Doctor).all()
patients = db.query(Patient).all()

print("\n👨‍⚕️ Doctors:")
for doc in doctors:
    print(f"{doc.name} — {doc.id}")

print("\n🧍 Patients:")
for pat in patients:
    print(f"{pat.name} — {pat.id}")

db.close()