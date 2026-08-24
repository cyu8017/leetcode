# LeetCode 3953 - Maximum Score with Co-Prime Element
# https://leetcode.com/problems/maximum-score-with-co-prime-element/

from typing import List


class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        limit = maxVal
        frequency = [0] * 100001
        for x in nums:
            frequency[x] += 1
            if x > limit:
                limit = x
        divisible = [0] * (limit + 1)
        for d in range(1, limit + 1):
            multiple = d
            while multiple <= limit:
                if multiple < len(frequency):
                    divisible[d] += frequency[multiple]
                multiple += d
        best = -len(nums)
        checked = [False] * (limit + 1)
        for x in range(1, maxVal + 1):
            best = max(best, self.evaluate(x, x < len(frequency) and frequency[x] > 0, checked, divisible))
        for x in nums:
            best = max(best, self.evaluate(x, True, checked, divisible))
        return best

    def evaluate(self, x: int, exists: bool, checked: List[bool], divisible: List[int]) -> int:
        if checked[x]:
            return -2147483648 // 4
        checked[x] = True
        bad = self.badCount(x, divisible)
        if exists:
            cost = bad - 1 if x > 1 else 0
        else:
            cost = bad if bad > 0 else 1
        return x - cost

    def badCount(self, x: int, divisible: List[int]) -> int:
        primes = []
        y = x
        p = 2
        while p * p <= y:
            if y % p == 0:
                primes.append(p)
                while y % p == 0:
                    y //= p
            p += 1
        if y > 1:
            primes.append(y)
        bad = 0
        psz = len(primes)
        for mask in range(1, 1 << psz):
            product = 1
            bits = 0
            for i in range(psz):
                if ((mask >> i) & 1) != 0:
                    product *= primes[i]
                    bits += 1
            if bits % 2 == 1:
                bad += divisible[product]
            else:
                bad -= divisible[product]
        return bad
