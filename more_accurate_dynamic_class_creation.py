import textwrap

"""
class Example:
	attr = 1

	def method(self):
		return "method"
"""


name = "Example"
bases = ()
namespace = type.__prepare__(name, bases)  # >>> {}, default is dict()
# namespace["attr"] = 1
# namespace["method"] = lambda self: "method"

body = textwrap.dedent(
	"""\
	attr = 1
	
	def method(self):
		return "method"
	"""
)

exec(body, globals(), namespace)
Example = type(name, bases, namespace)  # type: ignore

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
