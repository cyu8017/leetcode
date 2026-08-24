# LeetCode 2705 - Compact Object
# https://leetcode.com/problems/compact-object/

from typing import Any


class Solution:
    def compactObject(self, obj: Any) -> Any:
        if isinstance(obj, list):
            out = []
            for x in obj:
                v = self.compactObject(x)
                if v:
                    out.append(v)
            return out
        if isinstance(obj, dict):
            out = {}
            for k, val in obj.items():
                v = self.compactObject(val)
                if v:
                    out[k] = v
            return out
        return obj
