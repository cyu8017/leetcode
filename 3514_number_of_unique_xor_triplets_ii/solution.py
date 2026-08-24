# LeetCode 3514 - Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = 0
        for v in nums:
            mx = max(mx, v)
        mx <<= 1
        st = [False] * mx
        for a in nums:
            for b in nums:
                st[a ^ b] = True
        s = [0] * mx
        for ab in range(mx):
            if st[ab]:
                for c in nums:
                    s[ab ^ c] = 1
        ans = 0
        for v in s:
            ans += v
        return ans
