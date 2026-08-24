# LeetCode 2100 - Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        return [i for i in range(time, n - time) if left[i] >= time and right[i] >= time]
