# LeetCode 2698 - Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s: str, i: int, sm: int, target: int) -> bool:
            if i == len(s):
                return sm == target
            cur = 0
            for j in range(i, len(s)):
                cur = cur * 10 + (ord(s[j]) - 48)
                if sm + cur > target:
                    break
                if dfs(s, j + 1, sm + cur, target):
                    return True
            return False

        ans = 0
        for i in range(1, n + 1):
            sq = i * i
            if dfs(str(sq), 0, 0, i):
                ans += sq
        return ans
