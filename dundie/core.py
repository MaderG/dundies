from dundie.utils.log import get_logger
from dundie.database import connect, commit, add_user
from csv import reader

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
        person, created = add_user(db, pk, person_data)
        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db)
    return people
