import os
from csv import reader

from dundie.database import add_movement, add_person, commit, connect
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from a file to the database"""
    try:
        csv_data = reader(open(filepath, "r"))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, (item.strip() for item in line)))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)
        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db)
    return people


def read(**query):
    """Reads data from database and filters using query"""
    db = connect()
    return_data = []
    for pk, data in db["people"].items():
        query_dept = query.get("dept")
        if query_dept and query_dept != data["dept"]:
            continue

        query_email = query.get("email")
        if query_email and query_email != pk:
            continue

        return_data.append(
            {
                "email": pk,
                **data,
                "balance": db["balance"][pk],
                "last_movement": db["movement"][pk][-1]["date"],
            }
        )
    return return_data


def add(value, **query):
    """Add value to record on query"""
    return_data = read(**query)
    if not return_data:
        raise (RuntimeError, "No records found")

    db = connect()
    user = os.getenv("USER")
    for user in return_data:
        add_movement(db, user["email"], value, user)
    commit(db)
