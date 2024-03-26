from random import sample
from string import ascii_letters, digits


def generate_password(len=8):
    """Generate a random password of given length"""
    password = "".join(sample(ascii_letters + digits, len))
    return password
