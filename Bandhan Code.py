from fastapi import FastAPI, Request
import requests

app = FastAPI()

CRM_URL = "https://bsbcrm.bandhan-konnagar.org:7071/api/DataCollection/SaveDataCollectionCollegeHai"

@app.post("/send-lead")
async def send_lead(request: Request):
    payload = await request.json()

    r = requests.post(
        CRM_URL,
        json=payload,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        },
        timeout=15
    )

    return {
        "status_code": r.status_code,
        "response_body": r.text
    }
