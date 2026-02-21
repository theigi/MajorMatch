import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_root_endpoint():
    """Test if the API root is accessible"""
    # Create transport for the FastAPI app
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

@pytest.mark.asyncio
async def test_prediction_endpoint():
    """Test if the ML model returns a prediction for valid data"""
    payload = {
        "math": 90.0,
        "physics": 85.0,
        "chemistry": 80.0,
        "english": 70.0,
        "interest": "Technology"
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/predict", json=payload)
    
    assert response.status_code == 200
    assert "major" in response.json()
    assert isinstance(response.json()["major"], str)

@pytest.mark.asyncio
async def test_invalid_data_validation():
    """Test if the API correctly rejects scores out of range (0-100)"""
    invalid_payload = {
        "math": 150.0,
        "physics": 85.0,
        "chemistry": 80.0,
        "english": 70.0,
        "interest": "Technology"
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/predict", json=invalid_payload)
    
    assert response.status_code == 422