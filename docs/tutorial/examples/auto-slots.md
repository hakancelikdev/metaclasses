```python
class Meta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        __slots__ = namespace.get("__slots__", ())
        if not __slots__:
            if __init__ := namespace.get("__init__", None):
                __slots__ = __init__.__code__.co_names
                namespace["__slots__"] = __slots__
        return super().__new__(mcs, name, bases, namespace, **kwargs)


class AutoSlots(metaclass=Meta):
    pass


class Example(AutoSlots):
    def __init__(self, field: str, *, keyword_field: int):
        self.field = field
        self.keyword_field = keyword_field
        self.constant = "constant"


assert Example.__slots__ == ("field", "keyword_field", "constant")
assert Example("field", keyword_field=1).__dict__ == {}
```
