import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_valid_prediction(client):
    response = client.post(
        "/predict",
        json={
            "hours_studied": 6,
            "attendance": 85,
            "previous_score": 72
        }
    )

    assert response.status_code == 200
    assert "predicted_score" in response.get_json()


def test_missing_field(client):
    response = client.post(
        "/predict",
        json={
            "hours_studied": 6
        }
    )

    assert response.status_code == 400


def test_invalid_input(client):
    response = client.post(
        "/predict",
        json={
            "hours_studied": -5,
            "attendance": 85,
            "previous_score": 72
        }
    )

    assert response.status_code == 400