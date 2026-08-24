# LeetCode 2488 - Count Subarrays With Median K
# https://leetcode.com/problems/count-subarrays-with-median-k/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = 0
        for i in range(len(nums)):
            if nums[i] == k:
                pos = i
                break
        bal = {0: 1}
        cur = 0
        for i in range(pos - 1, -1, -1):
            cur += -1 if nums[i] < k else 1
            bal[cur] = bal.get(cur, 0) + 1
        ans = bal.get(0, 0) + bal.get(1, 0)
        cur = 0
        for i in range(pos + 1, len(nums)):
            cur += -1 if nums[i] < k else 1
            ans += bal.get(-cur, 0) + bal.get(1 - cur, 0)
        return ans
