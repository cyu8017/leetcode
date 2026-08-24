# LeetCode 2354 - Number of Excellent Pairs
# https://leetcode.com/problems/number-of-excellent-pairs/

from typing import List


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        uniq = set(nums)
        cnt = [0] * 32

        def bit_count(x: int) -> int:
            c = 0
            while x:
                x &= x - 1
                c += 1
            return c

        for x in uniq:
            cnt[bit_count(x)] += 1
        ans = 0
        for i in range(32):
            for j in range(32):
                if i + j >= k:
                    ans += cnt[i] * cnt[j]
        return ans
