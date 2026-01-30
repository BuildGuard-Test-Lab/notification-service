# Notification Service

Sends email, SMS, and push notifications. Integrates with SendGrid and Twilio.

## Tech Stack
- Python 3.12
- FastAPI
- Celery + Redis
- SendGrid / Twilio SDKs

## Getting Started
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
