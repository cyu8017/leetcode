# LeetCode 3164 - Find the Number of Good Pairs II
# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt1 = {}
        for x in nums1:
            if x % k == 0:
                cnt1[x // k] = cnt1.get(x // k, 0) + 1
        if not cnt1:
            return 0
        cnt2 = {}
        for x in nums2:
            cnt2[x] = cnt2.get(x, 0) + 1
        mx = 0
        for x in cnt1:
            mx = max(mx, x)
        ans = 0
        for x, v in cnt2.items():
            s = 0
            y = x
            while y <= mx:
                c = cnt1.get(y)
                if c is not None:
                    s += c
                y += x
            ans += s * v
        return ans
