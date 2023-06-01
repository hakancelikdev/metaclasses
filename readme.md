## Metaclasses

- [Understanding Python Classes](./docs/understanding-python-classes.md)
- [Dynamic Class Creation](./docs/dynamic-class-creation.md)
- [More Accurate Dynamic Class Creation](./docs/more-accurate-dynamic-class-creation.md)
- [Metaclasses in Python](./docs/metaclasses-in-python.md)
- [Run Methods Order in Python](./docs/run-methods-order-in-python.md)
- [Run Methods Order in Python with More Explanation](./docs/run-methods-order-in-python-with-more-explanation.md)
- [Invisible Metaclasses in Python](./docs/invisible-metaclasses-in-python.md)
- [Meta Classes without type](./docs/meta-classes-without-type.md)
- [More Accurate Meta Classes without type](./docs/more-accurate-meta-classes-without-type.md)

### Examples

- [Register Classes in Python](./examples/register_classes_in_python.py)
- [Singleton in Python](./examples/singleton_in_python.py)
- [Auto Slots ](./examples/auto_slots.py)
- [Logging Namespace](./examples/logging_namespace.py)
- [Modeling a Class with a Metaclass](./examples/modeling_a_class_with_a_metaclass.py)
- [Define Method If Condition True](./examples/define_method_if_condition_true.py)

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
