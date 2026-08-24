# LeetCode 3766 - Minimum Operations to Make Binary Palindrome
# https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        PALS = []
        N = 1 << 14

        def isPalindrome(s: str) -> bool:
            m = len(s)
            for i in range(m // 2):
                if s[i] != s[m - 1 - i]:
                    return False
            return True

        for i in range(N):
            x = i
            if x == 0:
                sb = "0"
            else:
                bits = []
                while x > 0:
                    bits.append(chr(48 + (x & 1)))
                    x >>= 1
                sb = "".join(reversed(bits))
            if isPalindrome(sb):
                PALS.append(i)

        def lowerBound(x: int) -> int:
            lo, hi = 0, len(PALS)
            while lo < hi:
                mid = (lo + hi) >> 1
                if PALS[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = [0] * len(nums)
        for k, x in enumerate(nums):
            it = lowerBound(x)
            t = 10**18
            if it < len(PALS):
                t = PALS[it] - x
            if it > 0:
                t = min(t, x - PALS[it - 1])
            ans[k] = t
        return ans
