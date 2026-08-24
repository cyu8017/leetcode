# LeetCode 2618 - Check if Object Instance of Class
# https://leetcode.com/problems/check-if-object-instance-of-class/

from typing import Any


class Solution:
    def checkIfInstanceOf(self, obj: Any, classFunction: Any) -> bool:
        if obj is None or not isinstance(classFunction, type):
            return False
        try:
            return isinstance(obj, classFunction)
        except TypeError:
            return False
