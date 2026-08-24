# LeetCode 2798 - Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for h in hours:
            if h >= target:
                ans += 1
        return ans
