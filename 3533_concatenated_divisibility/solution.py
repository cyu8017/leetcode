# LeetCode 3533 - Concatenated Divisibility
# https://leetcode.com/problems/concatenated-divisibility/

from typing import List


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        pows = [0] * n
        for i in range(n):
            p = 1
            num = nums[i]
            if num == 0:
                p = 10 % k
            else:
                x = num
                while x > 0:
                    p = p * 10 % k
                    x //= 10
            pows[i] = p
        memo = {}

        def dp(mask: int, mod: int) -> bool:
            if mask == (1 << n) - 1:
                return mod == 0
            key = (mask << 32) | mod
            if key in memo:
                return memo[key]
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    nm = (mod * pows[i] + nums[i]) % k
                    if dp(mask | (1 << i), nm):
                        memo[key] = True
                        return True
            memo[key] = False
            return False

        def reconstruct(mask: int, mod: int) -> List[int]:
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    nm = (mod * pows[i] + nums[i]) % k
                    if dp(mask | (1 << i), nm):
                        rest = reconstruct(mask | (1 << i), nm)
                        rest.insert(0, nums[i])
                        return rest
            return []

        if not dp(0, 0):
            return []
        return reconstruct(0, 0)
