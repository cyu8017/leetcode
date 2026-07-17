# LeetCode 1871 - Jump Game VII
# https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        prefix = [0] * (n + 1)

        for i in range(n):
            if i > 0 and s[i] == "0":
                left = max(0, i - maxJump)
                right = i - minJump
                if right >= left and prefix[right + 1] - prefix[left] > 0:
                    reachable[i] = True
            prefix[i + 1] = prefix[i] + (1 if reachable[i] else 0)

        return reachable[n - 1]
