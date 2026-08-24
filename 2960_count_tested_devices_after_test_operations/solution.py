# LeetCode 2960 - Count Tested Devices After Test Operations
# https://leetcode.com/problems/count-tested-devices-after-test-operations/

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for b in batteryPercentages:
            if b > ans:
                ans += 1
        return ans
