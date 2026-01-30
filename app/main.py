from fastapi import FastAPI

app = FastAPI(title="Notification Service")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "notification-service"}

@app.post("/api/v1/notifications/email")
def send_email(payload: dict):
    return {"id": "notif_001", "type": "email", "status": "queued"}

@app.post("/api/v1/notifications/sms")
def send_sms(payload: dict):
    return {"id": "notif_002", "type": "sms", "status": "queued"}
