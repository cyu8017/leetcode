# LeetCode 2704 - To Be Or Not To Be
# https://leetcode.com/problems/to-be-or-not-to-be/

from typing import Any, Callable, Dict


class Solution:
    def expect(self, val: Any) -> Dict[str, Callable[[Any], bool]]:
        def toBe(other: Any) -> bool:
            if val == other:
                return True
            raise Exception("Not Equal")

        def notToBe(other: Any) -> bool:
            if val != other:
                return True
            raise Exception("Equal")

        return {"toBe": toBe, "notToBe": notToBe}
