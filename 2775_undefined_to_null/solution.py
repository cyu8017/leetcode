# LeetCode 2775 - Undefined to Null
# https://leetcode.com/problems/undefined-to-null/

from typing import Any


UNDEFINED = object()


class Solution:
    def undefinedToNull(self, obj: Any) -> Any:
        if isinstance(obj, str) and obj.lstrip()[:1] in "{[":
            import json
            import re

            obj = json.loads(re.sub(r"\bundefined\b", "null", obj))
        if obj is UNDEFINED:
            return None
        if obj is None or not isinstance(obj, (dict, list)):
            return obj
        if isinstance(obj, list):
            for i in range(len(obj)):
                obj[i] = self.undefinedToNull(obj[i])
            return obj
        for k in list(obj.keys()):
            obj[k] = self.undefinedToNull(obj[k])
        return obj
