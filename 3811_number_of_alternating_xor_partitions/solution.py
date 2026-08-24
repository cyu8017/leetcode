# LeetCode 3811 - Number of Alternating XOR Partitions
# https://leetcode.com/problems/number-of-alternating-xor-partitions/

from typing import List


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        MOD = 1000000007
        cnt1 = {}
        cnt2 = {0: 1}
        pre = 0
        ans = 0
        for x in nums:
            pre ^= x
            a = cnt2.get(pre ^ target1, 0)
            b = cnt1.get(pre ^ target2, 0)
            ans = (a + b) % MOD
            cnt1[pre] = (cnt1.get(pre, 0) + a) % MOD
            cnt2[pre] = (cnt2.get(pre, 0) + b) % MOD
        return ans
