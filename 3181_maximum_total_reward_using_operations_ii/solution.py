# LeetCode 3181 - Maximum Total Reward Using Operations II
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        uniq = 0
        for i in range(len(rewardValues)):
            if uniq == 0 or rewardValues[i] != rewardValues[uniq - 1]:
                rewardValues[uniq] = rewardValues[i]
                uniq += 1
        f = 1
        for i in range(uniq):
            v = rewardValues[i]
            mask = f & ((1 << v) - 1)
            f = f | (mask << v)
        for i in range(100000, -1, -1):
            if (f >> i) & 1:
                return i
        return 0
