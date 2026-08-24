# LeetCode 3309 - Maximum Possible Number by Binary Concatenation
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

from typing import List


def toBin(x: int) -> str:
    if x == 0:
        return "0"
    s = ""
    while x > 0:
        s = str(x & 1) + s
        x >>= 1
    return s


def perm(i: int, idx: List[int], bs: List[str], ans: List[int]) -> None:
    if i == 3:
        s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
        v = 0
        for c in s:
            v = v * 2 + (ord(c) - 48)
        if v > ans[0]:
            ans[0] = v
        return
    for j in range(i, 3):
        idx[i], idx[j] = idx[j], idx[i]
        perm(i + 1, idx, bs, ans)
        idx[i], idx[j] = idx[j], idx[i]


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        bs = [toBin(nums[0]), toBin(nums[1]), toBin(nums[2])]
        idx = [0, 1, 2]
        ans = [0]
        perm(0, idx, bs, ans)
        return ans[0]
