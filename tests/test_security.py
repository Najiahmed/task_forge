# tests/test_security.py

from security.password import hash_password, verify_password


def test_hash_password():
    password = "secret123"

    hashed = hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password


def test_verify_password_correct():
    password = "secret123"
    hashed = hash_password(password)

    result = verify_password(password, hashed)

    assert result is True


def test_verify_password_wrong():
    password = "secret123"
    hashed = hash_password(password)

    result = verify_password("wrong_password", hashed)

    assert result is False