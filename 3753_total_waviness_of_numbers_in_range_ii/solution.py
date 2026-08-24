# LeetCode 3753 - Total Waviness of Numbers in Range II
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

from typing import Dict, Tuple


class Solution:
    def totalWaviness(self, a: int, b: int) -> int:
        def wavinessUpTo(limit: int) -> int:
            if limit < 0:
                return 0
            digits = []
            if limit == 0:
                digits.append(0)
            else:
                value = limit
                while value > 0:
                    digits.append(value % 10)
                    value //= 10
                digits.reverse()
            memo: Dict[str, Tuple[int, int]] = {}

            def dfs(position: int, secondLast: int, last: int, started: bool, tight: bool) -> Tuple[int, int]:
                if position == len(digits):
                    return 1, 0
                key = f"{position},{secondLast},{last},{started}"
                if not tight and key in memo:
                    return memo[key]
                upper = digits[position] if tight else 9
                count = 0
                total = 0
                for digit in range(upper + 1):
                    nextTight = tight and digit == upper
                    nextSecondLast, nextLast = secondLast, last
                    nextStarted = started or digit != 0
                    add = 0
                    if not nextStarted:
                        nextSecondLast = nextLast = 10
                    elif not started:
                        nextSecondLast = 10
                        nextLast = digit
                    else:
                        if secondLast != 10 and (
                            (last > secondLast and last > digit) or (last < secondLast and last < digit)
                        ):
                            add = 1
                        nextSecondLast = last
                        nextLast = digit
                    child_count, child_sum = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight)
                    count += child_count
                    total += child_sum + add * child_count
                if not tight:
                    memo[key] = (count, total)
                return count, total

            return dfs(0, 10, 10, False, True)[1]

        return wavinessUpTo(b) - wavinessUpTo(a - 1)
