# LeetCode 2755 - Deep Merge of Two Objects
# https://leetcode.com/problems/deep-merge-of-two-objects/

from typing import Any


class Solution:
    def deepMerge(self, obj1: Any, obj2: Any) -> Any:
        def is_obj(x: Any) -> bool:
            return isinstance(x, dict)

        def is_arr(x: Any) -> bool:
            return isinstance(x, list)

        def merge(a: Any, b: Any) -> Any:
            if is_obj(a) and is_obj(b):
                res = dict(a)
                for k in b:
                    if k in res:
                        res[k] = merge(res[k], b[k])
                    else:
                        res[k] = b[k]
                return res
            if is_arr(a) and is_arr(b):
                n = max(len(a), len(b))
                res = [None] * n
                for i in range(n):
                    if i >= len(a):
                        res[i] = b[i]
                    elif i >= len(b):
                        res[i] = a[i]
                    else:
                        res[i] = merge(a[i], b[i])
                return res
            return b

        return merge(obj1, obj2)
