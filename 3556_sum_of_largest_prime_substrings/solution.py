# LeetCode 3556 - Sum of Largest Prime Substrings
# https://leetcode.com/problems/sum-of-largest-prime-substrings/

import math


def is_prime3556(x: int) -> bool:
    if x < 2:
        return False
    sqrt_x = int(math.sqrt(x))
    for i in range(2, sqrt_x + 1):
        if x % i == 0:
            return False
    return True


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        st = set()
        n = len(s)
        for i in range(n):
            x = 0
            for j in range(i, n):
                x = x * 10 + (ord(s[j]) - 48)
                if is_prime3556(x):
                    st.add(x)
        nums = sorted(st)
        ans = 0
        i = len(nums) - 1
        while i >= 0 and len(nums) - i <= 3:
            ans += nums[i]
            i -= 1
        return ans
