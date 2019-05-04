import contextlib
import os

import zope.sqlalchemy
import pytest
import transaction
from ming import create_datastore
from ming.odm import ThreadLocalODMSession
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool


@pytest.fixture(scope="session")
def sql_session():
    engine = create_engine(
        os.getenv("DATABASE_URL"),
        poolclass=NullPool,
    )
    DBSession = scoped_session(sessionmaker())
    DBSession.configure(bind=engine)

    def get_dbsession(transaction_manager):
        zope.sqlalchemy.register(DBSession, transaction_manager=transaction_manager)
        return DBSession

    @contextlib.contextmanager
    def tm_session_ctx():
        with transaction.manager:
            yield get_dbsession(transaction.manager)

    return tm_session_ctx


@pytest.fixture(scope="session")
def ming_session():
    return ThreadLocalODMSession(
        bind=create_datastore(os.getenv("MONGODB_URL")),
    )


metadata = MetaData()
BaseModel = declarative_base(metadata=metadata)
