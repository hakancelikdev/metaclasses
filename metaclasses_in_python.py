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


"""# noqa
            type   ( instance of type )
             |
             |
			Meta    ( instance of type )
			 |
			 |
		   Example  ( instance of Meta )
		     |
			 |
		  Example() ( instance of Example )
"""

assert isinstance(Meta, type)
assert isinstance(Example, Meta)
assert isinstance(Example(), Example)
