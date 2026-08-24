# LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
# https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

from typing import List

INF3892 = (1 << 53) // 4


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 0
        if k > n // 2:
            return -1
        cost = [0] * n
        for i in range(n):
            left = nums[(i + n - 1) % n]
            right = nums[(i + 1) % n]
            need = max(left, right)
            if need >= nums[i]:
                cost[i] = need - nums[i] + 1

        def line(left: int, right: int, choose: int) -> int:
            if choose == 0:
                return 0
            if left > right or choose > (right - left + 2) // 2:
                return INF3892
            prev2 = [INF3892] * (choose + 1)
            prev1 = [INF3892] * (choose + 1)
            prev2[0] = prev1[0] = 0
            for i in range(left, right + 1):
                current = prev1[:]
                for j in range(1, choose + 1):
                    if prev2[j - 1] != INF3892 and prev2[j - 1] + cost[i] < current[j]:
                        current[j] = prev2[j - 1] + cost[i]
                prev2 = prev1
                prev1 = current
            return prev1[choose]

        answer = line(1, n - 1, k)
        with_first = line(2, n - 2, k - 1)
        if with_first != INF3892:
            with_first += cost[0]
            answer = min(answer, with_first)
        if answer == INF3892:
            return -1
        return answer
