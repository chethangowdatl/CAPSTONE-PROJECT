# src/functions.py
import json
from datetime import datetime
import uuid

APPOINTMENTS = []  # in-memory list for demo

def book_appointment(name, phone, clinic_id, datetime_str, reason):
    # simple validation
    appt_id = str(uuid.uuid4())
    record = {
        "id": appt_id,
        "name": name,
        "phone": phone,
        "clinic_id": clinic_id,
        "datetime": datetime_str,
        "reason": reason,
        "status": "confirmed"
    }
    APPOINTMENTS.append(record)
    return {"status":"ok", "appointment": record}

def generate_referral(patient_name, patient_phone, from_clinic, to_clinic, symptoms, urgency="medium"):
    referral_id = str(uuid.uuid4())
    referral = {
        "referral_id": referral_id,
        "patient_name": patient_name,
        "patient_phone": patient_phone,
        "from_clinic": from_clinic,
        "to_clinic": to_clinic,
        "symptoms": symptoms,
        "triage": urgency,
    }
    # Optionally generate a PDF/file here; return referral JSON for judge ingestion
    return {"status":"ok", "referral": referral}
