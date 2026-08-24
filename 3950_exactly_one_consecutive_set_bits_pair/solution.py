# LeetCode 3950 - Exactly One Consecutive Set Bits Pair
# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        vis = False
        pre = 0
        while n > 0:
            cur = n & 1
            if pre == cur and cur == 1:
                if vis:
                    return False
                vis = True
            pre = cur
            n >>= 1
        return vis
