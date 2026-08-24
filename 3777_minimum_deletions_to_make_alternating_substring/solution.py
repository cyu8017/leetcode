# LeetCode 3777 - Minimum Deletions to Make Alternating Substring
# https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

from typing import List


class BIT:
    def __init__(self, n_: int):
        self.n = n_
        self.c = [0] * (n_ + 1)

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
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        nums = [0] * n
        bit = BIT(n)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                nums[i] = 1
                bit.update(i + 1, 1)
        ans = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                delta = (nums[j] ^ 1) - nums[j]
                nums[j] ^= 1
                bit.update(j + 1, delta)
                if j + 1 < n:
                    delta = (nums[j + 1] ^ 1) - nums[j + 1]
                    nums[j + 1] ^= 1
                    bit.update(j + 2, delta)
            else:
                l, r = q[1], q[2]
                ans.append(bit.query(r + 1) - bit.query(l + 1))
        return ans
