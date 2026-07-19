from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_valid_incident():
    payload = {
        "title": "Customer cannot log in",
        "description": "The customer receives an invalid session error.",
        "requester": "Support Team",
    }

    response = client.post("/incidents", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        **payload,
        "id": 1,
        "status": "open",
    }


def test_reject_incident_with_short_fields():
    payload = {
        "title": "Hi",
        "description": "Too short",
        "requester": "S",
    }

    response = client.post("/incidents", json=payload)

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert len(errors) == 3

def test_create_multiple_incidents_have_unique_ids():
    first_payload = {
        "title": "First incident",
        "description": "This is the first incident.",
        "requester": "Virt",
    }

    second_payload = {
        "title": "Second incident",
        "description": "This is the second incident.",
        "requester": "Virt",
    }

    first_response = client.post("/incidents", json=first_payload)
    second_response = client.post("/incidents", json=second_payload)

    first_id = first_response.json()["id"]
    second_id = second_response.json()["id"]

    assert second_id == first_id + 1