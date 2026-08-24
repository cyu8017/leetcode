# LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
# https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

from typing import List


class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        cnt = {0: 1}
        for x in nums:
            s = (s + x) % k
            ans += cnt.get(s, 0)
            cnt[s] = cnt.get(s, 0) + 1
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            m = j - i
            for h in range(1, m + 1):
                if (nums[i] * h) % k == 0:
                    ans -= m - h
            i = j
        return ans
