# 🧪 Testing example for: 27. Advanced Python

def test_basic_behavior():
    expected = "PASS"
    actual = "PASS"
    assert actual == expected

def test_negative_behavior():
    actual = "FAIL"
    expected = "PASS"
    assert actual != expected
