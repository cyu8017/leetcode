# LeetCode 3574 - Maximize Subarray GCD Score
# https://leetcode.com/problems/maximize-subarray-gcd-score/

from typing import List


def gcd3574(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * n
        for i in range(n):
            x = nums[i]
            while x % 2 == 0:
                cnt[i] += 1
                x //= 2
        ans = 0
        for l in range(n):
            g = 0
            mi = 2147483647
            t = 0
            for r in range(l, n):
                g = gcd3574(g, nums[r])
                if cnt[r] < mi:
                    mi = cnt[r]
                    t = 1
                elif cnt[r] == mi:
                    t += 1
                score = g * (r - l + 1)
                if t <= k:
                    score *= 2
                ans = max(ans, score)
        return ans
