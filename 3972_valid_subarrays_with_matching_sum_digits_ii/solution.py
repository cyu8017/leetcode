# LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

from typing import List


class Solution:
    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        by_remainder = [[] for _ in range(10)]
        by_remainder[0].append(0)
        prefix = 0
        answer = 0
        for value in nums:
            prefix += value
            required = ((prefix - x) % 10 + 10) % 10
            values = by_remainder[required]
            power = 1
            while x * power <= prefix:
                low = x * power
                high = (x + 1) * power - 1
                min_prefix = prefix - high
                max_prefix = prefix - low
                left = self.lowerBound(values, min_prefix)
                right = self.upperBound(values, max_prefix)
                answer += right - left
                if power > prefix // 10:
                    break
                power *= 10
            by_remainder[prefix % 10].append(prefix)
        return answer

    def lowerBound(self, a: List[int], x: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upperBound(self, a: List[int], x: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo
