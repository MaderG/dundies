import json
from dundie.settings import EMAIL_FROM
from dundie.settings import DATABASE_PATH
from dundie.utils.user import generate_password
from dundie.utils.email import is_email, send_email
from datetime import datetime

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


def add_user(db, pk, data):
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


def add_movement(db, pk, value):
    """Add movement to the database"""
    movements = db["movement"].setdefault(pk, [])
    movements.append(
        {
            "date": datetime.now().isoformat(),
            "amount": value,
            "actor": "system",
        }
    )
    db["balance"][pk] = sum(m["amount"] for m in movements)
