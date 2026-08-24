# LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
# https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/


class Solution:
    def countWays(self, word1: str, word2: str, target: str) -> int:
        mod = 1000000007
        n1 = len(word1)
        n2 = len(word2)
        size = (n1 + 1) * (n2 + 1) * 4
        dp = [0] * size
        nxt = [0] * size
        dp[self.index(0, 0, 0, n2)] = 1
        for ti in range(len(target)):
            ch = target[ti]
            nxt = [0] * size
            for j in range(n2 + 1):
                prefix = [0] * 4
                for a in range(n1):
                    for mask in range(4):
                        prefix[mask] += dp[self.index(a, j, mask, n2)]
                        if prefix[mask] >= mod:
                            prefix[mask] -= mod
                    if word1[a] == ch:
                        for mask in range(4):
                            at = self.index(a + 1, j, mask | 1, n2)
                            nxt[at] += prefix[mask]
                            if nxt[at] >= mod:
                                nxt[at] -= mod
            for i in range(n1 + 1):
                prefix = [0] * 4
                for b in range(n2):
                    for mask in range(4):
                        prefix[mask] += dp[self.index(i, b, mask, n2)]
                        if prefix[mask] >= mod:
                            prefix[mask] -= mod
                    if word2[b] == ch:
                        for mask in range(4):
                            at = self.index(i, b + 1, mask | 2, n2)
                            nxt[at] += prefix[mask]
                            if nxt[at] >= mod:
                                nxt[at] -= mod
            dp, nxt = nxt, dp
        answer = 0
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                answer += dp[self.index(i, j, 3, n2)]
                if answer >= mod:
                    answer -= mod
        return answer

    def index(self, i: int, j: int, mask: int, n2: int) -> int:
        return ((i * (n2 + 1) + j) * 4) + mask
