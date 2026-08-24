# LeetCode 3412 - Find Mirror Score of a String
# https://leetcode.com/problems/find-mirror-score-of-a-string/


class Solution:
    def calculateScore(self, s: str) -> int:
        stacks = [[] for _ in range(26)]
        ans = 0
        for i, ch in enumerate(s):
            ci = ord(ch) - 97
            mir = 25 - ci
            if stacks[mir]:
                j = stacks[mir].pop()
                ans += i - j
            else:
                stacks[ci].append(i)
        return ans
