import pytest

from dundie.database import (
    DB_SCHEMA,
    add_movement,
    add_person,
    commit,
    connect,
)


@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == DB_SCHEMA.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    db["people"]["michaelscott@dundermifflin.com"] = {
        "name": "Michael Scott",
        "role": "Regional Manager",
        "department": "Management",
    }
    commit(db)
    db = connect()
    assert db["people"]["michaelscott@dundermifflin.com"] == {
        "name": "Michael Scott",
        "role": "Regional Manager",
        "department": "Management",
    }


@pytest.mark.unit
def test_add_person_for_the_first_time():
    pk = "stanleyh@dundermifflin.com"
    data = {
        "name": "Stanley Hudson",
        "role": "Salesman",
        "department": "Sales",
    }

    db = connect()
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)
    db = connect()
    assert db["people"][pk] == data
    assert db["balance"][pk] == 500
    assert len(db["movement"][pk]) > 0
    assert db["movement"][pk][0]["amount"] == 500


@pytest.mark.unit
def test_negative_add_person_invalid_email():
    with pytest.raises(ValueError):
        db = {}
        add_person(db, "ed@valdo", {})


@pytest.mark.unit
def test_positive_add_value_for_user():
    pk = "joe@doe.com"
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "department": "Sales",
    }
    db = connect()
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)
    db = connect()
    old_balance = db["balance"][pk]
    add_movement(db, pk, 100)
    commit(db)
    db = connect()
    new_balance = db["balance"][pk]
    assert new_balance == old_balance + 100
    assert new_balance == 600
    assert old_balance == 500
