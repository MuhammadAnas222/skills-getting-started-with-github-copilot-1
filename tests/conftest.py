import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def activities(monkeypatch):
    test_activities = {
        "Chess Club": {
            "description": "Practice chess",
            "schedule": "Fridays",
            "max_participants": 4,
            "participants": ["existing@example.edu"],
        },
        "Art Club": {
            "description": "Make art",
            "schedule": "Wednesdays",
            "max_participants": 4,
            "participants": [],
        },
    }
    monkeypatch.setattr(app_module, "activities", test_activities)
    return test_activities


@pytest.fixture
def client(activities):
    return TestClient(app_module.app)