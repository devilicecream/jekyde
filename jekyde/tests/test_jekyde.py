import sqlalchemy as sa
from ming import schema as s
from ming.odm import MappedClass
from jekyde.drivers import Driver
from jekyde.meta import JekydeModel
from sqlalchemy.orm import configure_mappers
from .conftest import BaseModel


def test_change_type(sql_session, ming_session):
    class AMingModel(MappedClass):
        class __mongometa__:
            session = ming_session
            name = "amodel"

        _id = s.ObjectId()
        value = s.String()

    class ASQLModel(BaseModel):
        __tablename__ = "amodel"

        id = sa.Column(sa.Integer(), primary_key=True)
        value = sa.Column(sa.String(length=32))

    class AModel(JekydeModel):
        _driver = Driver.Ming
        _models = {Driver.Ming: AMingModel, Driver.SQLAlchemy: ASQLModel}

    configure_mappers()

    AModel(value="test")
    ming_session.flush()
    assert AModel.query.find({}).first()

    AModel.use(Driver.SQLAlchemy)
    with sql_session() as session:
        new_obj = AModel(value="test2")
        session.add(new_obj)
        session.flush()
        created = session.query(AModel).get(new_obj.id)
        assert created


def test_migration(sql_session, ming_session):
    class BMingModel(MappedClass):
        class __mongometa__:
            session = ming_session
            name = "bmodel"

        _id = s.ObjectId()
        value = s.String()

    class BSQLModel(BaseModel):
        __tablename__ = "bmodel"

        id = sa.Column(sa.Integer(), primary_key=True)
        value = sa.Column(sa.String(length=32))

    class BModel(JekydeModel):
        _driver = Driver.Ming
        _models = {Driver.Ming: BMingModel, Driver.SQLAlchemy: BSQLModel}

    configure_mappers()
    BModel(value="test")
    ming_session.flush()
    doc = BModel.query.find({}).first()
    assert doc
    with sql_session() as session:
        new_obj = BModel.migrate_to(doc, Driver.SQLAlchemy)
        session.add(new_obj)
        session.flush()
        obj_id = new_obj.id
    with sql_session() as session:
        assert session.query(BSQLModel).get(obj_id)
