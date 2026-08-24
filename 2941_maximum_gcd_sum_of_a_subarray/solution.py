# LeetCode 2941 - Maximum GCD-Sum of a Subarray
# https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 0
        st = []
        for i in range(n):
            nst = [[nums[i], i]]
            for p in st:
                g = gcd(p[0], nums[i])
                if nst[-1][0] == g:
                    if p[1] < nst[-1][1]:
                        nst[-1][1] = p[1]
                    continue
                nst.append([g, p[1]])
            st = nst
            for g, idx in st:
                if i - idx + 1 >= k:
                    cand = (pref[i + 1] - pref[idx]) * g
                    if cand > ans:
                        ans = cand
        return ans
