# LeetCode 2823 - Deep Object Filter
# https://leetcode.com/problems/deep-object-filter/

from typing import Any, Callable, Optional


class Solution:
    def deepFilter(self, obj: Any, fn: Callable) -> Optional[Any]:
        if not isinstance(obj, (dict, list)) or obj is None:
            return obj if fn(obj) else None
        if isinstance(obj, list):
            res = []
            for v in obj:
                f = self.deepFilter(v, fn)
                if f is not None:
                    res.append(f)
            return res if res else None
        res = {}
        for k in obj:
            f = self.deepFilter(obj[k], fn)
            if f is not None:
                res[k] = f
        return res if res else None
