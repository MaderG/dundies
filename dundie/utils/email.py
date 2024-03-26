import re


def is_email(email):
    """Return True if the email is valid"""
    return (
        re.match(r"\b[A-Za-z0-9._+-]+@[A-za-z0-9.-]+\.[A-z|a-z]{2,}\b", email)
        is not None
    )