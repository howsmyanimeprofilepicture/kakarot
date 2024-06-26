from typing import overload, TypeVar, Callable, Iterable
import functools

T = TypeVar("T")


@overload
def reduce(function: Callable[[T, T], T]) -> Callable[[Iterable[T]], T]:
    """
    ```python
    >>> import subete_ga_F_ni_naru as F
    >>> F.reduce(lambda x, y: x + y, [1, 0.1, 0.01])
    1.11
    >>> F.reduce(lambda x, y: x + y)([1, 0.1, 0.01])
    1.11
    ```
    """


@overload
def reduce(function: Callable[[T, T], T], sequence: Iterable[T]) -> T: ...


def reduce(function, sequence=None):
    if sequence is None:
        return functools.partial(functools.reduce, function)
    return functools.reduce(function, sequence)
