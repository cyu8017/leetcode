# LeetCode 3668 - Restore Finishing Order
# https://leetcode.com/problems/restore-finishing-order/

from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        n = len(order)
        d = [0] * (n + 1)
        for i, x in enumerate(order):
            d[x] = i
        friends.sort(key=lambda a: d[a])
        return friends
