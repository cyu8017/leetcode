# LeetCode 2601 - Prime Subtraction Operation
# https://leetcode.com/problems/prime-subtraction-operation/

from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_v = 0
        for x in nums:
            if x > max_v:
                max_v = x
        is_p = [True] * (max_v + 1)
        if max_v >= 0:
            is_p[0] = False
        if max_v >= 1:
            is_p[1] = False
        i = 2
        while i * i <= max_v:
            if is_p[i]:
                for j in range(i * i, max_v + 1, i):
                    is_p[j] = False
            i += 1
        primes = [i for i in range(2, max_v + 1) if is_p[i]]
        prev = 0
        for x in nums:
            need = x - prev
            best = -1
            for p in primes:
                if p >= need:
                    break
                best = p
            cur = x if best < 0 else x - best
            if cur <= prev:
                return False
            prev = cur
        return True
