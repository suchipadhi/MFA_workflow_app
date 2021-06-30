from api.utils.dbutils import database
from api.auth import schema


def find_exist_user(email: str):
    query = "select * from py_users where email=:email"
    return database.fetch_one(query, values={"email": email})


def save_user(user: schema.UserCreate):
    query = "INSERT INTO py_users VALUES (nextval('user_id_seq'), :email, :password, now() at time zone 'CET')"
    return database.execute(query, values={"email": user.email, "password": user.password})
