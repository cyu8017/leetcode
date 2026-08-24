# LeetCode 2879 - Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows/

from typing import Any, List


class Solution:
    def selectFirstRows(self, employees: List[Any]) -> List[Any]:
        return employees[:3]
