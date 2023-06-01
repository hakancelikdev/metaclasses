```python
class K(metaclass=type):
    pass


class Example(K, metaclass=type):
    pass


class K:
    pass


class Example(K):
    pass
```
