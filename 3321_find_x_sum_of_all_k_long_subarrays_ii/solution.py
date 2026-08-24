# LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            freq = {}
            for j in range(i, i + k):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
            arr = [[key, val] for key, val in freq.items()]
            arr.sort(key=lambda A: (-A[1], -A[0]))
            lim = min(x, len(arr))
            keep = set(arr[t][0] for t in range(lim))
            s = 0
            for j in range(i, i + k):
                if nums[j] in keep:
                    s += nums[j]
            ans[i] = s
        return ans
