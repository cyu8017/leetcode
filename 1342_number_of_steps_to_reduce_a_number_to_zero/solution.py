# LeetCode 1342 - Number Of Steps To Reduce A Number To Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            num = num // 2 if num % 2 == 0 else num - 1
            steps += 1
        return steps
