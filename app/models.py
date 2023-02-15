import sqlalchemy
from db import db, metadata, sqlalchemy
import bcrypt

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("age", sqlalchemy.Integer),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False)
)


class User:
    @classmethod
    async def get(cls, id):
        query = users.select().where(users.c.id == id)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def get_by_name(cls, username):
        query = users.select().where(users.c.username == username)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def get_by_email(cls, username):
        query = users.select().where(users.c.email == username)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def create(cls, **user):
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(user['password'].encode("utf-8"), salt)
        user['password'] = hash_password.decode("utf-8")
        query = users.insert().values(**user)
        user_id = await db.execute(query)
        return user_id
