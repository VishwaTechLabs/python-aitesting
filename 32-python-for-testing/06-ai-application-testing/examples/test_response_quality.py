def test_response_is_not_empty():
    response = "A useful answer"
    assert response.strip() != ""

def test_response_contains_expected_topic():
    response = "Python testing uses assertions to validate behavior."
    assert "testing" in response.lower()
