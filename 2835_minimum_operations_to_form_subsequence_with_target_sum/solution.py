# LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
# https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        cnt = [0] * 32
        total = 0
        for v in nums:
            total += v
            b = 0
            while (1 << b) < v:
                b += 1
            cnt[b] += 1
        if total < target:
            return -1
        ans = 0
        for i in range(31):
            if target & (1 << i):
                if cnt[i] > 0:
                    cnt[i] -= 1
                else:
                    j = i + 1
                    while j < 32 and cnt[j] == 0:
                        j += 1
                    if j == 32:
                        return -1
                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ans += 1
                        j -= 1
                    cnt[i] -= 1
            cnt[i + 1] += cnt[i] // 2
        return ans
