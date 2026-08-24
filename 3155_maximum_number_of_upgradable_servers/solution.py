# LeetCode 3155 - Maximum Number of Upgradable Servers
# https://leetcode.com/problems/maximum-number-of-upgradable-servers/

from typing import List


class Solution:
    def maxUpgrades(
        self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]
    ) -> List[int]:
        ans = [0] * len(count)
        for i in range(len(count)):
            cnt = count[i]
            ans[i] = min(cnt, (cnt * sell[i] + money[i]) // (upgrade[i] + sell[i]))
        return ans
