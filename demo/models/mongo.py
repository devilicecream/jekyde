import os

from ming.odm import MappedClass, ThreadLocalODMSession
from ming import schema as s, create_datastore

MingSession = ThreadLocalODMSession(bind=create_datastore(os.getenv("MONGODB_URL")))


class Login(MappedClass):
    class __mongometa__:
        session = MingSession
        name = "logins"

    _id = s.ObjectId()
    id = s.Int()
    device_id = s.Int()
    datetime = s.DateTime()

    def __str__(self):
        return f"<Login(mongo) device_id={self.device_id} datetime={self.datetime}>"
