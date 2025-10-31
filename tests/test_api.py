import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculator API" in response.json()["message"]

def test_add_endpoint():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_subtract_endpoint():
    response = client.get("/subtract", params={"a": 5, "b": 2})
    assert response.status_code == 200
    assert response.json()["result"] == 3

def test_multiply_endpoint():
    response = client.get("/multiply", params={"a": 4, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 12

def test_divide_endpoint():
    response = client.get("/divide", params={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_divide_by_zero_endpoint():
    response = client.get("/divide", params={"a": 10, "b": 0})
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.json()["detail"]

