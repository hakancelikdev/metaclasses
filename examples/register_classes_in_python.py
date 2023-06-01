class Meta(type):
    _names = []

    def __new__(mcs, name, bases, namespace, **kwargs):
        obj = super().__new__(mcs, name, bases, namespace)
        if not [b for b in bases if isinstance(b, mcs)]:  # mcs is a Base
            return obj

        mcs._names.append(name)
        return obj


class Base(metaclass=Meta):
    pass


class Example(Base):
    pass


class Example2(Base):
    pass


assert Example._names == ["Example", "Example2"]
assert Example2._names == ["Example", "Example2"]

# -------


class Base:
    _names = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._names.append(cls.__name__)


class Example(Base):
    pass


class Example2(Base):
    pass


assert Example._names == ["Example", "Example2"]
assert Example2._names == ["Example", "Example2"]


# -------

def decorator(cls):
    if hasattr(cls, "_names"):
        cls._names.append(cls.__name__)
    else:
        cls._names = []

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


assert Example._names == ["Example", "Example2"]
assert Example2._names == ["Example", "Example2"]
