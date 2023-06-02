```python
class Meta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        if not [base for base in bases if isinstance(base, mcs)]:
            return super().__new__(mcs, name, bases, namespace, **kwargs)

        annotations = namespace.get('__annotations__', {})
        namespace["__slots__"] = tuple(annotations.keys())  # auto __slots__

        return super().__new__(mcs, name, bases, namespace, **kwargs)

    def __call__(cls, **kwargs):
        for field_name, field_type in cls.__annotations__.items():
            if field_name not in kwargs:
                raise ValueError(f"Missing field {field_name}")
            else:
                assert isinstance(kwargs[field_name], field_type), f"Field {field_name} must be of type {field_type}"

        for field_name, field_value in kwargs.items():
            if field_name not in cls.__annotations__:
                raise ValueError(f"Unknown field {field_name}")

        return super().__call__(**kwargs)


class BaseModel(metaclass=Meta):
    def __init__(self, **kwargs):
        for field_name, field_value in kwargs.items():
            setattr(self, field_name, field_value)


class Account(BaseModel):
    first_name: str
    last_name: str
    username: str


account = Account(first_name="Hakan", last_name="Çelik", username="hakancelik")

assert account.__slots__ == ("first_name", "last_name", "username")
assert account.__dict__ == {}

assert account.first_name == "Hakan"
assert account.last_name == "Çelik"
assert account.username == "hakancelik"

# Account(first_name="Hakan", last_name="Çelik", username=1)
```
