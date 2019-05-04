import sqlalchemy as sa

from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

metadata = MetaData()
BaseModel = declarative_base(metadata=metadata)


class User(BaseModel):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    full_name = sa.Column(sa.String(length=32))

    def __str__(self):
        return f"<User id={self.id} name='{self.full_name}'' device_id={self.device.id}>"


class Device(BaseModel):
    __tablename__ = "devices"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), index=True)
    user = relationship(
        "User", backref=backref("device", uselist=False, cascade="all, delete-orphan")
    )

    def __str__(self):
        return f"<Device id={self.id}>"


class Login(BaseModel):
    __tablename__ = "logins"

    id = sa.Column(sa.Integer, primary_key=True)
    device_id = sa.Column(sa.Integer, sa.ForeignKey("devices.id"), index=True)
    device = relationship(
        "Device", backref=backref("logins", uselist=True, cascade="all, delete-orphan")
    )
    datetime = sa.Column(sa.DateTime, default=datetime.utcnow())

    def __str__(self):
        return f"<Login device_id={self.device_id} datetime={self.datetime}>"
