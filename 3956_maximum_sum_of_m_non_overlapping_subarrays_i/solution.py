# LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dp = [0] * (n + 1)
        best_selected = -(2 ** 62)
        for count in range(1, m + 1):
            nxt = dp[:]
            deque = []
            for end in range(1, n + 1):
                add_index = end - l
                if add_index >= 0:
                    value = dp[add_index] - prefix[add_index]
                    while deque:
                        last = deque[-1]
                        if dp[last] - prefix[last] > value:
                            break
                        deque.pop()
                    deque.append(add_index)
                min_index = end - r
                while deque and deque[0] < min_index:
                    deque.pop(0)
                if deque:
                    candidate = prefix[end] + dp[deque[0]] - prefix[deque[0]]
                    if candidate > nxt[end]:
                        nxt[end] = candidate
                    if candidate > best_selected:
                        best_selected = candidate
                if nxt[end - 1] > nxt[end]:
                    nxt[end] = nxt[end - 1]
            dp = nxt
        return best_selected
