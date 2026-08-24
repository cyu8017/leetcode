# LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            z = o = 0
            for j in range(i, n):
                if s[j] == "0":
                    z += 1
                else:
                    o += 1
                if z <= k or o <= k:
                    ans += 1
                else:
                    break
        return ans
