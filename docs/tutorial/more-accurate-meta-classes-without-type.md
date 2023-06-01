```python
class Meta:
    def __prepare__(name, bases, **kwargs):
        return dict()

    def __new__(cls, name, bases, namespace, **kwargs):
        obj = object.__new__(cls)

        obj.__init__(name, bases, namespace, **kwargs)
        return obj

    def __init__(self, name, bases, namespace, **kwargs):
        self.name = name
        self.bases = bases
        self.namespace = namespace
        self.kwargs = kwargs

        self.__call_run = False

    def __call__(self, *args, **kwargs):
        if not self.__call_run:
            self.__call_run = True

            cls_new = self.namespace["__new__"]
            cls_init = self.namespace["__init__"]

            obj = cls_new(self, *args, **kwargs)
            cls_init(obj, *args, **kwargs)
        else:
            cls_call = self.namespace["__call__"]
            obj = cls_call(self, *args, **kwargs)

        return obj

    def __str__(self):
        if not self.__call_run:
            return "<Meta: {}>".format(self.name)
        else:
            return self.namespace["__str__"](self)

    def __repr__(self):
        return self.__str__()

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        object.__delattr__(self, name)

    def __getitem__(self, key):
        return self.namespace[key]

    def __setitem__(self, key, value):
        self.namespace[key] = value

    def __delitem__(self, key):
        del self.namespace[key]

    def __len__(self):
        return len(self.namespace)

    def __contains__(self, item):
        return item in self.namespace

    def __iter__(self):
        return iter(self.namespace)

    def __reversed__(self):
        return reversed(self.namespace)



class Klass(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        return cls

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __str__(self):
        return "<Klass: {}>".format(self.name)


klass = Klass(1, a=1)
klass(deneme=3)

print(klass)
```
