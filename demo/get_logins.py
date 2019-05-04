import click
import transaction
import zope.sqlalchemy
import os
from models.sql import Login
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
@click.option("--device-id", "-did", type=int, help="device id")
def get_logins(device_id=None):
    with transaction.manager:
        session = get_dbsession(transaction.manager)
        query = session.query(Login)
        if device_id:
            query = query.filter_by(device_id=device_id)
        click.echo([str(l) for l in query])


if __name__ == "__main__":
    get_logins()
