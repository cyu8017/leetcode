# LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        memo = [-1] * n

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            cnt = [0] * 26
            freq = {}
            memo[i] = n - i
            for j in range(i, n):
                k = ord(s[j]) - 97
                if cnt[k] > 0:
                    c = cnt[k]
                    nv = freq[c] - 1
                    if nv == 0:
                        del freq[c]
                    else:
                        freq[c] = nv
                cnt[k] += 1
                freq[cnt[k]] = freq.get(cnt[k], 0) + 1
                if len(freq) == 1:
                    memo[i] = min(memo[i], 1 + dfs(j + 1))
            return memo[i]

        return dfs(0)
