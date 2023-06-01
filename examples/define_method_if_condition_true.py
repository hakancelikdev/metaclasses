import inspect
import typing

__all__ = ("DefineMeta", "Namespace")


FuncT = typing.Callable[[typing.Any], typing.Any]  # unexport: not-public


class NotSet:  # unexport: not-public
    ...


class Namespace(dict):
    test: typing.List[bool] = []  # TODO: rename

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__setitem__("define_if", self.define_if)

    def __setitem__(self, key: str, value: typing.Any):
        if inspect.isfunction(value):
            if self.test:
                if self.test.pop() is True:
                    super().__setitem__(key, value)
            else:
                super().__setitem__(key, value)
        else:
            super().__setitem__(key, value)

    @classmethod
    def define_if(cls, condition: bool) -> typing.Callable[[typing.Callable], FuncT]:
        def wrapper(func: FuncT) -> FuncT:
            cls.test.append(condition)
            return func

        return wrapper


class DefineMeta(type):
    if typing.TYPE_CHECKING:

        @classmethod
        def define_if(mcs, condition: bool) -> typing.Callable[[typing.Callable], FuncT]:
            ...

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs) -> typing.Union["Namespace", dict]:  # type: ignore[override]  # noqa: E501
        return Namespace()

    def __call__(cls, condition: typing.Union[bool, typing.Type[NotSet], None] = NotSet):
        if condition is NotSet:
            return super().__call__()
        else:
            assert isinstance(condition, bool)
            return cls.define_if(condition)


class Defineif(metaclass=DefineMeta):
    pass


define_if = Defineif


class Example(metaclass=DefineMeta):
    @define_if(condition=True)
    def foo(self):
        return True

    @define_if(condition=False)
    def foo(self):
        return False


assert Example().foo() is True
