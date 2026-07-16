# LeetCode 0313 - Super Ugly Number
# https://leetcode.com/problems/super-ugly-number/

from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next_values = [ugly[pointers[index]] * primes[index] for index in range(len(primes))]
            next_ugly = min(next_values)
            ugly.append(next_ugly)
            for index in range(len(primes)):
                if next_ugly == ugly[pointers[index]] * primes[index]:
                    pointers[index] += 1
        return ugly[-1]
