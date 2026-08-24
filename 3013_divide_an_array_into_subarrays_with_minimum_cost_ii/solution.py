# LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

from typing import List


class BITI:
    def __init__(self, n_: int):
        self.n = n_
        self.c = [0] * (n_ + 1)

    def upd(self, x: int, d: int) -> None:
        while x <= self.n:
            self.c[x] += d
            x += x & -x

    def qry(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class BITL:
    def __init__(self, n_: int):
        self.n = n_
        self.c = [0] * (n_ + 1)

    def upd(self, x: int, d: int) -> None:
        while x <= self.n:
            self.c[x] += d
            x += x & -x

    def qry(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


def kth(cnt: BITI, m: int, k: int) -> int:
    idx = 0
    bit = 1 << 20
    while bit != 0:
        nidx = idx + bit
        if nidx <= m and cnt.c[nidx] < k:
            k -= cnt.c[nidx]
            idx = nidx
        bit >>= 1
    return idx + 1


def sumSmallest(cnt: BITI, sbit: BITL, uniq: List[int], m: int, kk: int) -> int:
    if kk <= 0:
        return 0
    r = kth(cnt, m, kk)
    before = cnt.qry(r - 1)
    s = sbit.qry(r - 1)
    s += (kk - before) * uniq[r - 1]
    return s


def lowerBound(arr: List[int], x: int) -> int:
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) >> 1
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        n = len(nums)
        uniq = sorted(nums[:])
        write = 0
        for i in range(len(uniq)):
            if write == 0 or uniq[i] != uniq[write - 1]:
                uniq[write] = uniq[i]
                write += 1
        uniq = uniq[:write]
        m = len(uniq)
        cnt = BITI(m + 2)
        sbit = BITL(m + 2)
        for i in range(1, min(dist + 1, n - 1) + 1):
            r = lowerBound(uniq, nums[i]) + 1
            cnt.upd(r, 1)
            sbit.upd(r, nums[i])
        end = min(dist + 1, n - 1)
        kk = min(k, end)
        ans = nums[0] + sumSmallest(cnt, sbit, uniq, m, kk)
        for i in range(dist + 2, n):
            rem = nums[i - dist - 1]
            r1 = lowerBound(uniq, rem) + 1
            cnt.upd(r1, -1)
            sbit.upd(r1, -rem)
            add = nums[i]
            r2 = lowerBound(uniq, add) + 1
            cnt.upd(r2, 1)
            sbit.upd(r2, add)
            kk = min(k, dist + 1)
            ans = min(ans, nums[0] + sumSmallest(cnt, sbit, uniq, m, kk))
        return ans
