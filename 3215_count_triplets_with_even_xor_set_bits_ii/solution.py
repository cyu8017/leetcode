# LeetCode 3215 - Count Triplets with Even XOR Set Bits II
# https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

from typing import List


class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def bitCount(x: int) -> int:
            n = 0
            while x:
                n += x & 1
                x >>= 1
            return n

        cnt1, cnt2, cnt3 = [0, 0], [0, 0], [0, 0]
        for x in a:
            cnt1[bitCount(x) % 2] += 1
        for x in b:
            cnt2[bitCount(x) % 2] += 1
        for x in c:
            cnt3[bitCount(x) % 2] += 1
        ans = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if (i + j + k) % 2 == 0:
                        ans += cnt1[i] * cnt2[j] * cnt3[k]
        return ans
