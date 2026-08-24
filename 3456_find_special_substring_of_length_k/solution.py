# LeetCode 3456 - Find Special Substring of Length K
# https://leetcode.com/problems/find-special-substring-of-length-k/


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n - k + 1):
            ok = True
            for j in range(i + 1, i + k):
                if s[j] != s[i]:
                    ok = False
                    break
            if not ok:
                continue
            if i > 0 and s[i - 1] == s[i]:
                continue
            if i + k < n and s[i + k] == s[i]:
                continue
            return True
        return False
