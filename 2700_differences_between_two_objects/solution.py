# LeetCode 2700 - Differences Between Two Objects
# https://leetcode.com/problems/differences-between-two-objects/

from typing import Any, Dict


class Solution:
    def objDiff(self, obj1: Any, obj2: Any) -> Any:
        diff = {}
        if isinstance(obj1, dict):
            keys = obj1.keys()
        else:
            keys = range(len(obj1)) if isinstance(obj1, list) else []
        for k in keys:
            if isinstance(obj1, dict):
                if k not in obj2:
                    continue
                v1, v2 = obj1[k], obj2[k]
            else:
                if not isinstance(obj2, list) or k >= len(obj2):
                    continue
                v1, v2 = obj1[k], obj2[k]
            if isinstance(v1, dict) and isinstance(v2, dict):
                child = self.objDiff(v1, v2)
                if child:
                    diff[k] = child
            elif isinstance(v1, list) and isinstance(v2, list):
                child = self.objDiff(v1, v2)
                if child:
                    diff[k] = child
            elif v1 != v2:
                diff[k] = [v1, v2]
        return diff
