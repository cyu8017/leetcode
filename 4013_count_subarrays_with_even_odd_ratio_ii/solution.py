# LeetCode 4013 - Count Subarrays With Even Odd Ratio II
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

from typing import List


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def lowerBound(self, a: List[int], x: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            if nums[i] % 2 == 1:
                s[i + 1] = s[i] + a
            else:
                s[i + 1] = s[i] - b
        st = s[:]
        st.sort()
        uniq = 0
        for i in range(len(st)):
            if uniq == 0 or st[i] != st[uniq - 1]:
                st[uniq] = st[i]
                uniq += 1
        st = st[:uniq]
        bit = BIT(len(st) + 1)
        ans = 0
        for v in s:
            x = self.lowerBound(st, v) + 1
            ans += bit.query(x)
            bit.update(x, 1)
        return ans
