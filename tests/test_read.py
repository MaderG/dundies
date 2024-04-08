import pytest

from dundie.core import read
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_with_query():
    db = connect()
    pk = "stanley@dundermifflin.com"
    data = {
        "name": "Stanley Hudson",
        "role": "Salesman",
        "dept": "Sales",
    }
    _, created = add_person(db, pk, data)
    assert created is True

    pk = "jim@dundermifflin.com"
    data = {
        "name": "Jim Halpert",
        "role": "Manager",
        "dept": "Management",
    }
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)
    response = read()
    assert len(response) == 2
    response = read(dept="Management")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Halpert"
    response = read(email="jim@dundermifflin.com")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Halpert"
