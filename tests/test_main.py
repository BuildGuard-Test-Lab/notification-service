from app.main import app
from fastapi import FastAPI


def test_app_is_fastapi_instance():
    assert isinstance(app, FastAPI)


def test_app_title():
    assert app.title == "Notification Service"


def test_health_route_exists():
    routes = [route.path for route in app.routes]
    assert "/health" in routes


def test_email_route_exists():
    routes = [route.path for route in app.routes]
    assert "/api/v1/notifications/email" in routes


def test_sms_route_exists():
    routes = [route.path for route in app.routes]
    assert "/api/v1/notifications/sms" in routes
