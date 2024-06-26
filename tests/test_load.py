import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
def test_load_positive_has_2_people():
    """Test the load function"""
    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
def test_load_positive_has_first_name_starts_with_j():
    """Test the load function"""
    assert load(PEOPLE_FILE)[0]["name"][0] == "J"
