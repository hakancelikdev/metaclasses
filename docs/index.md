## Metaclasses

- [Understanding Python Classes](./tutorial/understanding-python-classes.md)
- [Dynamic Class Creation](./tutorial/dynamic-class-creation.md)
- [More Accurate Dynamic Class Creation](./tutorial/more-accurate-dynamic-class-creation.md)
- [Metaclasses in Python](./tutorial/metaclasses-in-python.md)
- [Run Methods Order in Python](./tutorial/run-methods-order-in-python.md)
- [Run Methods Order in Python with More Explanation](./tutorial/run-methods-order-in-python-with-more-explanation.md)
- [Invisible Metaclasses in Python](./tutorial/invisible-metaclasses-in-python.md)
- [Meta Classes without type](./tutorial/meta-classes-without-type.md)
- [More Accurate Meta Classes without type](./tutorial/more-accurate-meta-classes-without-type.md)

### Examples

- [Register Classes in Python](./tutorial/examples/register-classes-in-python.md)
- [Singleton in Python](./tutorial/examples/singleton-in-python.md)
- [Auto Slots ](./tutorial/examples/auto-slots.md)
- [Logging Namespace](./tutorial/examples/logging-namespace.md)
- [Modeling a Class with a Metaclass](./tutorial/examples/modeling-a-class-with-a-metaclass.md)
- [Define Method If Condition True](./tutorial/examples/define-method-if-condition-true.md)

Example on CPython

```shell
>>> import enum
>>> enum.Enum


>>> import abc
>>> abc.ABC


>>> import typing
>>> typing.Any
```

Example on 3.party libs

- https://github.com/django/django/blob/main/django/db/models/base.py#L92
- https://github.com/pydantic/pydantic/blob/main/pydantic/main.py#L47

## Tutorial, Docs, Videos

- https://www.youtube.com/watch?v=yWzMiaqnpkI
- https://realpython.com/python-metaclasses/
- https://www.python.org/doc/essays/metaclasses/
- https://docs.python.org/3/reference/datamodel.html#customizing-class-creation
- https://peps.python.org/pep-3115/
- https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
- https://jfreeman.dev/blog/2020/12/07/python-metaclasses/
- https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
- https://jfreeman.dev/blog/2020/12/07/python-metaclasses/
- https://peps.python.org/pep-3115/

## CPython Implementation

- https://github.com/python/cpython/blob/main/Python/bltinmodule.c#L89
