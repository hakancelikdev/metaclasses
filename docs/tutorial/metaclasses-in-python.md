![](../media/understanding-python-classes.png)

> Let's add an intermediate layer to the class creation phase.

```python
class Meta(type):
    pass


class Example(metaclass=Meta):
    attr = 1

    def method(self):
        return "method"


print(f"{Meta.__class__=}")       # <class 'type'>
print(f"{Example.__class__=}")    # <class '__main__.Meta'>
print(f"{Example().__class__=}")  # <class '__main__.Example'>


print(f"{Example().attr=}")        # 1
print(f"{Example().method()=}")    # 'method'


assert isinstance(Meta, type)
assert isinstance(Example, Meta)
assert isinstance(Example(), Example)
```
