from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as original_activities


@pytest.fixture(autouse=True)
def reset_activities():
    original_state = deepcopy(original_activities)
    try:
        yield
    finally:
        original_activities.clear()
        original_activities.update(original_state)


@pytest.fixture
def client():
    return TestClient(app)
