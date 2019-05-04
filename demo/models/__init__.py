from .mongo import Login as MingLogin
from .sql import Login as SQLLogin
from drivers import Driver
from meta import JekydeModel


class Login(JekydeModel):
    _driver = Driver.Ming
    _models = {Driver.Ming: MingLogin, Driver.SQLAlchemy: SQLLogin}
