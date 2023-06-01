```python
class Meta(type):
    @classmethod
    def __prepare__(mcs, cls_name, bases, **kwargs):  # default, staticmethod
        print("Meta.__prepare__")
        return super().__prepare__(cls_name, bases)

    def __new__(mcs, cls_name, bases, namespace, **kwargs):
        print(f"Meta.__new__")
        return super().__new__(mcs, cls_name, bases, namespace)

    def __init__(cls, cls_name, bases, namespace, **kwargs):
        print(f"Meta.__init__")
        super().__init__(cls_name, bases, namespace, **kwargs)

    def __call__(cls, *args, **kwargs):
        print(f"Meta.__call__")
        return super().__call__(*args, **kwargs)


class Base:
    pass


class Example(Base, metaclass=Meta):  # Order: Meta.__prepare__, Meta.__new__, Meta.__init__
    # def __prepare__(mcs, cls_name, bases):  # it doesn't work, in this way

    def __new__(cls, *args, **kwargs):
        print(f"Example.__new__")
        return super().__new__(cls)

    def __init__(self):
        print(f"Example.__init__")

    def __call__(self, *args, **kwargs):
        print(f"Example.__call__")


base = Example()             # Meta.__call__, Example.__new__, Example.__init__
base()                       # Example.__call__
```
