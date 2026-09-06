def test_api_response_shape():
    response = {"id": 101, "name": "Vishwa", "active": True}
    assert isinstance(response, dict)
    assert response["id"] > 0
    assert "name" in response
