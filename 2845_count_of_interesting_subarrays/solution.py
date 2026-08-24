# LeetCode 2845 - Count of Interesting Subarrays
# https://leetcode.com/problems/count-of-interesting-subarrays/

from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = {0: 1}
        ans = 0
        pref = 0
        for v in nums:
            if v % modulo == k:
                pref += 1
            need = (pref - k) % modulo
            if need < 0:
                need += modulo
            ans += freq.get(need, 0)
            key = pref % modulo
            freq[key] = freq.get(key, 0) + 1
        return ans
