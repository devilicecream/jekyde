from sqlalchemy.inspection import _inspects
from sqlalchemy.orm.base import _inspect_mapped_class
from sqlalchemy.schema import SchemaItem as sSchemaItem
from ming.schema import SchemaItem as mSchemaItem


class InvalidDriver(Exception):
    pass


class SameDriverException(InvalidDriver):
    pass


def jekyde_inspects(cls):
    _inspects(cls)(cls._inspect_mapped_class)
    return cls


@jekyde_inspects
class JekydeModelMeta(type):
    def __getattr__(cls, item):
        try:
            return getattr(cls._models[cls._driver], item)
        except KeyError:
            return getattr(super(JekydeModelMeta, cls), item)

    def _inspect_mapped_class(cls):
        return _inspect_mapped_class(cls._models[cls._driver])


class JekydeModel(metaclass=JekydeModelMeta):
    _models = {}
    _driver = None

    def __init__(self, *args, **kw):
        cls = self.__class__
        self._obj = cls._models[cls._driver](*args, **kw)

    def __getattr__(self, item):
        try:
            return getattr(self._obj, item)
        except KeyError:
            return getattr(super(JekydeModel, self), item)

    @classmethod
    def _check_different_driver(cls, driver):
        if driver == cls._driver:
            raise SameDriverException(f"Driver in use is already {driver}")

    @classmethod
    def use(cls, driver):
        cls._check_different_driver(driver)
        selected = cls._models.get(driver)
        if not selected:
            raise InvalidDriver(f"Can't select model for driver: {driver}")
        cls._driver = driver
        return cls

    @classmethod
    def migrate_to(cls, obj, driver):
        obj_class = obj.__class__
        values = dict(
            (name, val)
            for name, val in obj.__dict__.items()
            if isinstance(getattr(obj_class, name, None), sSchemaItem)
            or isinstance(getattr(obj_class, name, None), mSchemaItem)
        )
        new_obj = cls._models[driver](**values)
        return new_obj
