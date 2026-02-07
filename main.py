from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import urllib3

# Disable SSL warnings (testing only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI(
    title="CollegeHai Lead Proxy API",
    description="Proxy API to push leads to Bandhan CRM",
    version="1.0.0"
)

API_URL = "https://bsbcrm.bandhan-konnagar.org:7071/api/DataCollection/SaveDataCollectionCollegeHai"


# -------- Pydantic Model --------
class LeadPayload(BaseModel):
    city: str
    state: str
    medium: str
    source: str | None = ""
    emailId: str
    passKey: str
    courseId: int
    passCode: str
    contactNo: str
    studentName: str


# -------- API Route --------
@app.post("/push-lead")
def push_lead(payload: LeadPayload):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload.dict(),
            timeout=20,
            verify=False  # ⚠️ testing only
        )

        return {
            "status_code": response.status_code,
            "bandhan_response": response.text
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
