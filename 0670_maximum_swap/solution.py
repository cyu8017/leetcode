# LeetCode 0670 - Maximum Swap
# https://leetcode.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, ch in enumerate(digits):
            for candidate in range(9, int(ch), -1):
                j = last.get(candidate, -1)
                if j > i:
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num
