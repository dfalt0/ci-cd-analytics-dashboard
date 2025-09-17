from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_builds_empty():
    response = client.get("/builds")
    assert response.status_code == 200
    assert response.json() == []

# more tests
