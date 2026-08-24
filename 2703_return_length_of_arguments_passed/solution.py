# LeetCode 2703 - Return Length of Arguments Passed
# https://leetcode.com/problems/return-length-of-arguments-passed/

from typing import Any


class Solution:
    def argumentsLength(self, *args: Any) -> int:
        return len(args)
