import click
import transaction
import zope.sqlalchemy
import os
from models.sql import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, configure_mappers
from sqlalchemy.pool import NullPool

DBSession = scoped_session(sessionmaker())


def get_dbsession(transaction_manager):
    zope.sqlalchemy.register(DBSession, transaction_manager=transaction_manager)
    return DBSession


engine = create_engine(
    os.getenv("DATABASE_URL"),
    poolclass=NullPool,
)
DBSession.configure(bind=engine)
configure_mappers()

@click.command()
@click.option("--user-id", "-id", type=int, help="user id")
def get_user(user_id=None):
    with transaction.manager:
        session = get_dbsession(transaction.manager)
        if user_id:
            user = session.query(User).get(user_id)
            click.echo(user)
            return
        click.echo([str(u) for u in session.query(User)])


if __name__ == "__main__":
    get_user()
