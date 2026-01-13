from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_get_todo():
    payload = {"title": "Test todo", "description": "demo", "completed": False}
    create_resp = client.post("/todos", json=payload)
    assert create_resp.status_code == 201
    data = create_resp.json()
    assert data["title"] == payload["title"]

    todo_id = data["id"]
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == todo_id
