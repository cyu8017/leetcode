# LeetCode 0862 - Shortest Subarray with Sum at Least K
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        dq: deque[int] = deque()
        ans = n + 1
        for i, p in enumerate(prefix):
            while dq and p - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            while dq and p <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        return ans if ans <= n else -1
