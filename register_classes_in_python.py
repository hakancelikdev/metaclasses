class Meta(type):
    _instances = []

    def __new__(mcs, name, bases, namespace, **kwargs):
        instance = super().__new__(mcs, name, bases, namespace)
        if not [b for b in bases if isinstance(b, mcs)]:  # mcs is a Base
            return instance

        mcs._instances.append(name)
        return instance


class Base(metaclass=Meta):
    pass


class Example(Base):
    pass


class Example2(Base):
    pass


assert Example._instances == ["Example", "Example2"]
assert Example2._instances == ["Example", "Example2"]

# -------


class Base:
    _instances = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._instances.append(cls.__name__)


class Example(Base):
    pass


class Example2(Base):
    pass


assert Example._instances == ["Example", "Example2"]
assert Example2._instances == ["Example", "Example2"]


# -------

def decorator(cls):
    if hasattr(cls, "_instances"):
        cls._instances.append(cls.__name__)
    else:
        cls._instances = []

    return cls


@decorator
class Base:
    pass


@decorator
class Example(Base):
    pass


@decorator
class Example2(Base):
    pass


assert Example._instances == ["Example", "Example2"]
assert Example2._instances == ["Example", "Example2"]
