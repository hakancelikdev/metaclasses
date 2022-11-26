"""
class Example:
	attr = 1

	def method(self):
		return "method"
"""


name = "Example"
bases = ()
namespace = {
	"attr": 1,
	"method": lambda self: "method"
}

Example = type(name, bases, namespace)

print(f"{Example.__class__=}")     # <class 'type'>
print(f"{Example().attr=}")        # 1
print(f"{Example().method()=}")    # 'method'


"""# noqa
			type    ( instance of type )
			 |
			 |
		   Example  ( instance of type )
		     |
			 |
		  Example() ( instance of Example )
"""

assert isinstance(Example, type)
assert isinstance(Example(), Example)
