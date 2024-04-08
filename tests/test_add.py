import pytest

from dundie.core import add
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_add_movement():
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

    add(-50, email="stanley@dundermifflin.com")
    add(90, dept="Management")
    db = connect()
    assert db["balance"]["stanley@dundermifflin.com"] == 450
    assert db["balance"]["jim@dundermifflin.com"] == 190
