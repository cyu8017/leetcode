# LeetCode 1894 - Find the Student that Will Replace the Chalk
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        k %= sum(chalk)
        for index, need in enumerate(chalk):
            if k < need:
                return index
            k -= need
        return 0
