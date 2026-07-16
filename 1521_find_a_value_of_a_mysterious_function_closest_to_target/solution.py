# LeetCode 1521

class Solution:
    def closestToTarget(self, arr, target):
        answer = float("inf")
        current = set()
        for value in arr:
            current = {value} | {value & previous for previous in current}
            answer = min(answer, min(abs(candidate - target) for candidate in current))
        return answer
