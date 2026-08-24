# LeetCode 2794 - Create Object from Two Arrays
# https://leetcode.com/problems/create-object-from-two-arrays/

from typing import Any, Dict, List


class Solution:
    def createObject(self, keysArr: List[Any], valuesArr: List[Any]) -> Dict[Any, Any]:
        output = {}
        n = min(len(keysArr), len(valuesArr))
        for i in range(n):
            key = keysArr[i]
            if isinstance(key, bool):
                key = "true" if key else "false"
            else:
                key = str(key)
            if key not in output:
                output[key] = valuesArr[i]
        return output
