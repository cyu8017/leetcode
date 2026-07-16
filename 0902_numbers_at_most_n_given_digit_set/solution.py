# LeetCode 0902 - Numbers At Most N Given Digit Set
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        s = str(n)
        m = len(s)
        digits = sorted(digits)
        k = len(digits)

        def count_len(length: int) -> int:
            return k**length

        def count_up_to(s: str) -> int:
            if not s:
                return 0
            first = len([d for d in digits if d < s[0]])
            ways = first * (k ** (len(s) - 1))
            if s[0] in digits:
                ways += count_up_to(s[1:])
            return ways

        ans = sum(count_len(i) for i in range(1, m))
        ans += count_up_to(s)
        return ans
