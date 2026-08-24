# LeetCode 2692 - Make Object Immutable
# https://leetcode.com/problems/make-object-immutable/

from typing import Any


class _ImmutableList(list):
    _MUTATORS = {"pop", "append", "extend", "insert", "remove", "clear", "sort", "reverse"}

    def __setitem__(self, index: Any, value: Any) -> None:
        raise Exception(f"Error Modifying Index: {index}")

    def __delitem__(self, index: Any) -> None:
        raise Exception(f"Error Modifying Index: {index}")

    def __getattribute__(self, prop: str) -> Any:
        if prop in _ImmutableList._MUTATORS:
            def banned(*args: Any, **kwargs: Any) -> Any:
                raise Exception(f"Error Calling Method: {prop}")
            return banned
        return object.__getattribute__(self, prop)


class _ImmutableDict(dict):
    def __setitem__(self, key: Any, value: Any) -> None:
        raise Exception(f"Error Modifying: {key}")

    def __delitem__(self, key: Any) -> None:
        raise Exception(f"Error Modifying: {key}")


class Solution:
    def makeImmutable(self, obj: Any) -> Any:
        def wrap(val: Any) -> Any:
            if val is None or not isinstance(val, (dict, list)):
                return val
            if isinstance(val, list):
                return _ImmutableList(wrap(x) for x in val)
            return _ImmutableDict((k, wrap(v)) for k, v in val.items())

        return wrap(obj)
