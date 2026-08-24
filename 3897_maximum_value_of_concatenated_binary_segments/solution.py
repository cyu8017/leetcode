# LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
# https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

from typing import List

MOD3897 = 1000000007


def group3897(p: List[int]) -> int:
    if p[1] == 0:
        return 0
    if p[0] > 0:
        return 1
    return 2


class Solution:
    def maxValue(self, nums1: List[int], nums0: List[int]) -> int:
        n = len(nums1)
        pairs = [[nums1[i], nums0[i]] for i in range(n)]
        b = 0
        for i in range(n):
            b += nums1[i] + nums0[i]
        pairs.sort(key=lambda a: (
            group3897(a),
            -a[0] if group3897(a) == 0 else (-a[0] if group3897(a) == 1 else a[1]),
            a[1] if group3897(a) == 1 else 0,
        ))
        p = [0] * b
        p[0] = 1
        for i in range(1, b):
            p[i] = (2 * p[i - 1]) % MOD3897
        ans = 0
        b -= 1
        for pr in pairs:
            cnt1, cnt0 = pr[0], pr[1]
            while cnt1 > 0:
                ans = (ans + p[b]) % MOD3897
                b -= 1
                cnt1 -= 1
            b -= cnt0
        return ans
