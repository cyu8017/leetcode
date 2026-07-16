# LeetCode 0943 - Find the Shortest Superstring
# https://leetcode.com/problems/find-the-shortest-superstring/

class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                for k in range(min(len(a), len(b)), 0, -1):
                    if a.endswith(b[:k]):
                        overlap[i][j] = k
                        break

        dp = [[""] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = words[i]

        for mask in range(1 << n):
            for last in range(n):
                if not (mask & (1 << last)) or not dp[mask][last]:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    cand = dp[mask][last] + words[nxt][overlap[last][nxt] :]
                    nmask = mask | (1 << nxt)
                    if not dp[nmask][nxt] or len(cand) < len(dp[nmask][nxt]):
                        dp[nmask][nxt] = cand

        full = (1 << n) - 1
        return min((s for s in dp[full] if s), key=len)
