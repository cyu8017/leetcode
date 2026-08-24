# LeetCode 2761 - Prime Pairs With Target Sum
# https://leetcode.com/problems/prime-pairs-with-target-sum/

from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        i = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        ans = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                ans.append([x, y])
        return ans
