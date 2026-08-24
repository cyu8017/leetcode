# LeetCode 2727 - Is Object Empty
# https://leetcode.com/problems/is-object-empty/

from typing import Any, Dict, List, Union


class Solution:
    def isEmpty(self, obj: Union[Dict[Any, Any], List[Any]]) -> bool:
        if isinstance(obj, list):
            return len(obj) == 0
        return len(obj) == 0
