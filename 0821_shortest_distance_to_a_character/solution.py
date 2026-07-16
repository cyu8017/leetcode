# LeetCode 0821 - Shortest Distance to a Character
# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [0] * n
        prev = -n
        for i, ch in enumerate(s):
            if ch == c:
                prev = i
            ans[i] = i - prev
        prev = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
