# LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        def kadane(a: List[int]) -> int:
            best = -9007199254740991
            cur = 0
            for x in a:
                cur += x
                if cur > best:
                    best = cur
                if cur < 0:
                    cur = 0
            all_neg = True
            mx = a[0]
            for x in a:
                if x > mx:
                    mx = x
                if x >= 0:
                    all_neg = False
            if all_neg:
                return mx
            return best

        ans = kadane(nums)
        uniq = set()
        for x in nums:
            if x < 0:
                uniq.add(x)
        for v in uniq:
            b = [x for x in nums if x != v]
            if not b:
                continue
            cand = kadane(b)
            if cand > ans:
                ans = cand
        return ans
