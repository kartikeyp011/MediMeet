import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from db.database import Base, engine
from models.doctor import Doctor
from models.patient import Patient
from models.appointments import Appointment
from models.visit_log import VisitLog

print("🔧 Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")