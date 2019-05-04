from datetime import datetime

import click
import transaction
import zope.sqlalchemy
import os
from models.sql import Login
# from models import Login
# from models.mongo import MingSession
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
@click.option("--device-id", "-did", required=True, type=int, help="device id")
def make_login(device_id=None):
    # session = MingSession
    with transaction.manager:
        session = get_dbsession(transaction.manager)
        login = Login(device_id=device_id, datetime=datetime.utcnow())
        session.add(login)
        session.flush()
        click.echo(login)


if __name__ == "__main__":
    make_login()
