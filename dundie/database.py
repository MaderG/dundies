import json
from datetime import datetime

from dundie.settings import DATABASE_PATH, EMAIL_FROM
from dundie.utils.email import is_email, send_email
from dundie.utils.user import generate_password

DB_SCHEMA = {
    "people": {},
    "balance": {},
    "movement": {},
    "users": {},
}


def connect():
    try:
        with open(DATABASE_PATH, "r") as f:
            return json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError):
        return DB_SCHEMA


def commit(db):
    if db.keys() != DB_SCHEMA.keys():
        raise ValueError("Database schema mismatch")
    with open(DATABASE_PATH, "w") as f:
        f.write(json.dumps(db, indent=4))


def add_person(db, pk, data):
    """Saves a user to the database"""
    if is_email(pk) is False:
        raise ValueError("Invalid email")
    table = db["people"]
    person = table.get(pk, {})
    created = not bool(person)
    person.update(data)
    table[pk] = person
    if created:
        set_balance(db, pk, person)
        password = set_initial_password(db, pk)
        send_email(
            EMAIL_FROM,
            [pk],
            "Welcome to Dundie",
            f"Your password is {password}",
        )
    return person, created


def set_initial_password(db, pk):
    """Generates and save password"""
    password = generate_password()
    user = db["users"].setdefault(pk, {})
    user["password"] = password
    return user["password"]


def set_balance(db, pk, person):
    """Add movement and set inicial balance"""
    value = 100 if person["role"] == "Manager" else 500
    add_movement(db, pk, value)


def add_movement(db, pk, value, actor="system"):
    """Add movement to user account"""
    movements = db["movement"].setdefault(pk, [])
    movements.append(
        {
            "date": datetime.now().isoformat(),
            "amount": value,
            "actor": actor,
        }
    )
    db["balance"][pk] = sum(m["amount"] for m in movements)
