# LeetCode 2967 - Minimum Cost to Make Array Equalindromic
# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

from typing import List


def makePal(x: int) -> int:
    ch = list(str(x))
    i, j = 0, len(ch) - 1
    while i < j:
        ch[j] = ch[i]
        i += 1
        j -= 1
    return int("".join(ch))


def costOf(nums: List[int], p: int) -> int:
    c = 0
    for v in nums:
        c += abs(v - p)
    return c


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        candidates = [makePal(median)]
        s = str(median)
        half = int(s[: (len(s) + 1) // 2])
        for d in range(-2, 3):
            h = half + d
            if h <= 0:
                continue
            hs = str(h)
            if len(s) % 2 == 0:
                pal = hs + hs[::-1]
            else:
                prefix = hs[:-1]
                pal = hs + prefix[::-1]
            try:
                parsed = int(pal)
                candidates.append(parsed)
            except ValueError:
                pass
        for v in [1, 9, 11, 99, 101]:
            candidates.append(v)
        ans = (1 << 53) // 4
        for p in candidates:
            if p <= 0:
                continue
            ans = min(ans, costOf(nums, p))
        return ans
