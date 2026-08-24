# LeetCode 2512 - Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/

from typing import List


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        arr = [None] * len(report)
        for i in range(len(report)):
            score = 0
            for w in report[i].split(" "):
                if not w:
                    continue
                if w in pos:
                    score += 3
                elif w in neg:
                    score -= 1
            arr[i] = [student_id[i], score]
        arr.sort(key=lambda x: (-x[1], x[0]))
        return [arr[i][0] for i in range(k)]
