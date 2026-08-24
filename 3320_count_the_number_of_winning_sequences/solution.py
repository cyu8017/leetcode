# LeetCode 3320 - Count the Number of Winning Sequences
# https://leetcode.com/problems/count-the-number-of-winning-sequences/


class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        mp = {"F": 0, "W": 1, "E": 2}
        beat = [2, 0, 1]
        score = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                if a == b:
                    score[a][b] = 0
                elif beat[a] == b:
                    score[a][b] = 1
                else:
                    score[a][b] = -1
        offset = n
        dp = [[0] * (2 * n + 1) for _ in range(3)]
        b0 = mp[s[0]]
        for a in range(3):
            dp[a][score[a][b0] + offset] = 1
        for i in range(1, n):
            ndp = [[0] * (2 * n + 1) for _ in range(3)]
            b = mp[s[i]]
            for last in range(3):
                for d in range(2 * n + 1):
                    if dp[last][d] == 0:
                        continue
                    for a in range(3):
                        if a == last:
                            continue
                        nd = d + score[a][b]
                        if nd < 0 or nd > 2 * n:
                            continue
                        ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
            dp = ndp
        ans = 0
        for a in range(3):
            for d in range(offset + 1, 2 * n + 1):
                ans = (ans + dp[a][d]) % mod
        return ans
