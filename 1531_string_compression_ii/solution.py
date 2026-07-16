# LeetCode 1531

class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        from functools import lru_cache
        @lru_cache(None)
        def dp(index, remaining):
            if remaining < 0:
                return 10**9
            if index == len(s) or len(s) - index <= remaining:
                return 0
            answer = dp(index + 1, remaining - 1)
            same = removed = 0
            for j in range(index, len(s)):
                if s[j] == s[index]:
                    same += 1
                    encoded = 1 + (same >= 2) + (same >= 10) + (same >= 100)
                    answer = min(answer, encoded + dp(j + 1, remaining - removed))
                else:
                    removed += 1
                    if removed > remaining:
                        break
            return answer
        return dp(0, k)
