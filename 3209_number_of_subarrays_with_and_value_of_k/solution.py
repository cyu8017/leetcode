# LeetCode 3209 - Number of Subarrays With AND Value of K
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

from typing import Dict, List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pre: Dict[int, int] = {}
        ans = 0
        for x in nums:
            cur: Dict[int, int] = {}
            for key, val in pre.items():
                nk = x & key
                cur[nk] = cur.get(nk, 0) + val
            cur[x] = cur.get(x, 0) + 1
            ans += cur.get(k, 0)
            pre = cur
        return ans
