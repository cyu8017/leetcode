# LeetCode 0793 - Preimage Size of Factorial Zeroes Function
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeros(x: int) -> int:
            count = 0
            while x:
                x //= 5
                count += x
            return count

        def first_ge(target: int) -> int:
            lo, hi = 0, 5 * (target + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if zeros(mid) < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return 5 if zeros(first_ge(k)) == k else 0
