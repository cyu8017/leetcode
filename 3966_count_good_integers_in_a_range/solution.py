# LeetCode 3966 - Count Good Integers in a Range
# https://leetcode.com/problems/count-good-integers-in-a-range/


class Solution:
    def countGoodIntegers(self, l: int, r: int, k: int) -> int:
        return self.count(r, k) - self.count(l - 1, k)

    def count(self, bound: int, k: int) -> int:
        if bound <= 0:
            return 0
        digits = str(bound)
        memo = {}
        return self.dfs(0, 0, False, True, digits, k, memo)

    def dfs(self, position: int, previous: int, started: bool, tight: bool, digits: str, k: int, memo: dict) -> int:
        if position == len(digits):
            return 1 if started else 0
        key = (position, previous, started)
        if not tight and key in memo:
            return memo[key]
        limit = ord(digits[position]) - 48 if tight else 9
        result = 0
        for digit in range(limit + 1):
            next_started = started or digit != 0
            if started and abs(previous - digit) > k:
                continue
            next_previous = digit if next_started else previous
            result += self.dfs(position + 1, next_previous, next_started, tight and digit == limit, digits, k, memo)
        if not tight:
            memo[key] = result
        return result
