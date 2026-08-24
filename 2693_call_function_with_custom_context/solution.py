# LeetCode 2693 - Call Function with Custom Context
# https://leetcode.com/problems/call-function-with-custom-context/

from typing import Any, Callable


class Solution:
    def callPolyfill(self, fn: Callable, obj: Any, *args: Any) -> Any:
        key = object()
        if isinstance(obj, dict):
            obj[key] = fn
            res = obj[key](*args)
            del obj[key]
            return res
        setattr(obj, "_call_polyfill_fn", fn)
        res = getattr(obj, "_call_polyfill_fn")(*args)
        delattr(obj, "_call_polyfill_fn")
        return res
