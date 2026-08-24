# LeetCode 2822 - Inversion of Object
# https://leetcode.com/problems/inversion-of-object/

from typing import Any, Dict


class Solution:
    def invertObject(self, obj: Any) -> Dict[Any, Any]:
        inverted = {}
        keys = obj.keys() if isinstance(obj, dict) else range(len(obj))
        for key in keys:
            val = obj[key]
            key_s = str(key)
            if val in inverted:
                if not isinstance(inverted[val], list):
                    inverted[val] = [inverted[val]]
                inverted[val].append(key_s)
            else:
                inverted[val] = key_s
        return inverted
