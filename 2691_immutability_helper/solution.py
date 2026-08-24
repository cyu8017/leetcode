# LeetCode 2691 - Immutability Helper
# https://leetcode.com/problems/immutability-helper/

from typing import Any, Callable, Dict, List, Union


class ImmutableHelper:
    def __init__(self, obj: Any):
        self.obj = obj

    def produce(self, mutator: Callable[[Any], None]) -> Any:
        clones = {}

        def is_obj(v: Any) -> bool:
            return isinstance(v, (dict, list))

        def get_clone(original: Any) -> Any:
            oid = id(original)
            if oid in clones:
                return clones[oid]
            if isinstance(original, list):
                copy = original[:]
            else:
                copy = dict(original)
            clones[oid] = copy
            return copy

        class _Proxy:
            def __init__(self, node: Any, on_replace: Callable[[Any], None]):
                object.__setattr__(self, "_node", node)
                object.__setattr__(self, "_on_replace", on_replace)

            def __getitem__(self, prop: Any) -> Any:
                node = object.__getattribute__(self, "_node")
                on_replace = object.__getattribute__(self, "_on_replace")
                val = node[prop]
                if is_obj(val):
                    def child_replace(child_clone: Any, _prop=prop, _node=node, _on=on_replace) -> None:
                        clone = get_clone(_node)
                        clone[_prop] = child_clone
                        _on(clone)
                    return _Proxy(val, child_replace)
                return val

            def __setitem__(self, prop: Any, value: Any) -> None:
                node = object.__getattribute__(self, "_node")
                on_replace = object.__getattribute__(self, "_on_replace")
                clone = get_clone(node)
                clone[prop] = value
                on_replace(clone)

            def __delitem__(self, prop: Any) -> None:
                node = object.__getattribute__(self, "_node")
                on_replace = object.__getattribute__(self, "_on_replace")
                clone = get_clone(node)
                del clone[prop]
                on_replace(clone)

            def __getattr__(self, prop: str) -> Any:
                node = object.__getattribute__(self, "_node")
                if isinstance(node, dict) and prop in node:
                    return self[prop]
                raise AttributeError(prop)

            def __setattr__(self, prop: str, value: Any) -> None:
                if prop.startswith("_"):
                    object.__setattr__(self, prop, value)
                    return
                self[prop] = value

        root_result = [self.obj]

        def on_root(clone: Any) -> None:
            root_result[0] = clone

        mutator(_Proxy(self.obj, on_root))
        return root_result[0]


class Solution:
    def ImmutableHelper(self, obj: Any, mutators: Any = None) -> ImmutableHelper:
        return ImmutableHelper(obj)
