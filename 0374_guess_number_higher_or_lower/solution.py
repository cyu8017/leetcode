# LeetCode 0374 - Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is patched by the test runner.


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0:
                right = mid - 1
            else:
                left = mid + 1

        return left
