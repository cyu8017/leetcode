# LeetCode 3901 - Good Subsequence Queries
# https://leetcode.com/problems/good-subsequence-queries/

from typing import List


def gcd3901(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


class SegmentTree3901:
    def __init__(self, n: int):
        self.tr = [{"l": 0, "r": 0, "g": 0} for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u: int, l: int, r: int) -> None:
        self.tr[u]["l"] = l
        self.tr[u]["r"] = r
        self.tr[u]["g"] = 0
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def pushup(self, u: int) -> None:
        self.tr[u]["g"] = gcd3901(self.tr[u << 1]["g"], self.tr[u << 1 | 1]["g"])

    def modify(self, u: int, x: int, v: int) -> None:
        if self.tr[u]["l"] == self.tr[u]["r"]:
            self.tr[u]["g"] = v
            return
        mid = (self.tr[u]["l"] + self.tr[u]["r"]) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def query(self, u: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if self.tr[u]["l"] >= l and self.tr[u]["r"] <= r:
            return self.tr[u]["g"]
        mid = (self.tr[u]["l"] + self.tr[u]["r"]) >> 1
        if r <= mid:
            return self.query(u << 1, l, r)
        if l > mid:
            return self.query(u << 1 | 1, l, r)
        return gcd3901(self.query(u << 1, l, mid), self.query(u << 1 | 1, mid + 1, r))


class Solution:
    def countGoodSubseq(self, nums: List[int], p: int, queries: List[List[int]]) -> int:
        n = len(nums)
        tree = SegmentTree3901(n)
        cnt = 0
        for i in range(n):
            if nums[i] % p == 0:
                tree.modify(1, i + 1, nums[i])
                cnt += 1
        ans = 0
        for q in queries:
            idx, val = q[0], q[1]
            if nums[idx] % p == 0:
                tree.modify(1, idx + 1, 0)
                cnt -= 1
            if val % p == 0:
                tree.modify(1, idx + 1, val)
                cnt += 1
            nums[idx] = val
            if tree.tr[1]["g"] != p:
                continue
            if cnt < n or n > 6:
                ans += 1
                continue
            for i in range(1, n + 1):
                left_g = tree.query(1, 1, i - 1)
                right_g = tree.query(1, i + 1, n)
                if gcd3901(left_g, right_g) == p:
                    ans += 1
                    break
        return ans
