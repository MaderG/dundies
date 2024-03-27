import pytest
from dundie.utils.email import is_email
from dundie.utils.user import generate_password


@pytest.mark.unit
@pytest.mark.parametrize("email", ["jim@dunder.com", "a2@b.com"])
def test_positive_valid_email(email):
    """Verifies if the email is valid"""
    assert is_email(email) is True


@pytest.mark.unit
@pytest.mark.parametrize("email", [".@dunder", "@b", "a@.com"])
def test_negative_valid_email(email):
    """Verifies if the email is invalid"""
    assert is_email(email) is False


@pytest.mark.unit
def test_generate_password():
    """Test generation of passwords"""
    passwords = []
    for _ in range(100):
        passwords.append(generate_password(8))
    assert len(set(passwords)) == 100
