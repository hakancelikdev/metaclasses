## Metaclasses

- [Understanding Python Classes](./understanding_python_classes.py)
- [Dynamic Class Creation](./dynamic_class_creation.py)
- [More Accurate Dynamic Class Creation](./more_accurate_dynamic_class_creation.py)
- [Metaclasses in Python](./metaclasses_in_python.py)
- [Run Methods Order in Python](./run_methods_order_in_python.py)
- [Run Methods Order in Python with More Explanation](./run_methods_order_in_python_with_more_explanation.py)
- [Invisible Metaclasses in Python](./invisible_metaclasses_in_python.py)
- [Meta Classes without type](./meta_classes_without_type.py)

### Examples
- [Register Classes in Python](./register_classes_in_python.py)
- [Singleton in Python](./singleton_in_python.py)
- [Auto Slots ](./auto_slots.py)
- [Logging Namespace](./logging_namespace.py)
- [Modeling a Class with a Metaclass](./modeling_a_class_with_a_metaclass.py)
- [Define Method If Condition True](./define_method_if_condition_true.py)



Example on CPython

```python
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
