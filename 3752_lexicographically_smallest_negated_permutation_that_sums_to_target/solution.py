# LeetCode 3752 - Lexicographically Smallest Negated Permutation That Sums to Target
# https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

from typing import List


class Solution:
    def lexicographicallySmallest(self, n: int, target: int) -> List[int]:
        total = n * (n + 1) // 2
        if target < -total or target > total or (total - target) % 2 != 0:
            return []
        remaining = (total - target) // 2
        negative = [False] * (n + 1)
        for value in range(n, 0, -1):
            if value <= remaining:
                negative[value] = True
                remaining -= value
        answer = []
        for value in range(n, 0, -1):
            if negative[value]:
                answer.append(-value)
        for value in range(1, n + 1):
            if not negative[value]:
                answer.append(value)
        return answer
