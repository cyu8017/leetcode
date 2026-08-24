# LeetCode 2231 - Largest Number After Digit Swaps by Parity
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/


class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        even = sorted((d for d in digits if d % 2 == 0), reverse=True)
        odd = sorted((d for d in digits if d % 2 == 1), reverse=True)
        ei = oi = 0
        ans = 0
        for d in digits:
            if d % 2 == 0:
                ans = ans * 10 + even[ei]
                ei += 1
            else:
                ans = ans * 10 + odd[oi]
                oi += 1
        return ans
