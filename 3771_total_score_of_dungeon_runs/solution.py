# LeetCode 3771 - Total Score of Dungeon Runs
# https://leetcode.com/problems/total-score-of-dungeon-runs/

from typing import List


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]
        answer = n * (n + 1) // 2
        for j in range(1, n + 1):
            threshold = prefix[j] + (requirement[j - 1] - hp)
            lo, hi = 0, j
            while lo < hi:
                mid = (lo + hi) >> 1
                if prefix[mid] < threshold:
                    lo = mid + 1
                else:
                    hi = mid
            answer -= lo
        return answer
