# LeetCode 2195 - Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

from typing import List
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ans = 0
        prev = 0
        for x in nums:
            if x <= prev:
                continue
            start = prev + 1
            end = x - 1
            if start <= end:
                cnt = end - start + 1
                if cnt > k:
                    end = start + k - 1
                    cnt = k
                ans += (start + end) * cnt / 2
                k -= cnt
                if k == 0:
                    return ans
            prev = x
        s = prev + 1
        e = s + k - 1
        ans += (s + e) * k / 2
        return ans
