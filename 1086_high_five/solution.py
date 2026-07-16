# LeetCode 1086 - High Five
# https://leetcode.com/problems/high-five/

from collections import defaultdict


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores: dict[int, list[int]] = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)
        ans = []
        for student_id in sorted(scores):
            top = sorted(scores[student_id], reverse=True)[:5]
            ans.append([student_id, sum(top) // 5])
        return ans
