# LeetCode 2031 - Count Subarrays With More Ones Than Zeros
# https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

from typing import List


class Fenwick:
    def __init__(self, n: int):
        self.bit = [0] * (n + 2)

    def add(self, i: int, v: int) -> None:
        while i < len(self.bit):
            self.bit[i] += v
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        offset = n + 1
        fw = Fenwick(2 * n + 5)
        pref = 0
        ans = 0
        fw.add(offset, 1)
        for x in nums:
            pref += 1 if x == 1 else -1
            idx = pref + offset
            ans = (ans + fw.sum(idx - 1)) % MOD
            fw.add(idx, 1)
        return ans
