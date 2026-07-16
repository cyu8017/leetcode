# LeetCode 1088 - Confusing Number II
# https://leetcode.com/problems/confusing-number-ii/

class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        digits = [0, 1, 6, 8, 9]
        ans = 0

        def is_confusing(num: int) -> bool:
            original = num
            rotated = 0
            while num:
                d = num % 10
                rotated = rotated * 10 + rotate[d]
                num //= 10
            return rotated != original

        def dfs(cur: int) -> None:
            nonlocal ans
            if cur > n:
                return
            if cur and is_confusing(cur):
                ans += 1
            if cur == 0:
                for d in (1, 6, 8, 9):
                    dfs(d)
            else:
                for d in digits:
                    dfs(cur * 10 + d)

        dfs(0)
        return ans
