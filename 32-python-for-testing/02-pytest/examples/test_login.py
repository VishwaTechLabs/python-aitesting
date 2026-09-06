import pytest

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "secret", True),
        ("admin", "wrong", False),
        ("", "secret", False),
    ],
)
def test_login(username, password, expected):
    actual = username == "admin" and password == "secret"
    assert actual is expected
