# LeetCode 3579 - Minimum Steps to Convert String with Operations
# https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/


class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        def calc(l: int, r: int, rev: bool) -> int:
            cnt = [[0] * 26 for _ in range(26)]
            res = 0
            for i in range(l, r + 1):
                j = r - (i - l) if rev else i
                a = ord(word1[j]) - 97
                b = ord(word2[i]) - 97
                if a != b:
                    if cnt[b][a] > 0:
                        cnt[b][a] -= 1
                    else:
                        cnt[a][b] += 1
                        res += 1
            return res

        n = len(word1)
        f = [2147483647 // 2] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                a = calc(j, i - 1, False)
                b = 1 + calc(j, i - 1, True)
                f[i] = min(f[i], f[j] + min(a, b))
        return f[n]
