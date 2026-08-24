# LeetCode 2024 - Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_with(ch: str) -> int:
            left = bad = best = 0
            for right, c in enumerate(answerKey):
                if c != ch:
                    bad += 1
                while bad > k:
                    if answerKey[left] != ch:
                        bad -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best

        return max(max_with("T"), max_with("F"))
