from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_table():
    response = client.get("/tables/")
    assert response.status_code == 200

def test_create_table():
    data = {
    "name": "string",
    "seats": 10,
    "location": "string"
    }
    response = client.post('/tables/', json=data)
    assert response.status_code == 422
