# LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
# https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

from typing import List


class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        arr = sorted(nums, reverse=True)
        s = sum(arr[:k])
        if s % 2 == 0:
            return s
        ans = -1
        odd_in = even_in = odd_out = even_out = -1
        for i in range(k - 1, -1, -1):
            if arr[i] % 2 != 0 and odd_in == -1:
                odd_in = i
            if arr[i] % 2 == 0 and even_in == -1:
                even_in = i
        for i in range(k, len(arr)):
            if arr[i] % 2 != 0 and odd_out == -1:
                odd_out = i
            if arr[i] % 2 == 0 and even_out == -1:
                even_out = i
        if odd_in != -1 and even_out != -1:
            ans = max(ans, s - arr[odd_in] + arr[even_out])
        if even_in != -1 and odd_out != -1:
            ans = max(ans, s - arr[even_in] + arr[odd_out])
        return ans
