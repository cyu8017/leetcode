# LeetCode 2628 - JSON Deep Equal
# https://leetcode.com/problems/json-deep-equal/

from typing import Any


class Solution:
    def areDeeplyEqual(self, o1: Any, o2: Any) -> bool:
        if o1 is o2:
            return True
        if type(o1) is not type(o2):
            return False
        if o1 is None or o2 is None:
            return False
        if not isinstance(o1, (list, dict)):
            return o1 == o2
        if isinstance(o1, list) != isinstance(o2, list):
            return False
        if isinstance(o1, list):
            if len(o1) != len(o2):
                return False
            for i in range(len(o1)):
                if not self.areDeeplyEqual(o1[i], o2[i]):
                    return False
            return True
        if len(o1) != len(o2):
            return False
        for k in o1:
            if k not in o2 or not self.areDeeplyEqual(o1[k], o2[k]):
                return False
        return True
