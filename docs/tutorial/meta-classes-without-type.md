```python
class Meta:  # this class is a normal class, Meta = instance of type, Only the Meta class does not contain the properties of the type.  # noqa
    @classmethod
    def __prepare__(mcs, cls_name, bases):  # default, staticmethod
        prepare = dict()
        print(f"Meta.__prepare__({mcs=}, {cls_name=}, {bases=}, {prepare=})")
        #       Meta.__prepare__(
        #           mcs=<class '__main__.Meta'>,
        #           cls_name='K',
        #           bases=(),
        #           prepare={}
        #       )

        #       Meta.__prepare__(
        #           mcs=<class '__main__.Meta'>,
        #           cls_name='Example',
        #           bases=(<__main__.Meta object at 0x10b3bea60>,),
        #           prepare={}
        #       )
        return prepare

    def __new__(cls, cls_name, bases, namespace, **kwargs):
        new = super().__new__(cls)
        print(f"Meta.__new__({cls=}, {cls_name=}, {bases=}, {namespace=}, {kwargs=}, {new=})")
        #       Meta.__new__(
        #           mcs=<class '__main__.Meta'>,
        #           cls_name=='K',
        #           bases=(),
        #           namespace={'__module__': '__main__', '__qualname__': 'K'},
        #           kwargs={},
        #           new=<class '__main__.Meta'> ( self )
        #       )

        #       Meta.__new__(
        #           mcs=<class '__main__.Meta'>,
        #           cls_name=='Example',
        #           bases=(<__main__.Meta object at 0x10b3bea60>,),
        #           namespace={'__module__': '__main__', '__qualname__': 'Example', '__new__': <function Example.__new__ at 0x10b3cab80>, '__init__': <function Example.__init__ at 0x10b3cac10>, '__call__': <function Example.__call__ at 0x10b3caca0>, '__classcell__': <cell at 0x10b3bea90: empty>},  # noqa
        #           kwargs={},
        #           new=<class '__main__.Meta'> ( self )
        #       )
        return new

    def __init__(self, cls_name, bases, namespace, **kwargs):
        init = super().__init__()
        print(f"Meta.__init__({self=}, {cls_name=}, {bases=}, {namespace}, {kwargs=}, {init=})")
        #       Meta.__init__(
        #           cls=<class '__main__.Example'>,  ( self )
        #           cls_name='K',
        #           bases=(),
        #           namespace={'__module__': '__main__', '__qualname__': 'K'},  # noqa
        #           kwargs={},
        #           init=None  ( int return None )
        #       )

        #       Meta.__init__(
        #           cls=<class '__main__.Example'>,  ( self )
        #           cls_name='Example',
        #           bases=(<__main__.Meta object at 0x10b3bea60>,),
        #           namespace={'__module__': '__main__', '__qualname__': 'Example', '__new__': <function Example.__new__ at 0x10b3cab80>, '__init__': <function Example.__init__ at 0x10b3cac10>, '__call__': <function Example.__call__ at 0x10b3caca0>, '__classcell__': <cell at 0x10b3bea90: empty>},  # noqa
        #           kwargs={},
        #           init=None  ( int return None )
        #       )

    def __call__(self, *args, **kwargs):
        print(f"Meta.__call__({self=}, {args=}, {kwargs=})")
        #       Meta.__call__(
        #           cls=<class '__main__.Meta'>,
        #           args=(1, 2),
        #           kwargs={'c': 3},
        #           call=<__main__.Example object at 0x10d4c3940>
        #       )

        #       Meta.__call__(
        #           cls=<class '__main__.Meta'>,
        #           args=(1,),
        #           kwargs={'k': 1},
        #           call=<__main__.Example object at 0x10d4c3940>
        #       )
        return self


class K(metaclass=Meta):  # In order to get inherit, it must be instanced of Meta.
    pass                  # Order: Meta.__prepare__, Meta.__new__, Meta.__init__


class Example(K, metaclass=Meta):  # Order: Meta.__prepare__, Meta.__new__, Meta.__init__
    pass


base = Example(1, 2, c=3)             # Meta.__call__
base(1, k=1)                          # Meta.__call__
```
